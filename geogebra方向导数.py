#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GeoGebra 案例复刻 — 方向导数与梯度
====================================

原案例: https://www.geogebra.org/m/xveq7eyj
作者: Tuyetdong Phan-Yamada, Juan Carlos Ponce Campuzano

功能:
  - 3D 曲面 f(x,y)（可旋转）
  - 方向导数 D_u f(P) 的几何解释（可切换显示）
  - 梯度向量 ∇f(P)（蓝色箭头）
  - 方向角 θ 滑块
  - 点 P 可拖动（x, y 滑块）
  - 2D 俯视图（等高线 + 方向箭头）
  - 极坐标玫瑰图（方向导数随角度变化）
  - 信息面板（精确值、近似值、误差）

运行:
  双击旁边的「运行GeoGebra方向导数.command」
  或手动执行:
    env -u PYTHONHOME -u PYTHONPATH \\
      venv/bin/python3.14 geogebra方向导数.py
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path

# ---- 修复 TRAE SOLO 注入的 PYTHONHOME / PYTHONPATH ----
for key in ("PYTHONHOME", "PYTHONPATH"):
    os.environ.pop(key, None)

# 若不在 venv 里，尝试自动切换
_VENV_PY = Path(__file__).resolve().parent / "venv" / "bin" / "python3.14"
if _VENV_PY.exists() and Path(sys.executable).resolve() != _VENV_PY.resolve():
    os.execv(str(_VENV_PY), [str(_VENV_PY), str(Path(__file__).resolve()), *sys.argv[1:]])

import numpy as np
import matplotlib
matplotlib.use("MacOSX")
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, Slider
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# ============================================================
# 数学函数定义
# ============================================================

def f(x, y):
    """曲面函数: f(x,y) = (x² + y²) / 4"""
    return (x * x + y * y) / 4.0

def grad_f(x, y):
    """梯度: ∇f = (x/2, y/2)"""
    return 0.5 * x, 0.5 * y

def dir_deriv(x, y, ux, uy):
    """方向导数: D_u f = ∇f · u"""
    gx, gy = grad_f(x, y)
    return gx * ux + gy * uy


# ============================================================
# 颜色（GeoGebra 风格 — 白底、蓝色曲面）
# ============================================================
BG       = "#ffffff"
SURFACE  = "#5aa8d6"   # GeoGebra 蓝
TANGENT  = "#2e8b57"   # 绿色 — 精确方向导数
SECANT   = "#e87830"   # 橙色 — 近似方向导数
GRADIENT = "#1e6fb8"   # 深蓝 — 梯度
NEG_GRAD = "#c0392b"   # 红色 — 负梯度方向
DIR_U    = "#8e44ad"   # 紫色 — 当前方向 u
POINT_P  = "#e74c3c"   # 红色 — 点 P
GRID     = "#d0d0d0"
AXIS     = "#555555"
TEXT     = "#222222"
TICK     = "#666666"


class DirectionalDerivativeDemo:
    """交互式方向导数演示，复刻 GeoGebra 案例。"""

    def __init__(self):
        self.xlim = (-2.0, 4.0)
        self.ylim = (-2.0, 4.0)
        self.n_surf = 50
        self.arrow_scale = 1.4

        # 默认 P = (1, 1)（与 GeoGebra 案例一致）
        self.px0, self.py0 = 1.0, 1.0

        plt.rcParams.update({
            "font.sans-serif": [
                "PingFang SC", "Heiti SC", "STHeiti",
                "Arial Unicode MS", "SimHei", "DejaVu Sans",
            ],
            "axes.unicode_minus": False,
            "figure.facecolor": BG,
            "savefig.facecolor": BG,
            "text.color": TEXT,
            "axes.labelcolor": TEXT,
            "xtick.color": TICK,
            "ytick.color": TICK,
        })

        self.fig = plt.figure(figsize=(15, 9), facecolor=BG)
        if self.fig.canvas.manager:
            self.fig.canvas.manager.set_window_title(
                "GeoGebra 案例复刻 — 方向导数与梯度"
            )

        gs = self.fig.add_gridspec(
            2, 2,
            width_ratios=[1.6, 1.0],
            height_ratios=[1.3, 1.0],
            left=0.05, right=0.97, top=0.90, bottom=0.28,
            wspace=0.15, hspace=0.25,
        )
        self.ax3d = self.fig.add_subplot(gs[:, 0], projection="3d", facecolor=BG)
        self.ax2d = self.fig.add_subplot(gs[0, 1], facecolor="#f8f9fa")
        self.axpolar = self.fig.add_subplot(gs[1, 1], facecolor="#f8f9fa")

        self.fig.suptitle(
            "方向导数与梯度  ·  GeoGebra 案例复刻",
            fontsize=16, fontweight="bold", color=TEXT, y=0.96,
        )
        self.fig.text(
            0.06, 0.255,
            "拖拽左图旋转 · 滚轮缩放\n"
            "蓝色箭头 = 梯度（增长最快）  绿色 = 方向导数  橙色 = 割线近似\n"
            "探索: θ 为何值时 D=0?  何时 D 最大?  最大值多大?",
            fontsize=9, color="#666", va="center", linespacing=1.6,
        )

        # ---- 控件 ----
        self.s_theta = Slider(
            self.fig.add_axes([0.07, 0.20, 0.46, 0.028], facecolor="#e8e8e8"),
            "方向角 θ", 0, 360, valinit=45, valstep=1, color=DIR_U,
        )
        self.s_h = Slider(
            self.fig.add_axes([0.07, 0.155, 0.46, 0.028], facecolor="#e8e8e8"),
            "步长 h", 0.02, 2.0, valinit=1.5, valstep=0.01, color=SECANT,
        )
        self.s_px = Slider(
            self.fig.add_axes([0.07, 0.11, 0.22, 0.028], facecolor="#e8e8e8"),
            "点 Px", -1.5, 3.5, valinit=self.px0, valstep=0.05, color=POINT_P,
        )
        self.s_py = Slider(
            self.fig.add_axes([0.31, 0.11, 0.22, 0.028], facecolor="#e8e8e8"),
            "点 Py", -1.5, 3.5, valinit=self.py0, valstep=0.05, color=POINT_P,
        )
        for sl in (self.s_theta, self.s_h, self.s_px, self.s_py):
            sl.label.set_color(TEXT)
            sl.valtext.set_color(TEXT)

        self.chk = CheckButtons(
            self.fig.add_axes([0.57, 0.07, 0.18, 0.16], facecolor="#f0f0f0"),
            ["方向导数", "梯度向量", "割线近似", "所有方向", "截面曲线"],
            [True, True, True, False, True],
        )
        self._style_checkbox(self.chk)

        # 信息面板
        self.info = self.fig.text(
            0.06, 0.025, "", fontsize=10, family="monospace",
            color=TEXT, va="center", linespacing=1.5,
        )

        # 事件绑定
        self.s_theta.on_changed(self._redraw)
        self.s_h.on_changed(self._redraw)
        self.s_px.on_changed(self._redraw)
        self.s_py.on_changed(self._redraw)
        self.chk.on_clicked(self._redraw)

        # 保存视角
        self._elev, self._azim = 25, -55

        self._redraw()

    # ---- 控件样式 ----
    @staticmethod
    def _style_checkbox(chk):
        chk.ax.set_facecolor("#f0f0f0")
        for spine in chk.ax.spines.values():
            spine.set_color("#bbb")
        for txt in chk.labels:
            txt.set_color(TEXT)
            txt.set_fontsize(10)

    def _checked(self, label):
        labels = [t.get_text() for t in self.chk.labels]
        return bool(self.chk.get_status()[labels.index(label)])

    # ---- 状态计算 ----
    def _state(self):
        theta = math.radians(self.s_theta.val)
        h = float(self.s_h.val)
        px, py = float(self.s_px.val), float(self.s_py.val)
        ux, uy = math.cos(theta), math.sin(theta)
        gx, gy = grad_f(px, py)
        fp = float(f(px, py))
        fph = float(f(px + h * ux, py + h * uy))
        exact = gx * ux + gy * uy
        approx = (fph - fp) / h if h > 1e-9 else exact
        gnorm = math.hypot(gx, gy)
        gdir = math.atan2(gy, gx) if gnorm > 1e-12 else 0.0
        return dict(
            theta=theta, h=h, px=px, py=py, fp=fp,
            ux=ux, uy=uy, gx=gx, gy=gy, gnorm=gnorm, gdir=gdir,
            fph=fph, exact=exact, approx=approx,
            phx=px + h * ux, phy=py + h * uy,
        )

    # ---- 3D 坐标轴 ----
    def _draw_axes_3d(self, ax, zmin, zmax):
        x0, x1 = self.xlim
        y0, y1 = self.ylim
        tl = 0.12
        # 三轴
        ax.plot([x0, x1], [y0, y0], [zmin, zmin], color=AXIS, lw=2)
        ax.plot([x0, x0], [y0, y1], [zmin, zmin], color=AXIS, lw=2)
        ax.plot([x0, x0], [y0, y0], [zmin, zmax], color=AXIS, lw=2)
        # x 轴刻度
        for x in range(int(math.ceil(x0)), int(math.floor(x1)) + 1):
            ax.plot([x, x], [y0 - tl, y0 + tl], [zmin, zmin], color=AXIS, lw=1)
            ax.text(x, y0 - 0.35, zmin, str(x), color=AXIS, fontsize=8, ha="center")
        # y 轴刻度
        for y in range(int(math.ceil(y0)), int(math.floor(y1)) + 1):
            ax.plot([x0 - tl, x0 + tl], [y, y], [zmin, zmin], color=AXIS, lw=1)
            ax.text(x0 - 0.35, y, zmin, str(y), color=AXIS, fontsize=8, ha="right")
        # z 轴刻度
        span = max(zmax - zmin, 1.0)
        z_step = 1.0 if span >= 3.5 else (0.5 if span >= 1.6 else 0.25)
        z_start = math.ceil(zmin / z_step) * z_step
        for z in np.arange(z_start, zmax + 1e-9, z_step):
            ax.plot([x0 - tl, x0 + tl], [y0, y0], [z, z], color=AXIS, lw=1)
            label = f"{z:.0f}" if abs(z - round(z)) < 1e-9 else f"{z:.2f}"
            ax.text(x0 - 0.3, y0, z, label, color=AXIS, fontsize=8, ha="right")
        # 轴标签
        ax.text(x1 + 0.2, y0, zmin, "x", color=AXIS, fontsize=13, fontweight="bold")
        ax.text(x0, y1 + 0.2, zmin, "y", color=AXIS, fontsize=13, fontweight="bold")
        ax.text(x0, y0, zmax + 0.08 * span, "z", color=AXIS, fontsize=13, fontweight="bold")
        # 地面网格
        for x in range(int(math.ceil(x0)), int(math.floor(x1)) + 1):
            ax.plot([x, x], [y0, y1], [zmin, zmin], color=GRID, lw=0.5, alpha=0.6)
        for y in range(int(math.ceil(y0)), int(math.floor(y1)) + 1):
            ax.plot([x0, x1], [y, y], [zmin, zmin], color=GRID, lw=0.5, alpha=0.6)

    # ---- 箭头工具 ----
    @staticmethod
    def _arrow(ax, origin, vec, color, lw=2.2, alpha=1.0, ratio=0.15):
        o = np.asarray(origin, dtype=float)
        v = np.asarray(vec, dtype=float)
        if np.linalg.norm(v) < 1e-9:
            return
        ax.quiver(o[0], o[1], o[2], v[0], v[1], v[2],
                  color=color, linewidth=lw, arrow_length_ratio=ratio,
                  alpha=alpha, normalize=False, zorder=30)

    def _tangent_vec(self, ux, uy, dval):
        """切线方向 (ux, uy, D)，长度 ∝ |D|。"""
        if abs(dval) < 0.005:
            return None
        t = np.array([ux, uy, dval], dtype=float)
        n = float(np.linalg.norm(t))
        if n < 1e-9:
            return None
        return t / n * (self.arrow_scale * 2.5 * abs(dval))

    @staticmethod
    def _style_3d(ax, zmin, zmax, xlim, ylim):
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_zlim(zmin, zmax)
        try:
            ax.set_box_aspect((1.0, 1.0, 0.7))
        except Exception:
            pass
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_zlabel("")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
            pane.set_facecolor((0.95, 0.95, 0.97, 0.3))
            pane.set_edgecolor("#ccc")
        ax.grid(False)

    # ---- 主绘制 ----
    def _redraw(self, _=None):
        st = self._state()
        px, py, fp = st["px"], st["py"], st["fp"]
        ux, uy = st["ux"], st["uy"]
        gx, gy = st["gx"], st["gy"]
        sc = self.arrow_scale

        show_dir  = self._checked("方向导数")
        show_grad = self._checked("梯度向量")
        show_sec  = self._checked("割线近似")
        show_all  = self._checked("所有方向")
        show_curve = self._checked("截面曲线")

        # 曲面数据
        xs = np.linspace(*self.xlim, self.n_surf)
        ys = np.linspace(*self.ylim, self.n_surf)
        X, Y = np.meshgrid(xs, ys)
        Z = np.asarray(f(X, Y), dtype=float)
        zmin = max(float(np.min(Z)) - 0.3, -0.5)
        zmax = float(np.max(Z)) + 0.5

        # 保存用户旋转视角
        elev = self.ax3d.elev if self.ax3d.elev is not None else self._elev
        azim = self.ax3d.azim if self.ax3d.azim is not None else self._azim
        self._elev, self._azim = elev, azim

        self.ax3d.cla()
        self.ax2d.cla()
        self.axpolar.cla()
        self._style_3d(self.ax3d, zmin, zmax, self.xlim, self.ylim)
        self.ax3d.view_init(elev=elev, azim=azim)
        self._draw_axes_3d(self.ax3d, zmin, zmax)

        # 曲面 — GeoGebra 风格蓝色
        self.ax3d.plot_surface(
            X, Y, Z,
            cmap="Blues", linewidth=0.1, antialiased=True,
            alpha=0.55, edgecolor="#bbb", rstride=3, cstride=3, shade=True,
        )

        # 点 P 的铅垂线 + 标记
        self.ax3d.plot([px, px], [py, py], [zmin, fp], color=POINT_P, ls="--", lw=1, alpha=0.5)
        self.ax3d.scatter([px], [py], [zmin], color=POINT_P, s=20, alpha=0.6, depthshade=False)
        self.ax3d.scatter([px], [py], [fp], color=POINT_P, s=60, depthshade=False, zorder=40)
        self.ax3d.text(px, py, fp + 0.12, "P", color=POINT_P, fontsize=11, fontweight="bold")

        # xy 平面上的方向 u（紫色箭头）
        self._arrow(self.ax3d, (px, py, zmin), (sc * ux, sc * uy, 0), DIR_U, lw=2.0, alpha=0.8)
        self._arrow(self.ax3d, (px, py, zmin), (sc * ux, sc * uy, 0), DIR_U, lw=2.0, alpha=0.8)

        # ---- 所有方向模式 ----
        if show_all:
            segs, cols, widths = [], [], []
            for deg in range(0, 360, 10):
                a = math.radians(deg)
                dux, duy = math.cos(a), math.sin(a)
                dval = gx * dux + gy * duy
                vec = self._tangent_vec(dux, duy, dval)
                if vec is None:
                    continue
                origin = np.array([px, py, fp])
                segs.append([origin, origin + vec])
                is_cur = abs((deg - self.s_theta.val) % 360) < 6
                if is_cur:
                    cols.append(TANGENT)
                    widths.append(2.6)
                elif dval >= 0:
                    cols.append((0.18, 0.55, 0.34, 0.5))
                    widths.append(1.4)
                else:
                    cols.append((0.75, 0.22, 0.16, 0.5))
                    widths.append(1.4)
            if segs:
                self.ax3d.add_collection3d(Line3DCollection(segs, colors=cols, linewidths=widths))
            # 方向圆
            ang = np.linspace(0, 2 * np.pi, 80)
            self.ax3d.plot(
                px + sc * np.cos(ang), py + sc * np.sin(ang),
                np.full_like(ang, zmin), color="#888", lw=0.8, alpha=0.4, ls="--",
            )

        # ---- 方向导数（精确值） ----
        if show_dir and not show_all:
            vec = self._tangent_vec(ux, uy, st["exact"])
            if vec is not None:
                self._arrow(self.ax3d, (px, py, fp), vec, TANGENT, lw=2.6, ratio=0.14)
                tip = np.array([px, py, fp]) + vec
                self.ax3d.text(tip[0], tip[1], tip[2] + 0.08,
                               f"D={st['exact']:.3f}", color=TANGENT, fontsize=9)

        # ---- 截面曲线 ----
        if show_curve and not show_all:
            ts = np.linspace(-0.3, 2.2, 120)
            cx, cy = px + ts * ux, py + ts * uy
            cz = np.asarray(f(cx, cy), dtype=float)
            self.ax3d.plot(cx, cy, cz, color="#333", lw=2, alpha=0.7)

        # ---- 割线近似（检查点箭头） ----
        if show_sec and not show_all:
            for ch, a in [(1.5, 0.15), (1.0, 0.18), (0.7, 0.22), (0.4, 0.28), (0.2, 0.35), (0.1, 0.45)]:
                fph = float(f(px + ch * ux, py + ch * uy))
                cslope = (fph - fp) / ch
                origin = np.array([px, py, fp])
                tip = origin + sc * np.array([ux, uy, cslope])
                self.ax3d.plot(*zip(origin, tip), color=SECANT, lw=1, alpha=a)
            # 当前 h 的割线
            phx, phy, fph = st["phx"], st["phy"], st["fph"]
            self.ax3d.plot([px, phx], [py, phy], [fp, fph], color=SECANT, lw=2, alpha=0.85)
            self.ax3d.scatter([phx], [phy], [fph], color=SECANT, s=40, depthshade=False)
            self.ax3d.text(phx, phy, fph + 0.1, "P+hu", color=SECANT, fontsize=9)
            # 近似方向导数箭头
            avec = self._tangent_vec(ux, uy, st["approx"])
            if avec is not None:
                self._arrow(self.ax3d, (px, py, fp), avec, SECANT, lw=2.0)

        # ---- 梯度向量（蓝色箭头） ----
        if show_grad and st["gnorm"] > 1e-10:
            ngx, ngy = gx / st["gnorm"], gy / st["gnorm"]
            gvec = self._tangent_vec(ngx, ngy, st["gnorm"])
            if gvec is not None:
                self._arrow(self.ax3d, (px, py, fp), gvec, GRADIENT, lw=3.0, ratio=0.12)
                tip = np.array([px, py, fp]) + gvec
                self.ax3d.text(tip[0], tip[1], tip[2] + 0.08,
                               f"∇f={st['gnorm']:.3f}", color=GRADIENT, fontsize=9)
            # xy 平面上的梯度投影
            self._arrow(self.ax3d, (px, py, zmin),
                        (sc * ngx, sc * ngy, 0), GRADIENT, lw=1.8, alpha=0.7, ratio=0.14)

        # 2D 俯视图 & 极坐标图
        self._draw_top_view(st, show_all, show_grad)
        self._draw_polar_rose(st)
        self._draw_info(st)

        self.fig.canvas.draw_idle()

    # ---- 2D 俯视图 ----
    def _draw_top_view(self, st, show_all, show_grad):
        ax = self.ax2d
        px, py, ux, uy = st["px"], st["py"], st["ux"], st["uy"]
        gx, gy = st["gx"], st["gy"]
        xs = np.linspace(*self.xlim, 80)
        ys = np.linspace(*self.ylim, 80)
        X, Y = np.meshgrid(xs, ys)
        Z = np.asarray(f(X, Y), dtype=float)

        ax.set_facecolor("#f8f9fa")
        ax.contourf(X, Y, Z, levels=14, cmap="Blues", alpha=0.8)
        ax.contour(X, Y, Z, levels=14, colors="#888", linewidths=0.3, alpha=0.4)
        ax.axhline(0, color="#aaa", lw=0.5)
        ax.axvline(0, color="#aaa", lw=0.5)

        # 坐标轴标签
        ax.plot([self.xlim[0], self.xlim[1]], [self.ylim[0], self.ylim[0]], color=AXIS, lw=1.5)
        ax.plot([self.xlim[0], self.xlim[0]], [self.ylim[0], self.ylim[1]], color=AXIS, lw=1.5)
        ax.text(self.xlim[1] - 0.05, self.ylim[0] - 0.08, "x", color=AXIS, fontsize=10, ha="right")
        ax.text(self.xlim[0] - 0.08, self.ylim[1] - 0.05, "y", color=AXIS, fontsize=10, ha="right")
        ax.tick_params(colors=TICK, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color("#ccc")

        r = self.arrow_scale
        gnorm = max(st["gnorm"], 1e-9)
        circ = plt.Circle((px, py), r, fill=False, ec="#888", lw=0.8, ls="--", alpha=0.6)
        ax.add_patch(circ)

        # 所有方向
        if show_all:
            for deg in range(0, 360, 10):
                a = math.radians(deg)
                dux, duy = math.cos(a), math.sin(a)
                dval = gx * dux + gy * duy
                if abs(dval) < 0.005:
                    continue
                L = r * abs(dval) / gnorm
                col = TANGENT if dval >= 0 else NEG_GRAD
                ax.annotate("", xy=(px + L * dux, py + L * duy), xytext=(px, py),
                            arrowprops=dict(arrowstyle="-|>", color=col, lw=1, alpha=0.5))

        # 当前方向 u
        ax.annotate("", xy=(px + r * ux, py + r * uy), xytext=(px, py),
                    arrowprops=dict(arrowstyle="-|>", color=DIR_U, lw=2.2))
        ax.text(px + r * ux * 1.1, py + r * uy * 1.1, "u", color=DIR_U, fontsize=9)

        # 梯度
        if show_grad and st["gnorm"] > 1e-10:
            ngx, ngy = gx / gnorm, gy / gnorm
            ax.annotate("", xy=(px + r * ngx, py + r * ngy), xytext=(px, py),
                        arrowprops=dict(arrowstyle="-|>", color=GRADIENT, lw=2.5))
            ax.text(px + 1.1 * r * ngx, py + 1.1 * r * ngy, "∇f", color=GRADIENT, fontsize=9)

        ax.plot(px, py, "o", color=POINT_P, ms=7, zorder=5)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(*self.xlim)
        ax.set_ylim(*self.ylim)
        ax.set_title("俯视图 · 等高线 + 方向箭头", color=TEXT, fontsize=11)

    # ---- 极坐标玫瑰图 ----
    def _draw_polar_rose(self, st):
        ax = self.axpolar
        ax.set_facecolor("#f8f9fa")
        gx, gy = st["gx"], st["gy"]
        gnorm = max(st["gnorm"], 1e-9)

        thetas = np.linspace(0, 2 * np.pi, 361)
        vals = gx * np.cos(thetas) + gy * np.sin(thetas)
        xs = vals * np.cos(thetas)
        ys = vals * np.sin(thetas)

        pos = vals >= 0
        ax.plot(xs[pos], ys[pos], color=TANGENT, lw=2.2, label="D > 0 升高")
        ax.plot(xs[~pos], ys[~pos], color=NEG_GRAD, lw=2.2, label="D < 0 下降")
        ax.fill(xs, ys, color=TANGENT, alpha=0.08)

        lim = gnorm * 1.5
        ax.axhline(0, color="#aaa", lw=0.5)
        ax.axvline(0, color="#aaa", lw=0.5)
        ax.add_patch(plt.Circle((0, 0), gnorm, fill=False, ec="#999", lw=0.6, ls=":", alpha=0.7))

        for deg in range(0, 360, 45):
            a = math.radians(deg)
            ax.plot([0, lim * math.cos(a)], [0, lim * math.sin(a)], color="#e0e0e0", lw=0.5)
            ax.text(1.06 * lim * math.cos(a), 1.06 * lim * math.sin(a),
                    f"{deg}°", color=TICK, fontsize=7, ha="center")

        # 当前方向
        cx, cy = st["exact"] * math.cos(st["theta"]), st["exact"] * math.sin(st["theta"])
        ax.annotate("", xy=(cx, cy), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=SECANT, lw=2))
        ax.plot(cx, cy, "o", color=SECANT, ms=6, zorder=5)

        # 梯度方向
        if gnorm > 1e-10:
            ax.annotate("", xy=(gx, gy), xytext=(0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=GRADIENT, lw=2.2))
            ax.plot(gx, gy, "o", color=GRADIENT, ms=7, zorder=6)

        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.tick_params(colors=TICK, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color("#ccc")
        ax.set_xlabel("D·cos θ", color=TICK, fontsize=8)
        ax.set_ylabel("D·sin θ", color=TICK, fontsize=8)
        ax.set_title("方向导数玫瑰 · 直径 = |∇f|", color=TEXT, fontsize=10, pad=8)
        ax.grid(color="#eee", alpha=0.8)

    # ---- 信息面板 ----
    def _draw_info(self, st):
        deg = self.s_theta.val
        gdeg = math.degrees(st["gdir"]) % 360
        err = abs(st["approx"] - st["exact"])
        phi = abs(((deg - gdeg + 180) % 360) - 180)
        self.info.set_text(
            f"P=({st['px']:.2f}, {st['py']:.2f})   f(P)={st['fp']:.4f}   "
            f"u=(cos {deg:.0f}°, sin {deg:.0f}°)   "
            f"∇f=({st['gx']:.3f}, {st['gy']:.3f})   |∇f|={st['gnorm']:.4f}\n"
            f"精确 D_u f = {st['exact']:+.4f}     "
            f"近似 D* = {st['approx']:+.4f}     "
            f"误差 = {err:.4f}     "
            f"梯度方向 θ={gdeg:.1f}°     "
            f"夹角 φ={phi:.1f}°     "
            f"|D|={abs(st['exact']):.4f}"
        )

    def show(self):
        plt.show()


def main():
    try:
        DirectionalDerivativeDemo().show()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
