#!/usr/bin/env python3
import random

ALL_TIPS = [
    "💡 Gunakan 'venv' untuk isolasi project Python: `python -m venv env`",
    "💡 Baca error message dengan teliti — 90% jawaban ada di sana!",
    "💡 Commit kode kamu sering, buat pesan commit yang deskriptif.",
    "💡 Belajar touch typing bisa meningkatkan produktivitas 2x lipat.",
    "💡 DuckDuckGo + 'site:stackoverflow.com' untuk cari solusi spesifik.",
    "💡 'rubber duck debugging': jelaskan masalahmu ke benda mati untuk menemukan solusi.",
]

def get_random_tip() -> str:
    return random.choice(ALL_TIPS)
