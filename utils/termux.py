#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Termux Compatibility Utilities"""

import os
import sys
from config import IS_TERMUX

def setup_termux():
    """Apply Termux-specific configurations"""
    if not IS_TERMUX:
        return
    
    # Ensure proper encoding
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    
    # Adjust for Termux's limited terminal capabilities
    if "TERM" in os.environ and os.environ["TERM"] in ["xterm", "linux"]:
        # Force basic terminal mode
        os.environ["TERM"] = "vt100"
    
    # Disable colors if TERMUX environment variable suggests issues
    if os.getenv("TERMUX_NO_COLOR"):
        os.environ["NO_COLOR"] = "1"
    
    # Set a reasonable COLUMNS value if not set
    if not os.getenv("COLUMNS"):
        os.environ["COLUMNS"] = "80"

def is_termux_pro() -> bool:
    """Check if running in Termux Pro (with more features)"""
    return IS_TERMUX and os.path.exists("/data/data/com.termux/files/home/.termux")

def get_termux_storage_path() -> str:
    """Get the appropriate storage path for Termux"""
    if IS_TERMUX:
        # Prefer external storage if available
        external = Path("/sdcard/Arina")
        if external.exists() or external.mkdir(parents=True, exist_ok=True):
            return str(external)
    return str(Path.home() / ".arina")

def notify_termux(message: str, title: str = "ARINA"):
    """Send a Termux notification (if termux-api installed)"""
    if not IS_TERMUX:
        return
    try:
        import subprocess
        subprocess.run(
            ["termux-notification", "-t", title, "-c", message],
            capture_output=True, timeout=1
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass  # termux-api not installed or failed
