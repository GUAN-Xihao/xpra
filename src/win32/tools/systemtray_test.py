#!/usr/bin/env python3
# This file is part of Xpra.
# Copyright (C) 2024 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import sys


def main():
    # pylint: disable=import-outside-toplevel
    from xpra.platform import program_context
    with program_context("SystemTray-Test", "SystemTray Test"):
        from xpra.client.gtk_base.example import tray
        return tray.main()


if __name__ == "__main__":
    v = main()
    sys.exit(v)