#!/usr/bin/env python3
"""General utility functions"""

def truncate(text: str, max_len: int = 100, suffix: str = "...") -> str:
    """Truncate text to max length"""
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix

def safe_input(prompt: str, default: str = None) -> str:
    """Get input with optional default value"""
    try:
        result = input(prompt).strip()
        return result if result else default
    except (EOFError, KeyboardInterrupt):
        print()
        return default
