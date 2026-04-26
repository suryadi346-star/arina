#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Typing Animation Effects"""

import sys
import time
from config import ENABLE_TYPING_EFFECT, TYPING_DELAY, IS_TERMUX

class TypingEffect:
    """Handle typing animation with Termux compatibility"""
    
    def __init__(self, delay: float = None, enabled: bool = None):
        self.delay = delay if delay is not None else TYPING_DELAY
        self.enabled = enabled if enabled is not None else ENABLE_TYPING_EFFECT
        
        # Auto-disable on Termux for better UX
        if IS_TERMUX:
            self.enabled = False
    
    def print(self, text: str, end: str = "\n", flush: bool = True):
        """Print text with optional typing effect"""
        if not self.enabled or not sys.stdout.isatty():
            print(text, end=end, flush=flush)
            return
        
        for char in text:
            print(char, end='', flush=flush)
            time.sleep(self.delay)
        print(end, end='', flush=flush)
    
    def print_lines(self, text: str, line_delay: float = 0.1):
        """Print multi-line text with typing effect per line"""
        if not self.enabled or not sys.stdout.isatty():
            print(text)
            return
        
        lines = text.split('\n')
        typer = TypingEffect(enabled=True, delay=self.delay)
        
        for i, line in enumerate(lines):
            typer.print(line, end='')
            if i < len(lines) - 1:
                print()
                time.sleep(line_delay)

# Global instance
typer = TypingEffect()
