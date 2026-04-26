#!/usr/bin/env python3
import re
import math

def safe_eval_math(expr: str):
    """Evaluate simple math expressions safely"""
    try:
        allowed = re.sub(r'[^0-9+\-*/(). %]', '', expr)
        if not allowed.strip():
            return None
        result = eval(allowed, {"__builtins__": {}}, {
            "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "abs": abs, "round": round, "pow": pow, "log": math.log,
        })
        return result
    except:
        return None

def handle_calculation(expr: str):
    return safe_eval_math(expr)
