#!/usr/bin/env python3
from arina.ui.colors import c, Colors
from arina.knowledge.base import KNOWLEDGE

def show_help():
    print(c("""
╔══════════════════════════════════════════════════╗
║         ARINA — Panduan Penggunaan               ║
╠══════════════════════════════════════════════════╣""", Colors.CYAN))
    print(c("║  TOPIK BELAJAR:", Colors.WHITE))
    for k in KNOWLEDGE:
        print(c(f"║  • {k:20} → {KNOWLEDGE[k]['intro'][:30]}...", Colors.GRAY))
    print(c("""║
║  PERINTAH: quiz | hitung | catatan | profil | tips | help | clear | exit
╚══════════════════════════════════════════════════╝
""", Colors.CYAN))
