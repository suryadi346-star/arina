#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Color & Style Helpers"""

from config import ENABLE_COLORS

class Colors:
    """ANSI color codes with fallback"""
    
    # Basic colors
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    GRAY    = '\033[90m'
    
    # Bright colors
    BRIGHT_RED    = '\033[91m'
    BRIGHT_GREEN  = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE   = '\033[94m'
    BRIGHT_CYAN   = '\033[96m'
    
    # Styles
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET   = '\033[0m'
    
    @classmethod
    def wrap(cls, text: str, *styles: str) -> str:
        """Wrap text with styles if colors enabled"""
        if not ENABLE_COLORS:
            return str(text)
        return ''.join(styles) + str(text) + cls.RESET

# Convenience function
def c(text: str, *styles: str) -> str:
    """Apply color/style to text"""
    return Colors.wrap(text, *styles)
