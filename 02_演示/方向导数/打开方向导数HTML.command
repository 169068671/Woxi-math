#!/bin/bash
# 用本地浏览器打开方向导数 HTML，不需要上网
DEMO="$(cd "$(dirname "$0")" && pwd)"
open "$DEMO/方向导数演示.html"
