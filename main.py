#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARINA - AI Responsive Intelligent Network Assistant
Main Entry Point
"""

import sys
import signal
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config import VERSION, IS_TERMUX
from arina.core.bot import ArinaBot
from arina.ui.colors import c, Colors
from utils.termux import setup_termux

def handle_sigint(signum, frame):
    """Graceful shutdown handler"""
    print(c("\n\n  👋 Arina ditutup. Sampai jumpa!", Colors.CYAN))
    sys.exit(0)

def main():
    """Main entry point"""
    # Setup signal handlers
    signal.signal(signal.SIGINT, handle_sigint)
    
    # Termux-specific setup
    if IS_TERMUX:
        setup_termux()
    
    # Print startup info
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"ARINA v{VERSION}")
        return
    
    # Run the bot
    try:
        bot = ArinaBot()
        bot.run()
    except Exception as e:
        print(c(f"\n❌ Error: {e}", Colors.RED, Colors.BOLD), file=sys.stderr)
        if "--debug" in sys.argv:
            raise
        sys.exit(1)

if __name__ == "__main__":
    main()
