#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Banner & UI Elements"""

from arina.ui.colors import c, Colors
from config import VERSION, APP_NAME, DESCRIPTION, IS_TERMUX

def get_banner() -> str:
    """Generate ASCII banner"""
    art = f"""
  ░█▀█░█▀▄░▀█▀░█▀█░█▀█
  ░█▀█░█▀▄░░█░░█░█░█▀█
  ░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀  v{VERSION}
  {DESCRIPTION}
  {"─" * 45}
"""
    return c(art, Colors.CYAN, Colors.BOLD)

def print_banner():
    """Print the banner"""
    print(get_banner())
    
    if IS_TERMUX:
        print(c("  📱 Mode Termux terdeteksi - beberapa efek dinonaktifkan\n", Colors.GRAY))
    else:
        print(c("  Ketik 'help' untuk panduan atau langsung ajak ngobrol!\n", Colors.GRAY))

def print_separator(char: str = "─", length: int = 45, style=None):
    """Print a separator line"""
    style = style or [Colors.GRAY]
    print(c(char * length, *style))

def print_box(title: str, content: str, color=Colors.CYAN):
    """Print content in a boxed format"""
    width = max(len(title), max(len(line) for line in content.split('\n'))) + 4
    print(c("╔" + "═" * (width-2) + "╗", color))
    print(c(f"║  {title}" + " " * (width - len(title) - 4) + "║", color))
    print(c("╠" + "═" * (width-2) + "╣", color))
    for line in content.split('\n'):
        print(c(f"║  {line}" + " " * (width - len(line) - 4) + "║", Colors.WHITE))
    print(c("╚" + "═" * (width-2) + "╝", color))
