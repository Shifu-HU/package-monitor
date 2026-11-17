# -*- coding: utf-8 -*-
"""允许 `python -m package_monitor` 启动程序。"""
from __future__ import annotations

from main import main

if __name__ == "__main__":
    raise SystemExit(main())
