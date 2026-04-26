#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARINA - Configuration Module
"""
import os
import sys
from pathlib import Path

# ─────────────────────────────────────────
#  VERSION & METADATA
# ─────────────────────────────────────────
VERSION = "2.1.0"
APP_NAME = "ARINA"
DESCRIPTION = "AI Responsive Intelligent Network Assistant"
AUTHOR = "suryadi"

# ─────────────────────────────────────────
#  PATHS
# ─────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = Path(os.getenv("ARINA_DATA", Path.home() / ".arina"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

MEMORY_FILE = DATA_DIR / "memory.json"
CONFIG_FILE = DATA_DIR / "config.json"
LOG_FILE = DATA_DIR / "arina.log"

# ─────────────────────────────────────────
#  TERMUX DETECTION
# ─────────────────────────────────────────
IS_TERMUX = (
    os.getenv("TERMUX_VERSION") is not None or
    os.getenv("PREFIX", "").endswith("termux") or
    Path("/data/data/com.termux").exists()
)

# ─────────────────────────────────────────
#  UI SETTINGS
# ─────────────────────────────────────────
ENABLE_COLORS = not os.getenv("NO_COLOR") and sys.stdout.isatty()
ENABLE_TYPING_EFFECT = not IS_TERMUX  # Disable di Termux untuk performa
TYPING_DELAY = 0.012  # detik per karakter

# ─────────────────────────────────────────
#  MODEL SETTINGS
# ─────────────────────────────────────────
DEFAULT_MODEL = "hybrid"  # rule_based | keyword | fuzzy | hybrid
MODELS_ENABLED = ["rule_based", "keyword", "fuzzy", "hybrid"]

# ─────────────────────────────────────────
#  KNOWLEDGE SETTINGS
# ─────────────────────────────────────────
MAX_RESPONSE_LENGTH = 2000
QUIZ_PASS_THRESHOLD = 70  # persen

# ─────────────────────────────────────────
#  LOGGING
# ─────────────────────────────────────────
LOG_LEVEL = os.getenv("ARINA_LOG", "INFO").upper()

