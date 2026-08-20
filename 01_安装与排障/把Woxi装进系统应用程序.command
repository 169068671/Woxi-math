#!/bin/zsh
# 把已经装在用户目录的 Woxi Studio 复制到 /Applications
# 用法：在 Finder 里双击本文件，弹出密码框时输入开机密码。

set -euo pipefail

SRC="${HOME}/Applications/Woxi Studio.app"
DEST="/Applications/Woxi Studio.app"
CLI="${HOME}/.local/bin/woxi"

echo
echo "======== Woxi → 系统应用程序 ========"
echo "来源：${SRC}"
echo "目标：${DEST}"
echo

if [[ ! -d "${SRC}" ]]; then
  echo "找不到来源应用："
  echo "  ${SRC}"
  echo "请确认用户「应用程序」文件夹里还有 Woxi Studio.app。"
  echo
  read -r "?按回车关闭"
  exit 1
fi

if [[ ! -x "${CLI}" ]]; then
  echo "提示：命令行 woxi 不在 ${CLI}，本次只处理 Studio 应用。"
  echo
fi

echo "接下来会弹出系统密码框，输入开机密码即可。"
echo

osascript <<EOF
do shell script "/bin/rm -rf '/Applications/Woxi Studio.app'; /bin/cp -R '${SRC}' '/Applications/Woxi Studio.app'; /usr/sbin/chown -R $(id -u):$(id -g) '/Applications/Woxi Studio.app'; /usr/bin/xattr -dr com.apple.quarantine '/Applications/Woxi Studio.app'; /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -f '/Applications/Woxi Studio.app'" with administrator privileges
EOF

echo
if [[ -d "${DEST}" ]]; then
  echo "完成：Woxi Studio 已在 /Applications"
  echo "命令行仍在：${CLI}"
  echo
  echo "可用：Spotlight 搜 Woxi Studio，或打开「应用程序」。"
else
  echo "复制后未找到 ${DEST}，请再试一次。"
  echo
  read -r "?按回车关闭"
  exit 1
fi

echo
read -r "?按回车关闭"
