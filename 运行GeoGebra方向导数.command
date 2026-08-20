#!/bin/bash
# 双击运行 GeoGebra 方向导数案例复刻
cd "$(dirname "$0")"
env -u PYTHONHOME -u PYTHONPATH \
  ./venv/bin/python3.14 "geogebra方向导数.py"
