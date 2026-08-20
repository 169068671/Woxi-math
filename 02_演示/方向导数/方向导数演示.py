#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
方向导数 3D 交互演示
====================

对应原来的 HTML / Woxi 演示，并修正坐标系：

    xy 平面在下方（地面），z 轴竖直向上，三轴都有刻度。

函数默认：f(x, y) = (x² + y²) / 4
点 P、方向角 θ、步长 h 都可以拖动。

方向导数：
    D_u f(P) = lim_{h→0} [f(P + h u) − f(P)] / h
             = ∇f(P) · u
             = |∇f(P)| cos φ

其中 u = (cos θ, sin θ) 是单位方向，φ 是 u 与梯度的夹角。
梯度方向就是函数值增长最快的方向，大小 |∇f| 就是最大方向导数。

运行：
    "/Users/wangzirui/Woxi mathmatic平替/venv/bin/python" \\
        "/Users/wangzirui/Woxi mathmatic平替/02_演示/方向导数/方向导数演示.py"
或双击旁边的「运行方向导数演示.command」。
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path


def _vault_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "00_HOME").is_dir():
            return p
    return start


_VAULT_ROOT = _vault_root(Path(__file__).resolve().parent)
_VENV_PYTHON = _VAULT_ROOT / "venv" / "bin" / "python"
if _VENV_PYTHON.exists() and Path(sys.executable).resolve() != _VENV_PYTHON.resolve():
    os.execv(str(_VENV_PYTHON), [str(_VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, RadioButtons, Slider
from mpl_toolkits.mplot3d.art3d import Line3DCollection


# ---------------------------------------------------------------------------
# 函数库
# ---------------------------------------------------------------------------
def _parab(x, y):
    return (x * x + y * y) / 4.0


def _parab_grad(x, y):
    return 0.5 * x, 0.5 * y


def _saddle(x, y):
    return 0.5 * x * y


def _saddle_grad(x, y):
    return 0.5 * y, 0.5 * x


def _gauss(x, y):
    return np.exp(-0.5 * (x * x + y * y))


def _gauss_grad(x, y):
    f = _gauss(x, y)
    return -x * f, -y * f


FUNCTIONS = {
    "抛物面  (x²+y²)/4": {
        "f": _parab,
        "grad": _parab_grad,
        "p0": (1.0, 1.0),
        "zmax": 4.0,
        "formula": r"$f(x,y)=(x^2+y^2)/4$",
    },
    "马鞍面  xy/2": {
        "f": _saddle,
        "grad": _saddle_grad,
        "p0": (1.0, 1.0),
        "zmax": 3.0,
        "formula": r"$f(x,y)=xy/2$",
    },
    "高斯包  e^{-(x²+y²)/2}": {
        "f": _gauss,
        "grad": _gauss_grad,
        "p0": (0.8, 0.4),
        "zmax": 1.3,
        "formula": r"$f(x,y)=e^{-(x^2+y^2)/2}$",
    },
}


# 配色（深色场景，和原来的 HTML 接近）
BG = "#141428"
PANEL = "#1c1c36"
AXIS_X = "#ff6b6b"
AXIS_Y = "#51cf66"
AXIS_Z = "#74c0fc"
TICK = "#9aa3c7"
SURFACE_CMAP = "YlGnBu"
CYAN = "#22d3ee"
GREEN = "#4ade80"
ORANGE = "#fb923c"
GOLD = "#f8fafc"
CRIMSON = "#f87171"
MUTED = "#64748b"


class DirectionalDerivativeDemo:
    def __init__(self):
        self.fn_name = next(iter(FUNCTIONS))
        self.xlim = (-1.0, 3.0)
        self.ylim = (-1.0, 3.0)
        self.n_surf = 48
        self.arrow_scale = 1.35
        self._view = (24, -60)  # elev, azim：从上斜看，xy 在下、z 朝上

        plt.rcParams.update(
            {
                "font.sans-serif": [
                    "PingFang SC",
                    "Heiti SC",
                    "STHeiti",
                    "Arial Unicode MS",
                    "SimHei",
                    "DejaVu Sans",
                ],
                "axes.unicode_minus": False,
                "figure.facecolor": BG,
                "savefig.facecolor": BG,
                "text.color": "#e2e8f0",
                "axes.labelcolor": "#e2e8f0",
                "xtick.color": TICK,
                "ytick.color": TICK,
            }
        )

        self.fig = plt.figure(figsize=(15.4, 9.2), facecolor=BG)
        if self.fig.canvas.manager is not None:
            self.fig.canvas.manager.set_window_title("方向导数演示  ·  xy 在下，z 竖直向上")

        gs = self.fig.add_gridspec(
            2,
            2,
            width_ratios=[1.55, 1.0],
            height_ratios=[1.35, 1.0],
            left=0.04,
            right=0.98,
            top=0.90,
            bottom=0.30,
            wspace=0.18,
            hspace=0.28,
        )
        self.ax3d = self.fig.add_subplot(gs[:, 0], projection="3d", facecolor=BG)
        self.ax2d = self.fig.add_subplot(gs[0, 1], facecolor="#16162c")
        # 用直角坐标画「方向导数玫瑰」：点 (D cosθ, D sinθ) 是过原点的圆
        self.axpolar = self.fig.add_subplot(gs[1, 1], facecolor="#16162c")

        self.fig.suptitle(
            "方向导数演示    xy 平面在下，z 轴垂直向上（轴上有刻度）",
            fontsize=15,
            fontweight="bold",
            color="#dbeafe",
            y=0.97,
        )
        self.fig.text(
            0.07,
            0.255,
            "拖拽左图旋转 · 滚轮缩放    箭头长短 = |方向导数|    白箭头最长=增长最快    垂直梯度处几乎没有箭头    青箭头=xy 上的方向 u",
            fontsize=9,
            color="#94a3b8",
        )

        spec = FUNCTIONS[self.fn_name]
        px, py = spec["p0"]

        self.s_theta = Slider(
            self.fig.add_axes([0.07, 0.21, 0.50, 0.028], facecolor="#243044"),
            "方向角 θ",
            0.0,
            360.0,
            valinit=45.0,
            valstep=1.0,
            color=CYAN,
        )
        self.s_h = Slider(
            self.fig.add_axes([0.07, 0.165, 0.50, 0.028], facecolor="#243044"),
            "步长 h",
            0.02,
            2.0,
            valinit=1.50,
            valstep=0.01,
            color=ORANGE,
        )
        self.s_px = Slider(
            self.fig.add_axes([0.07, 0.12, 0.23, 0.028], facecolor="#243044"),
            "点 Px",
            self.xlim[0] + 0.3,
            self.xlim[1] - 0.3,
            valinit=px,
            valstep=0.05,
            color=CRIMSON,
        )
        self.s_py = Slider(
            self.fig.add_axes([0.34, 0.12, 0.23, 0.028], facecolor="#243044"),
            "点 Py",
            self.ylim[0] + 0.3,
            self.ylim[1] - 0.3,
            valinit=py,
            valstep=0.05,
            color=CRIMSON,
        )
        for sl in (self.s_theta, self.s_h, self.s_px, self.s_py):
            sl.label.set_color("#cbd5e1")
            sl.valtext.set_color("#e2e8f0")

        self.chk = CheckButtons(
            self.fig.add_axes([0.62, 0.08, 0.16, 0.16], facecolor=PANEL),
            ["所有方向", "最快增长", "最快下降", "割线近似", "截面曲线"],
            [True, True, False, True, True],
        )
        self._style_check(self.chk)

        self.radio = RadioButtons(
            self.fig.add_axes([0.80, 0.08, 0.18, 0.16], facecolor=PANEL),
            list(FUNCTIONS.keys()),
            active=0,
            activecolor=CYAN,
        )
        self._style_radio(self.radio)

        self.info = self.fig.text(
            0.07,
            0.035,
            "",
            fontsize=10,
            family="sans-serif",
            color="#e2e8f0",
            va="center",
            linespacing=1.45,
        )

        self.s_theta.on_changed(self._on_change)
        self.s_h.on_changed(self._on_change)
        self.s_px.on_changed(self._on_change)
        self.s_py.on_changed(self._on_change)
        self.chk.on_clicked(self._on_change)
        self.radio.on_clicked(self._on_function)

        self._draw()

    # ----- 控件外观 -----
    @staticmethod
    def _style_check(chk: CheckButtons) -> None:
        chk.ax.set_facecolor(PANEL)
        for spine in chk.ax.spines.values():
            spine.set_color("#334155")
        for txt in chk.labels:
            txt.set_color("#e2e8f0")
            txt.set_fontsize(10)
        try:
            for rect in chk.rectangles:
                rect.set_facecolor("#0f172a")
                rect.set_edgecolor("#94a3b8")
        except Exception:
            pass

    @staticmethod
    def _style_radio(radio: RadioButtons) -> None:
        radio.ax.set_facecolor(PANEL)
        for spine in radio.ax.spines.values():
            spine.set_color("#334155")
        for txt in radio.labels:
            txt.set_color("#e2e8f0")
            txt.set_fontsize(9)

    def _checked(self, label: str) -> bool:
        labels = [t.get_text() for t in self.chk.labels]
        status = list(self.chk.get_status())
        return bool(status[labels.index(label)])

    # ----- 数学 -----
    def _current_fn(self):
        spec = FUNCTIONS[self.fn_name]
        return spec["f"], spec["grad"], spec

    def _state(self):
        f, grad, spec = self._current_fn()
        theta = math.radians(self.s_theta.val)
        h = float(self.s_h.val)
        px, py = float(self.s_px.val), float(self.s_py.val)
        ux, uy = math.cos(theta), math.sin(theta)
        gx, gy = grad(px, py)
        fp = float(f(px, py))
        phx, phy = px + h * ux, py + h * uy
        fph = float(f(phx, phy))
        approx = (fph - fp) / h
        exact = gx * ux + gy * uy
        gnorm = math.hypot(gx, gy)
        gdir = math.atan2(gy, gx) if gnorm > 1e-12 else 0.0
        return {
            "f": f,
            "grad": grad,
            "spec": spec,
            "theta": theta,
            "h": h,
            "p": (px, py, fp),
            "u": (ux, uy),
            "g": (gx, gy),
            "gnorm": gnorm,
            "gdir": gdir,
            "ph": (phx, phy, fph),
            "approx": approx,
            "exact": exact,
        }

    # ----- 坐标轴：xy 在地面，z 竖直，带刻度 -----
    def _draw_axes(self, ax, zmin: float, zmax: float) -> None:
        x0, x1 = self.xlim
        y0, y1 = self.ylim
        z0, z1 = zmin, zmax
        tick_len = 0.10

        ax.plot([x0, x1], [y0, y0], [z0, z0], color=AXIS_X, lw=2.0, zorder=20)
        ax.plot([x0, x0], [y0, y1], [z0, z0], color=AXIS_Y, lw=2.0, zorder=20)
        ax.plot([x0, x0], [y0, y0], [z0, z1], color=AXIS_Z, lw=2.0, zorder=20)

        for x in np.arange(math.ceil(x0), math.floor(x1) + 0.01, 1.0):
            ax.plot([x, x], [y0 - tick_len, y0 + tick_len], [z0, z0], color=AXIS_X, lw=1.2)
            ax.text(x, y0 - 0.32, z0, f"{int(x)}", color=AXIS_X, fontsize=8, ha="center", va="top")
        for y in np.arange(math.ceil(y0), math.floor(y1) + 0.01, 1.0):
            ax.plot([x0 - tick_len, x0 + tick_len], [y, y], [z0, z0], color=AXIS_Y, lw=1.2)
            ax.text(x0 - 0.32, y, z0, f"{int(y)}", color=AXIS_Y, fontsize=8, ha="right", va="center")

        span = max(z1 - z0, 1e-6)
        z_step = 1.0 if span >= 3.5 else (0.5 if span >= 1.6 else 0.2)
        z_start = math.ceil(z0 / z_step) * z_step
        z_vals = np.arange(z_start, z1 + 1e-9, z_step)
        for z in z_vals:
            ax.plot([x0 - tick_len, x0 + tick_len], [y0, y0], [z, z], color=AXIS_Z, lw=1.2)
            label = f"{z:.0f}" if abs(z - round(z)) < 1e-9 else f"{z:.1f}"
            ax.text(x0 - 0.28, y0, z, label, color=AXIS_Z, fontsize=8, ha="right", va="center")

        ax.text(x1 + 0.18, y0, z0, "x", color=AXIS_X, fontsize=13, fontweight="bold")
        ax.text(x0, y1 + 0.18, z0, "y", color=AXIS_Y, fontsize=13, fontweight="bold")
        ax.text(x0, y0, z1 + 0.08 * span, "z", color=AXIS_Z, fontsize=13, fontweight="bold")

        grid_c = "#2a2a48"
        xs = np.arange(math.ceil(x0), math.floor(x1) + 0.01, 1.0)
        ys = np.arange(math.ceil(y0), math.floor(y1) + 0.01, 1.0)
        for x in xs:
            ax.plot([x, x], [y0, y1], [z0, z0], color=grid_c, lw=0.6, alpha=0.7)
        for y in ys:
            ax.plot([x0, x1], [y, y], [z0, z0], color=grid_c, lw=0.6, alpha=0.7)
        ax.plot([x0, x1, x1, x0, x0], [y0, y0, y1, y1, y0], [z0] * 5,
                color="#3b3b62", lw=0.8, alpha=0.8)

        # 若盒子底部不是 z=0，另画真正的 xy 平面
        if z0 < -1e-6:
            for x in xs:
                ax.plot([x, x], [y0, y1], [0, 0], color="#3f4c6b", lw=0.5, alpha=0.45)
            for y in ys:
                ax.plot([x0, x1], [y, y], [0, 0], color="#3f4c6b", lw=0.5, alpha=0.45)
            ax.text(x1 - 0.15, y1 - 0.15, 0.0, "z=0", color="#94a3b8", fontsize=8)

    def _scaled_tangent(self, ux: float, uy: float, dval: float):
        """切线方向 (ux, uy, D)，长度 ∝ |D_u f|。D≈0 时返回 None（几乎看不见箭头）。"""
        if abs(dval) < 0.005:
            return None
        tangent = np.array([ux, uy, dval], dtype=float)
        n = float(np.linalg.norm(tangent))
        if n < 1e-9:
            return None
        length = self.arrow_scale * 2.5 * abs(dval)
        return tangent / n * length

    @staticmethod
    def _arrow3d(ax, origin, vec, color, lw=2.2, alpha=1.0, ratio=0.16):
        o = np.asarray(origin, dtype=float)
        v = np.asarray(vec, dtype=float)
        if np.linalg.norm(v) < 1e-9:
            return
        ax.quiver(
            o[0], o[1], o[2],
            v[0], v[1], v[2],
            color=color,
            linewidth=lw,
            arrow_length_ratio=ratio,
            alpha=alpha,
            normalize=False,
            zorder=30,
        )

    @staticmethod
    def _style_3d(ax, zmin: float, zmax: float, xlim, ylim) -> None:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_zlim(zmin, zmax)
        try:
            ax.set_box_aspect((1.0, 1.0, 0.72))
        except Exception:
            pass
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_zlabel("")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        ax.xaxis.pane.set_facecolor((0.10, 0.10, 0.20, 0.15))
        ax.yaxis.pane.set_facecolor((0.10, 0.10, 0.20, 0.15))
        ax.zaxis.pane.set_facecolor((0.12, 0.12, 0.24, 0.08))
        ax.xaxis.pane.set_edgecolor("#2d2d4a")
        ax.yaxis.pane.set_edgecolor("#2d2d4a")
        ax.zaxis.pane.set_edgecolor("#2d2d4a")
        ax.grid(False)

    # ----- 主绘制 -----
    def _draw(self) -> None:
        st = self._state()
        f, p, u = st["f"], st["p"], st["u"]
        px, py, fp = p
        ux, uy = u
        gx, gy = st["g"]
        scale = self.arrow_scale
        show_all = self._checked("所有方向")
        show_grad = self._checked("最快增长")
        show_neg = self._checked("最快下降")
        show_sec = self._checked("割线近似")
        show_curve = self._checked("截面曲线")

        xs = np.linspace(*self.xlim, self.n_surf)
        ys = np.linspace(*self.ylim, self.n_surf)
        X, Y = np.meshgrid(xs, ys)
        Z = np.asarray(f(X, Y), dtype=float)
        data_min = float(np.min(Z))
        data_max = float(np.max(Z))
        span = max(data_max - data_min, 1.0)
        if data_min >= -1e-9:
            zmin, zmax = 0.0, data_max + 0.08 * span
        else:
            zmin = data_min - 0.08 * span
            zmax = max(data_max, 0.0) + 0.08 * span

        elev, azim = self.ax3d.elev, self.ax3d.azim
        if elev is None:
            elev, azim = self._view

        self.ax3d.cla()
        self.ax2d.cla()
        self.axpolar.cla()
        self._style_3d(self.ax3d, zmin, zmax, self.xlim, self.ylim)
        self.ax3d.view_init(elev=elev, azim=azim)
        self._draw_axes(self.ax3d, zmin, zmax)

        self.ax3d.plot_surface(
            X, Y, Z,
            cmap=SURFACE_CMAP,
            linewidth=0.15,
            antialiased=True,
            alpha=0.38,
            edgecolor="#334155",
            rstride=2,
            cstride=2,
            shade=True,
        )

        # 点 P 的铅垂线：从地面垂到曲面上，帮助看出 z 是高度
        self.ax3d.plot([px, px], [py, py], [0, fp], color=CRIMSON, ls="--", lw=1.0, alpha=0.7)
        self.ax3d.scatter([px], [py], [0], color=CRIMSON, s=22, alpha=0.85, depthshade=False)
        self.ax3d.scatter([px], [py], [fp], color=CRIMSON, s=55, depthshade=False, zorder=40)
        self.ax3d.text(px, py, fp + 0.08 * max(zmax - zmin, 1.0), "P", color=CRIMSON, fontsize=11, fontweight="bold")

        # xy 平面上的当前方向
        self._arrow3d(self.ax3d, (px, py, 0.0), (scale * ux, scale * uy, 0.0), CYAN, lw=2.0, alpha=0.95)

        if show_all:
            segs, colors, widths = [], [], []
            for deg in range(0, 360, 10):
                a = math.radians(deg)
                dux, duy = math.cos(a), math.sin(a)
                dval = gx * dux + gy * duy
                vec = self._scaled_tangent(dux, duy, dval)
                if vec is None:
                    continue
                origin = np.array([px, py, fp])
                segs.append([origin, origin + vec])
                cur = abs((deg - self.s_theta.val) % 360) < 6 or abs((deg - self.s_theta.val) % 360) > 354
                if cur:
                    colors.append(GREEN)
                    widths.append(2.6)
                elif dval >= 0:
                    colors.append((0.29, 0.87, 0.50, 0.55))
                    widths.append(1.6)
                else:
                    colors.append((0.97, 0.44, 0.44, 0.55))
                    widths.append(1.6)
            if segs:
                self.ax3d.add_collection3d(
                    Line3DCollection(segs, colors=colors, linewidths=widths)
                )
            cur_vec = self._scaled_tangent(ux, uy, st["exact"])
            if cur_vec is not None:
                self._arrow3d(self.ax3d, (px, py, fp), cur_vec, GREEN, lw=2.6, ratio=0.14)
            ang = np.linspace(0, 2 * np.pi, 80)
            self.ax3d.plot(
                px + scale * np.cos(ang),
                py + scale * np.sin(ang),
                np.zeros_like(ang),
                color="#60a5fa",
                lw=1.0,
                alpha=0.45,
            )
        else:
            if show_curve:
                ts = np.linspace(-0.25, 2.05, 120)
                cx = px + ts * ux
                cy = py + ts * uy
                cz = np.asarray(f(cx, cy), dtype=float)
                self.ax3d.plot(cx, cy, cz, color="#e2e8f0", lw=1.8, alpha=0.75)

            # 检查点：h 从大到小，箭头逐渐贴近绿切线
            for ch, alpha in ((1.5, 0.12), (1.0, 0.14), (0.7, 0.16), (0.4, 0.18), (0.2, 0.22), (0.1, 0.25)):
                cph = float(f(px + ch * ux, py + ch * uy))
                cslope = (cph - fp) / ch
                origin = np.array([px, py, fp])
                tip = origin + scale * np.array([ux, uy, cslope])
                self.ax3d.plot(*zip(origin, tip), color=ORANGE, lw=1.0, alpha=alpha)

            exact_vec = self._scaled_tangent(ux, uy, st["exact"])
            if exact_vec is not None:
                self._arrow3d(self.ax3d, (px, py, fp), exact_vec, GREEN, lw=2.4)
            if show_sec:
                approx_vec = self._scaled_tangent(ux, uy, st["approx"])
                if approx_vec is not None:
                    self._arrow3d(self.ax3d, (px, py, fp), approx_vec, ORANGE, lw=2.2)
                phx, phy, fph = st["ph"]
                self.ax3d.plot([px, phx], [py, phy], [fp, fph], color=ORANGE, lw=1.8, alpha=0.8)
                self.ax3d.scatter([phx], [phy], [fph], color=ORANGE, s=36, depthshade=False)
                self.ax3d.text(phx, phy, fph + 0.10, "P+hu", color=ORANGE, fontsize=9)

        if show_grad and st["gnorm"] > 1e-10:
            ngx, ngy = gx / st["gnorm"], gy / st["gnorm"]
            gvec = self._scaled_tangent(ngx, ngy, st["gnorm"])
            if gvec is not None:
                self._arrow3d(self.ax3d, (px, py, fp), gvec, GOLD, lw=2.8, ratio=0.12)
                tip = np.array([px, py, fp]) + gvec
                self.ax3d.text(tip[0], tip[1], tip[2] + 0.06, "增长最快", color=GOLD, fontsize=9)
            self._arrow3d(
                self.ax3d,
                (px, py, 0.0),
                (scale * ngx, scale * ngy, 0.0),
                GOLD,
                lw=1.8,
                alpha=0.85,
                ratio=0.14,
            )

        if show_neg and st["gnorm"] > 1e-10:
            ngx, ngy = gx / st["gnorm"], gy / st["gnorm"]
            nvec = self._scaled_tangent(-ngx, -ngy, -st["gnorm"])
            if nvec is not None:
                self._arrow3d(self.ax3d, (px, py, fp), nvec, CRIMSON, lw=2.0, alpha=0.9, ratio=0.12)

        self._draw_xy_view(st, show_all, show_grad, show_neg)
        self._draw_polar(st)
        self._draw_info(st)

        self.fig.canvas.draw_idle()

    def _draw_xy_view(self, st, show_all, show_grad, show_neg) -> None:
        ax = self.ax2d
        f, p, u = st["f"], st["p"], st["u"]
        px, py, _ = p
        ux, uy = u
        gx, gy = st["g"]
        xs = np.linspace(*self.xlim, 80)
        ys = np.linspace(*self.ylim, 80)
        X, Y = np.meshgrid(xs, ys)
        Z = np.asarray(f(X, Y), dtype=float)

        ax.set_facecolor("#16162c")
        ax.contourf(X, Y, Z, levels=14, cmap=SURFACE_CMAP, alpha=0.85)
        ax.contour(X, Y, Z, levels=14, colors="#0f172a", linewidths=0.35, alpha=0.45)
        ax.axhline(0, color="#475569", lw=0.6)
        ax.axvline(0, color="#475569", lw=0.6)

        # 坐标轴刻度（俯视图）
        ax.plot([self.xlim[0], self.xlim[1]], [self.ylim[0], self.ylim[0]], color=AXIS_X, lw=2)
        ax.plot([self.xlim[0], self.xlim[0]], [self.ylim[0], self.ylim[1]], color=AXIS_Y, lw=2)
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.text(self.xlim[1] - 0.05, self.ylim[0] - 0.08, "x", color=AXIS_X, fontsize=11, ha="right", va="top")
        ax.text(self.xlim[0] - 0.08, self.ylim[1] - 0.05, "y", color=AXIS_Y, fontsize=11, ha="right", va="top")
        ax.tick_params(colors=TICK, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color("#334155")

        r = self.arrow_scale
        gnorm = max(st["gnorm"], 1e-9)
        circle = plt.Circle((px, py), r, fill=False, ec="#60a5fa", lw=1.0, alpha=0.7, ls="--")
        ax.add_patch(circle)

        if show_all:
            for deg in range(0, 360, 10):
                a = math.radians(deg)
                dux, duy = math.cos(a), math.sin(a)
                dval = gx * dux + gy * duy
                if abs(dval) < 0.005:
                    continue
                L = r * abs(dval) / gnorm
                col = GREEN if dval >= 0 else CRIMSON
                ax.annotate(
                    "",
                    xy=(px + L * dux, py + L * duy),
                    xytext=(px, py),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.0, alpha=0.55),
                )

        ax.annotate(
            "",
            xy=(px + r * ux, py + r * uy),
            xytext=(px, py),
            arrowprops=dict(arrowstyle="-|>", color=CYAN, lw=2.2),
        )
        ax.text(px + r * ux * 1.08, py + r * uy * 1.08, "u 当前方向", color=CYAN, fontsize=8)

        if show_grad and st["gnorm"] > 1e-10:
            ngx, ngy = gx / st["gnorm"], gy / st["gnorm"]
            ax.annotate(
                "",
                xy=(px + r * ngx, py + r * ngy),
                xytext=(px, py),
                arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=2.4),
            )
            ax.text(px + 1.08 * r * ngx, py + 1.08 * r * ngy, "最快增长", color=GOLD, fontsize=8)
        if show_neg and st["gnorm"] > 1e-10:
            ngx, ngy = gx / st["gnorm"], gy / st["gnorm"]
            ax.annotate(
                "",
                xy=(px - r * ngx, py - r * ngy),
                xytext=(px, py),
                arrowprops=dict(arrowstyle="-|>", color=CRIMSON, lw=1.8),
            )

        ax.plot(px, py, "o", color=CRIMSON, ms=7, zorder=5)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(*self.xlim)
        ax.set_ylim(*self.ylim)
        ax.set_title("俯视图 · 箭头长短 = |方向导数|", color="#cbd5e1", fontsize=11)

    def _draw_polar(self, st) -> None:
        """把每个方向的 D_u f 画成向量端点，整体是过原点、直径沿梯度的圆。"""
        ax = self.axpolar
        ax.set_facecolor("#16162c")
        gx, gy = st["g"]
        gnorm = max(st["gnorm"], 1e-9)
        thetas = np.linspace(0, 2 * np.pi, 361)
        values = gx * np.cos(thetas) + gy * np.sin(thetas)
        xs = values * np.cos(thetas)
        ys = values * np.sin(thetas)

        pos = values >= 0
        ax.plot(xs[pos], ys[pos], color=GREEN, lw=2.4, label="升高 D>0")
        ax.plot(xs[~pos], ys[~pos], color=CRIMSON, lw=2.4, label="下降 D<0")
        ax.fill(xs, ys, color="#4ade80", alpha=0.10)

        lim = gnorm * 1.45
        ax.axhline(0, color="#475569", lw=0.7)
        ax.axvline(0, color="#475569", lw=0.7)
        circ = plt.Circle((0, 0), gnorm, fill=False, ec="#64748b", lw=0.7, ls=":", alpha=0.8)
        ax.add_patch(circ)

        # 角度参考线
        for deg in range(0, 360, 45):
            a = math.radians(deg)
            ax.plot([0, lim * math.cos(a)], [0, lim * math.sin(a)], color="#1e293b", lw=0.6)
            ax.text(1.05 * lim * math.cos(a), 1.05 * lim * math.sin(a), f"{deg}°",
                    color=TICK, fontsize=7, ha="center", va="center")

        same_dir = abs(((st["theta"] - st["gdir"] + math.pi) % (2 * math.pi)) - math.pi) < 0.12
        cx, cy = st["exact"] * math.cos(st["theta"]), st["exact"] * math.sin(st["theta"])
        ax.annotate("", xy=(cx, cy), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0))
        ax.plot(cx, cy, "o", color=ORANGE, ms=7, zorder=5)
        if not same_dir:
            ax.text(cx * 1.12, cy * 1.12, "当前方向", color=ORANGE, fontsize=8)

        if st["gnorm"] > 1e-10:
            mx, my = gx, gy
            ax.annotate("", xy=(mx, my), xytext=(0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=2.2))
            ax.plot(mx, my, "o", color=GOLD, ms=8, zorder=6)
            ax.text(mx * 1.16, my * 1.16,
                    "当前 = 最快增长" if same_dir else "最快增长",
                    color=GOLD, fontsize=8)

        ax.set_aspect("equal", adjustable="box")
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.tick_params(colors=TICK, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color("#334155")
        ax.set_xlabel("D · cos θ", color="#94a3b8", fontsize=8)
        ax.set_ylabel("D · sin θ", color="#94a3b8", fontsize=8)
        ax.set_title("方向导数玫瑰：每个方向的升降快慢（圆的直径 = 梯度）",
                     color="#cbd5e1", fontsize=10, pad=8)
        ax.grid(color="#1e293b", alpha=0.9)

    def _draw_info(self, st) -> None:
        px, py, fp = st["p"]
        ux, uy = st["u"]
        gx, gy = st["g"]
        deg = self.s_theta.val
        gdeg = math.degrees(st["gdir"]) % 360
        err = abs(st["approx"] - st["exact"])
        self.info.set_text(
            f"P = ({px:.2f}, {py:.2f})    f(P) = {fp:.4f}    "
            f"u = (cos {deg:.0f}°, sin {deg:.0f}°) = ({ux:.3f}, {uy:.3f})    "
            f"梯度 grad f(P) = ({gx:.3f}, {gy:.3f})    |grad f| = {st['gnorm']:.4f}（最大方向导数）\n"
            f"精确 D_u f = grad f · u = {st['exact']:+.4f}      "
            f"近似 D* = [f(P+hu)−f(P)]/h = {st['approx']:+.4f}      "
            f"误差 |D*−D| = {err:.4f}      "
            f"增长最快方向 θ = {gdeg:.1f}°      "
            f"当前夹角 φ = {abs(((deg - gdeg + 180) % 360) - 180):.1f}°      "
            f"箭头长度正比于 |D_u f| = {abs(st['exact']):.4f}"
        )

    def _on_change(self, _=None) -> None:
        self._draw()

    def _on_function(self, label: str) -> None:
        self.fn_name = label
        px, py = FUNCTIONS[label]["p0"]
        self.s_px.set_val(px)
        self.s_py.set_val(py)
        self._draw()

    def show(self) -> None:
        plt.show()


def main() -> int:
    if not hasattr(sys, "real_prefix") and sys.prefix == sys.base_prefix:
        venv = _VENV_PYTHON
        if venv.exists() and Path(sys.executable).resolve() != venv.resolve():
            print(f"建议用虚拟环境运行：\n  {venv} {Path(__file__).resolve()}")
    try:
        DirectionalDerivativeDemo().show()
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
