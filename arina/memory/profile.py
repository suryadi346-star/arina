#!/usr/bin/env python3
from arina.ui.colors import c, Colors

def show_profile(storage):
    stats = storage.get_stats()
    print(c("""
╔══════════════════════════════╗
║         PROFIL KAMU          ║
╠══════════════════════════════╣""", Colors.CYAN))
    print(c(f"║  Nama          : {stats['name']:<13}║", Colors.WHITE))
    print(c(f"║  Bergabung     : {stats['first_seen']:<13}║", Colors.WHITE))
    print(c(f"║  Total obrolan : {stats['conversations']:<13}║", Colors.WHITE))
    print(c(f"║  Quiz dimainkan: {stats['quizzes_taken']:<13}║", Colors.WHITE))
    print(c(f"║  Rata-rata quiz: {stats['average_score']:.1f}%{'':<9}║", Colors.WHITE))
    print(c("╚══════════════════════════════╝\n", Colors.CYAN))
