#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARINA - AI Responsive Intelligent Network Assistant
Asisten AI Edukatif & Interaktif untuk Teknologi & Pemrograman
Created by: suryadi
"""

import random
import sys
import time
import os
import json
import datetime
import re
import math
from pathlib import Path

# ─────────────────────────────────────────
#  COLOR HELPERS
# ─────────────────────────────────────────
class C:
    CYAN    = '\033[96m'
    BLUE    = '\033[94m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'
    MAGENTA = '\033[95m'
    GRAY    = '\033[90m'
    WHITE   = '\033[97m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    RESET   = '\033[0m'

def c(text, *styles):
    """Apply color/style to text"""
    return ''.join(styles) + str(text) + C.RESET

VERSION   = "2.0"
DATA_FILE = Path.home() / ".arina_memory.json"

# ─────────────────────────────────────────
#  BANNER
# ─────────────────────────────────────────
def print_banner():
    banner = f"""
{c('  ░█▀█░█▀▄░▀█▀░█▀█░█▀█', C.CYAN, C.BOLD)}
{c('  ░█▀█░█▀▄░░█░░█░█░█▀█', C.CYAN, C.BOLD)}
{c('  ░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀', C.CYAN, C.BOLD)}  {c(f'v{VERSION}', C.GRAY)}
  {c('AI Responsive Intelligent Network Assistant', C.GRAY)}
  {c('─────────────────────────────────────────', C.GRAY)}
"""
    print(banner)

# ─────────────────────────────────────────
#  KNOWLEDGE BASE
# ─────────────────────────────────────────
KNOWLEDGE = {
    # ── Python ──────────────────────────────
    "python": {
        "intro": "Python adalah bahasa pemrograman tingkat tinggi yang mudah dipelajari, dinamis, dan serbaguna. 🐍",
        "detail": """
📌 Kenapa Python populer?
  • Sintaks bersih & mudah dibaca
  • Library ekosistem sangat luas (NumPy, Pandas, TensorFlow, Django, dll)
  • Cocok untuk: web, data science, AI/ML, scripting, otomasi

📌 Contoh kode Python sederhana:
  ```python
  # Hello World
  print("Halo, Dunia!")

  # Fungsi dengan type hint
  def tambah(a: int, b: int) -> int:
      return a + b

  # List comprehension
  kuadrat = [x**2 for x in range(10)]
  print(kuadrat)
  ```

📌 Tips belajar Python:
  1. Mulai dari docs.python.org
  2. Latihan di repl.it atau Jupyter Notebook
  3. Buat proyek kecil (kalkulator, to-do list, bot)
""",
        "keywords": ["python", "py", "belajar python", "bahasa python"]
    },

    # ── Linux ────────────────────────────────
    "linux": {
        "intro": "Linux adalah OS open-source yang powerful, digunakan oleh developer, hacker, sysadmin, dan server di seluruh dunia. 🐧",
        "detail": """
📌 Perintah Linux yang wajib diketahui:
  ```bash
  ls -la          # list file dengan detail
  cd /path        # pindah direktori
  pwd             # lihat posisi sekarang
  cp src dst      # copy file
  mv src dst      # pindah/rename file
  rm -rf dir      # hapus folder (hati-hati!)
  grep "teks" f   # cari teks dalam file
  find / -name f  # cari file
  chmod +x file   # buat executable
  sudo apt update # update package (Debian/Ubuntu)
  ps aux          # lihat proses berjalan
  kill -9 PID     # matikan proses
  ssh user@host   # remote ke server
  ```

📌 Distro populer:
  • Ubuntu / Debian  → pemula
  • Arch / Manjaro   → menengah-mahir
  • Kali Linux       → keamanan siber
  • CentOS / RHEL    → server enterprise
""",
        "keywords": ["linux", "ubuntu", "terminal", "bash", "shell", "distro"]
    },

    # ── Keamanan Siber ───────────────────────
    "cybersecurity": {
        "intro": "Keamanan siber (cybersecurity) adalah praktik melindungi sistem, jaringan, dan data dari ancaman digital. 🔐",
        "detail": """
📌 Konsep Dasar Keamanan Siber:
  • CIA Triad: Confidentiality, Integrity, Availability
  • Authentication vs Authorization
  • Enkripsi (symmetric/asymmetric)
  • Firewall & IDS/IPS

📌 Area spesialisasi:
  • Penetration Testing (Ethical Hacking)
  • Digital Forensics
  • Security Operation Center (SOC)
  • Cloud Security
  • Reverse Engineering

📌 Tools populer (legal & edukatif):
  • Nmap       → network scanner
  • Wireshark  → packet analyzer
  • Burp Suite → web security testing
  • Metasploit → pen testing framework
  • OWASP ZAP  → web vulnerability scanner

⚠️  Selalu minta izin sebelum melakukan testing!
    Ethical hacking tanpa izin = ilegal.

📌 Sumber belajar:
  • TryHackMe.com  (pemula)
  • HackTheBox.eu  (menengah-mahir)
  • OWASP.org      (web security)
""",
        "keywords": ["hacking", "hack", "security", "keamanan", "siber", "cyber", "pentest", "ctf", "exploit"]
    },

    # ── Git & GitHub ─────────────────────────
    "git": {
        "intro": "Git adalah sistem version control terdistribusi. GitHub adalah platform hosting untuk repositori Git. 🗂️",
        "detail": """
📌 Perintah Git penting:
  ```bash
  git init                  # buat repo baru
  git clone <url>           # clone repo
  git status                # cek status
  git add .                 # stage semua perubahan
  git commit -m "pesan"     # commit
  git push origin main      # push ke remote
  git pull                  # ambil update
  git branch fitur-baru     # buat branch
  git checkout fitur-baru   # pindah branch
  git merge fitur-baru      # gabung branch
  git log --oneline         # lihat history singkat
  git diff                  # lihat perubahan
  git stash                 # simpan sementara
  git reset --hard HEAD~1   # undo commit terakhir
  ```

📌 Alur kerja tim (GitFlow):
  main → develop → feature → PR/MR → review → merge
""",
        "keywords": ["git", "github", "gitlab", "version control", "repo", "commit", "push", "pull"]
    },

    # ── Machine Learning ─────────────────────
    "machine_learning": {
        "intro": "Machine Learning (ML) adalah cabang AI di mana komputer belajar dari data tanpa diprogram secara eksplisit. 🤖",
        "detail": """
📌 Jenis Machine Learning:
  • Supervised Learning  → data berlabel (klasifikasi, regresi)
  • Unsupervised Learning → data tanpa label (clustering)
  • Reinforcement Learning → belajar dari reward/punishment

📌 Algoritma populer:
  • Linear/Logistic Regression
  • Decision Tree & Random Forest
  • Support Vector Machine (SVM)
  • K-Nearest Neighbors (KNN)
  • Neural Network & Deep Learning

📌 Framework Python untuk ML:
  ```python
  import numpy as np          # komputasi numerik
  import pandas as pd         # manipulasi data
  import matplotlib.pyplot as plt  # visualisasi
  from sklearn.model_selection import train_test_split
  from sklearn.ensemble import RandomForestClassifier

  # Contoh sederhana
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  model = RandomForestClassifier()
  model.fit(X_train, y_train)
  akurasi = model.score(X_test, y_test)
  print(f"Akurasi: {akurasi:.2%}")
  ```

📌 Roadmap belajar ML:
  Math dasar → Python → NumPy/Pandas → Scikit-learn → TF/PyTorch
""",
        "keywords": ["ml", "machine learning", "ai", "deep learning", "neural", "tensorflow", "pytorch", "sklearn"]
    },

    # ── Web Development ──────────────────────
    "webdev": {
        "intro": "Web development adalah proses membangun website dan aplikasi web. Ada frontend (tampilan) dan backend (logika server). 🌐",
        "detail": """
📌 Frontend (yang dilihat user):
  • HTML  → struktur halaman
  • CSS   → styling & layout
  • JS    → interaktivitas
  • Framework: React, Vue, Angular, Svelte

📌 Backend (server & database):
  • Python: Django, FastAPI, Flask
  • JavaScript: Node.js, Express
  • PHP: Laravel
  • Database: MySQL, PostgreSQL, MongoDB, Redis

📌 Contoh API sederhana dengan FastAPI:
  ```python
  from fastapi import FastAPI
  app = FastAPI()

  @app.get("/")
  def root():
      return {"pesan": "Halo dari API!"}

  @app.get("/user/{nama}")
  def get_user(nama: str):
      return {"user": nama, "status": "aktif"}
  ```

📌 Tools penting:
  • VS Code  → editor
  • Postman  → testing API
  • Docker   → containerization
  • Vercel/Netlify → deploy frontend
  • Railway/Render → deploy backend
""",
        "keywords": ["web", "html", "css", "javascript", "js", "react", "vue", "backend", "frontend", "api", "django", "flask", "fastapi"]
    },

    # ── Data Structures ──────────────────────
    "data_structures": {
        "intro": "Struktur data adalah cara menyimpan dan mengorganisir data agar bisa diakses dan dimanipulasi secara efisien. 📊",
        "detail": """
📌 Struktur Data Utama:

  Array/List:
    O(1) akses, O(n) pencarian
    ```python
    arr = [1, 2, 3, 4, 5]
    arr.append(6)    # O(1)
    arr.pop(2)       # O(n)
    ```

  Dictionary/HashMap:
    O(1) rata-rata untuk semua operasi
    ```python
    d = {"nama": "Arina", "versi": 2}
    d["baru"] = "nilai"
    ```

  Stack (LIFO):
    ```python
    stack = []
    stack.append("a")  # push
    stack.pop()        # pop
    ```

  Queue (FIFO):
    ```python
    from collections import deque
    q = deque()
    q.append("a")    # enqueue
    q.popleft()      # dequeue
    ```

  Tree & Graph → untuk hierarki & jaringan

📌 Big O Notation:
  O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
""",
        "keywords": ["struktur data", "data structure", "array", "list", "stack", "queue", "tree", "graph", "linked list", "hash"]
    },
}

# ─────────────────────────────────────────
#  SIMPLE RESPONSES (small talk, general)
# ─────────────────────────────────────────
RESPONSES = {
    "greet": {
        "triggers": ["halo", "hai", "hi", "hello", "hey", "selamat", "assalamualaikum", "waalaikumsalam"],
        "replies": [
            "Halo! 👋 Ada yang bisa Arina bantu hari ini?",
            "Hai! Senang bertemu kamu! Mau belajar apa hari ini? 😊",
            "Hello! Arina siap membantu. Ketik 'help' untuk melihat topik yang tersedia.",
            "Hei! 🌟 Apa yang ingin kamu eksplorasi hari ini?",
        ]
    },
    "how_are_you": {
        "triggers": ["apa kabar", "gimana kabar", "kabarmu", "how are you", "kamu baik"],
        "replies": [
            "Arina baik-baik saja, siap membantu 100%! 🔋 Kamu sendiri gimana?",
            "Alhamdulillah, baik! Semangat bantu kamu belajar. Ada yang mau ditanyakan? 😊",
            "Arina selalu dalam kondisi optimal! 💻 Bagaimana dengan kamu?",
        ]
    },
    "name": {
        "triggers": ["siapa kamu", "nama kamu", "siapa arina", "kamu siapa", "who are you"],
        "replies": [
            "Aku ARINA — AI Responsive Intelligent Network Assistant! 🤖\nDibuat untuk membantu kamu belajar teknologi, coding, dan banyak lagi.",
            "Namaku ARINA, asisten AI yang fokus pada edukasi teknologi. Aku bisa bantu kamu belajar Python, Linux, cybersecurity, web dev, dan masih banyak lagi! 🌐",
        ]
    },
    "thanks": {
        "triggers": ["terima kasih", "makasih", "thanks", "thank you", "thx", "tq"],
        "replies": [
            "Sama-sama! Semangat belajarnya ya! 🚀",
            "No problem! Kalau ada lagi yang mau ditanyakan, Arina selalu di sini. 😊",
            "Tentu! Itu kesenangan Arina. Jangan segan tanya lagi ya! 🌟",
        ]
    },
    "bye": {
        "triggers": ["bye", "dadah", "sampai jumpa", "selamat tinggal", "ciao", "exit", "quit", "keluar"],
        "replies": [
            "Sampai jumpa! Semangat belajarnya! 👋✨",
            "Bye! Jaga kesehatan dan terus coding ya! 💻",
            "Selamat tinggal! Kalau butuh bantuan lagi, Arina selalu siap. 🚀",
        ]
    },
    "creator": {
        "triggers": ["dibuat siapa", "creator", "pembuat", "developer arina", "siapa yang buat"],
        "replies": [
            "Arina dibuat oleh Suryadi! 👨‍💻 Seorang developer yang ingin membuat asisten AI edukatif untuk komunitas teknologi Indonesia.",
        ]
    },
    "joke": {
        "triggers": ["joke", "lucu", "candaan", "bercanda", "ketawa", "humor"],
        "replies": [
            "Kenapa programmer suka pakai kacamata? Karena mereka tidak bisa C# 😂",
            "Ada dua jenis orang di dunia ini: yang bisa mengekstrapolasi dari data yang tidak lengkap 😄",
            "Kenapa Python tidak bisa bermain kartu? Karena dia selalu 'indent'-an! 🐍😄",
            "Debugging itu seperti jadi detektif di film kriminal di mana kamu sekaligus jadi pelakunya. 🕵️",
            "99 bugs in the code, 99 bugs... fix one, compile again... 127 bugs in the code! 😱",
        ]
    },
    "motivasi": {
        "triggers": ["motivasi", "semangat", "encourage", "galau", "bingung", "menyerah", "susah", "sulit", "capek"],
        "replies": [
            "Setiap programmer pernah merasa stuck. Yang membedakan adalah yang terus mencoba! 💪\n\"Every expert was once a beginner.\"",
            "Belajar coding itu seperti lari maraton, bukan sprint. Pelan tapi konsisten itu kunci! 🏃\nKamu pasti bisa!",
            "Error bukan musuh — itu guru terbaik kamu! 📚 Setiap error = pelajaran baru.",
            "\"The only way to do great work is to love what you do.\" - Steve Jobs\nSemangat terus ya! 🔥",
        ]
    },
}

# ─────────────────────────────────────────
#  MATH EVALUATOR
# ─────────────────────────────────────────
def safe_eval_math(expr: str):
    """Evaluate simple math expressions safely"""
    try:
        # Allow only safe math operations
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

# ─────────────────────────────────────────
#  MEMORY / LEARNING SYSTEM
# ─────────────────────────────────────────
class Memory:
    def __init__(self):
        self.data = {
            "name": None,
            "topics_learned": [],
            "conversation_count": 0,
            "notes": {},
            "quiz_scores": [],
            "first_seen": str(datetime.date.today()),
        }
        self.load()

    def load(self):
        if DATA_FILE.exists():
            try:
                with open(DATA_FILE, "r") as f:
                    self.data.update(json.load(f))
            except:
                pass

    def save(self):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except:
            pass

    def record_topic(self, topic: str):
        if topic not in self.data["topics_learned"]:
            self.data["topics_learned"].append(topic)
            self.save()

    def add_note(self, key: str, value: str):
        self.data["notes"][key] = value
        self.save()

    def get_note(self, key: str):
        return self.data["notes"].get(key)

    def increment_conv(self):
        self.data["conversation_count"] += 1
        self.save()

# ─────────────────────────────────────────
#  QUIZ SYSTEM
# ─────────────────────────────────────────
QUIZZES = {
    "python": [
        {"q": "Apa output dari: print(type([]))?", "a": "<class 'list'>", "options": ["<class 'list'>", "<class 'array'>", "<class 'tuple'>", "<class 'dict'>"]},
        {"q": "Manakah yang bukan tipe data Python?", "a": "char", "options": ["int", "str", "char", "float"]},
        {"q": "Apa singkatan dari PEP?", "a": "Python Enhancement Proposal", "options": ["Python Enhancement Proposal", "Python Execution Protocol", "Python External Package", "Python Engine Program"]},
    ],
    "linux": [
        {"q": "Perintah apa yang digunakan untuk melihat isi direktori?", "a": "ls", "options": ["ls", "cd", "pwd", "rm"]},
        {"q": "Apa arti 'chmod 777'?", "a": "Semua user bisa read, write, execute", "options": ["Semua user bisa read, write, execute", "Hanya owner bisa akses", "File menjadi tersembunyi", "File dihapus"]},
        {"q": "Perintah untuk melihat proses yang berjalan?", "a": "ps aux", "options": ["ps aux", "ls -la", "top -all", "proc list"]},
    ],
    "cybersecurity": [
        {"q": "Apa kepanjangan dari CIA dalam keamanan siber?", "a": "Confidentiality, Integrity, Availability", "options": ["Confidentiality, Integrity, Availability", "Control, Identity, Access", "Cyber, Internet, Authentication", "Code, Inspect, Authorize"]},
        {"q": "Apa itu SQL Injection?", "a": "Serangan memasukkan kode SQL berbahaya ke input", "options": ["Serangan memasukkan kode SQL berbahaya ke input", "Jenis enkripsi database", "Tool backup database", "Framework query builder"]},
        {"q": "Protokol apa yang digunakan untuk koneksi terenkripsi ke server?", "a": "SSH", "options": ["SSH", "FTP", "HTTP", "SMTP"]},
    ],
}

def run_quiz(topic: str, memory: Memory):
    """Run an interactive quiz"""
    questions = QUIZZES.get(topic)
    if not questions:
        print(c(f"\n[!] Quiz untuk topik '{topic}' belum tersedia.", C.YELLOW))
        print(c(f"    Tersedia: {', '.join(QUIZZES.keys())}", C.GRAY))
        return

    print(c(f"\n╔══ QUIZ: {topic.upper()} ══╗", C.CYAN, C.BOLD))
    print(c("  Jawab dengan nomor pilihan\n", C.GRAY))

    score = 0
    for i, item in enumerate(questions, 1):
        print(c(f"  Q{i}: {item['q']}", C.WHITE, C.BOLD))
        for j, opt in enumerate(item["options"], 1):
            print(f"    {c(str(j), C.CYAN)}. {opt}")

        try:
            ans_input = input(c("  Jawaban kamu: ", C.GREEN)).strip()
            idx = int(ans_input) - 1
            chosen = item["options"][idx]
            if chosen == item["a"]:
                print(c("  ✅ Benar!\n", C.GREEN))
                score += 1
            else:
                print(c(f"  ❌ Salah. Jawaban: {item['a']}\n", C.RED))
        except:
            print(c("  ⚠️  Input tidak valid, dilewati.\n", C.YELLOW))

    pct = (score / len(questions)) * 100
    memory.data["quiz_scores"].append({"topic": topic, "score": pct, "date": str(datetime.date.today())})
    memory.save()

    print(c(f"╚══ Skor kamu: {score}/{len(questions)} ({pct:.0f}%) ══╝", C.CYAN, C.BOLD))
    if pct >= 80:
        print(c("  🏆 Excellent! Kamu menguasai topik ini!", C.GREEN, C.BOLD))
    elif pct >= 50:
        print(c("  📚 Lumayan! Ayo pelajari lagi untuk hasil lebih baik.", C.YELLOW))
    else:
        print(c("  💪 Jangan menyerah! Baca materi dan coba lagi.", C.RED))
    print()

# ─────────────────────────────────────────
#  COMMAND HELP
# ─────────────────────────────────────────
def show_help():
    topics = ", ".join(KNOWLEDGE.keys())
    quiz_t = ", ".join(QUIZZES.keys())
    print(c("""
╔══════════════════════════════════════════════════╗
║         ARINA — Panduan Penggunaan               ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  TOPIK BELAJAR (ketik nama topiknya):            ║""", C.CYAN))
    for k in KNOWLEDGE:
        kw = KNOWLEDGE[k]
        print(c(f"║  • {k:<20} → {kw['intro'][:28]}...", C.WHITE) if len(kw['intro']) > 28 else c(f"║  • {k}", C.WHITE))

    print(c(f"""║                                                  ║
║  PERINTAH KHUSUS:                                ║
║  quiz <topik>      → mulai kuis interaktif       ║
║  hitung <expr>     → kalkulator (misal: 2+2*3)  ║
║  catatan <simpan/lihat/hapus>                    ║
║  riwayat           → topik yang sudah dipelajari ║
║  profil            → lihat profil & statistikmu  ║
║  tips              → tips belajar random         ║
║  help / bantuan    → tampilkan panduan ini       ║
║  clear             → bersihkan layar             ║
║  exit / quit       → keluar dari ARINA           ║
║                                                  ║
║  QUIZ TERSEDIA: {quiz_t:<34}║
╚══════════════════════════════════════════════════╝
""", C.CYAN))

# ─────────────────────────────────────────
#  TIPS SYSTEM
# ─────────────────────────────────────────
ALL_TIPS = [
    "💡 Gunakan 'venv' untuk isolasi project Python: `python -m venv env`",
    "💡 Baca error message dengan teliti — 90% jawaban ada di sana!",
    "💡 Commit kode kamu sering, buat pesan commit yang deskriptif.",
    "💡 Belajar touch typing bisa meningkatkan produktivitas 2x lipat.",
    "💡 Gunakan .gitignore agar file sensitif tidak ter-commit.",
    "💡 DuckDuckGo + 'site:stackoverflow.com' untuk cari solusi spesifik.",
    "💡 Tulis kode yang bisa dibaca manusia, bukan hanya mesin.",
    "💡 Backup data secara rutin! 3-2-1: 3 copy, 2 media, 1 offsite.",
    "💡 Gunakan password manager dan aktifkan 2FA di semua akun penting.",
    "💡 Belajar regex — sangat berguna untuk manipulasi teks.",
    "💡 Dokumentasikan kode kamu sekarang, bukan nanti.",
    "💡 Tidur cukup. Otak memproses informasi saat tidur — penting untuk belajar!",
    "💡 Bergabung komunitas (Discord, Telegram, Reddit) untuk belajar lebih cepat.",
    "💡 'rubber duck debugging': jelaskan masalahmu ke benda mati untuk menemukan solusi.",
    "💡 Test driven development (TDD) — tulis test sebelum kode.",
]

# ─────────────────────────────────────────
#  NOTE COMMANDS
# ─────────────────────────────────────────
def handle_notes(parts: list, memory: Memory):
    if len(parts) < 2:
        print(c("  Gunakan: catatan simpan <kunci> <isi> | catatan lihat <kunci> | catatan daftar", C.YELLOW))
        return

    action = parts[1].lower()
    if action == "simpan" and len(parts) >= 4:
        key = parts[2]
        val = " ".join(parts[3:])
        memory.add_note(key, val)
        print(c(f"  ✅ Catatan '{key}' disimpan!", C.GREEN))
    elif action == "lihat" and len(parts) >= 3:
        key = parts[2]
        val = memory.get_note(key)
        if val:
            print(c(f"  📝 {key}: {val}", C.WHITE))
        else:
            print(c(f"  ⚠️  Catatan '{key}' tidak ditemukan.", C.YELLOW))
    elif action == "daftar":
        notes = memory.data["notes"]
        if notes:
            print(c("  📋 Catatan kamu:", C.CYAN))
            for k, v in notes.items():
                print(f"    {c(k, C.GREEN)}: {v}")
        else:
            print(c("  📋 Belum ada catatan tersimpan.", C.GRAY))
    elif action == "hapus" and len(parts) >= 3:
        key = parts[2]
        if key in memory.data["notes"]:
            del memory.data["notes"][key]
            memory.save()
            print(c(f"  🗑️  Catatan '{key}' dihapus.", C.GREEN))
        else:
            print(c(f"  ⚠️  Catatan '{key}' tidak ditemukan.", C.YELLOW))
    else:
        print(c("  Gunakan: catatan simpan <kunci> <isi> | catatan lihat <kunci> | catatan daftar | catatan hapus <kunci>", C.YELLOW))

# ─────────────────────────────────────────
#  PROFIL
# ─────────────────────────────────────────
def show_profile(memory: Memory):
    name = memory.data.get("name") or "Anonim"
    topics = memory.data["topics_learned"] or ["-"]
    conv   = memory.data["conversation_count"]
    first  = memory.data.get("first_seen", "?")
    scores = memory.data.get("quiz_scores", [])
    avg_score = sum(s["score"] for s in scores) / len(scores) if scores else 0

    print(c("""
╔══════════════════════════════╗
║         PROFIL KAMU          ║
╠══════════════════════════════╣""", C.CYAN))
    print(c(f"║  Nama          : {name:<13}║", C.WHITE))
    print(c(f"║  Bergabung     : {first:<13}║", C.WHITE))
    print(c(f"║  Total obrolan : {conv:<13}║", C.WHITE))
    print(c(f"║  Quiz dimainkan: {len(scores):<13}║", C.WHITE))
    print(c(f"║  Rata-rata quiz: {avg_score:.1f}%{'':<9}║", C.WHITE))
    print(c(f"║  Topik dipelajari:           ║", C.WHITE))
    for t in topics:
        print(c(f"║    • {t:<26}║", C.GREEN))
    print(c("╚══════════════════════════════╝\n", C.CYAN))

# ─────────────────────────────────────────
#  MAIN RESPONSE ENGINE
# ─────────────────────────────────────────
def find_response(user_input: str, memory: Memory) -> str | None:
    text = user_input.lower().strip()

    # ── Smalltalk ─────────────────────────────
    for key, data in RESPONSES.items():
        if any(t in text for t in data["triggers"]):
            if key == "bye":
                print(c("\n  " + random.choice(data["replies"]), C.CYAN))
                time.sleep(0.8)
                sys.exit(0)
            return random.choice(data["replies"])

    # ── Knowledge topics ─────────────────────
    for topic, data in KNOWLEDGE.items():
        if any(kw in text for kw in data["keywords"]):
            memory.record_topic(topic)
            detail = data.get("detail", "")
            return data["intro"] + ("\n" + detail if detail else "")

    return None

# ─────────────────────────────────────────
#  ARINA MAIN CLASS
# ─────────────────────────────────────────
class Arina:
    def __init__(self):
        self.memory = Memory()

    def typing_effect(self, text: str, delay: float = 0.012):
        """Print text with typing animation"""
        for ch in text:
            print(ch, end='', flush=True)
            time.sleep(delay)
        print()

    def arina_print(self, text: str):
        prefix = c("  Arina › ", C.CYAN, C.BOLD)
        print(f"\n{prefix}")
        for line in text.split("\n"):
            print(f"  {line}")
        print()

    def greet(self):
        print_banner()
        print(c("  Ketik 'help' untuk melihat panduan atau langsung ajak ngobrol!\n", C.GRAY))

        # Personalized greeting
        name = self.memory.data.get("name")
        conv = self.memory.data["conversation_count"]
        if name:
            msg = f"Selamat datang kembali, {c(name, C.YELLOW, C.BOLD)}! "
            if conv > 0:
                msg += f"Ini percakapan ke-{conv+1} kita. 😊"
            print(c(f"  {msg}", C.WHITE))
            print()
        else:
            self.arina_print("Halo! Aku ARINA 🤖 Siapa namamu?")
            try:
                nama = input(c("  Kamu › ", C.GREEN, C.BOLD)).strip()
                if nama:
                    self.memory.data["name"] = nama
                    self.memory.save()
                    self.arina_print(f"Senang kenal, {c(nama, C.YELLOW, C.BOLD)}! Aku siap menemani belajarmu. 🚀")
            except (KeyboardInterrupt, EOFError):
                pass

    def process(self, user_input: str):
        text = user_input.strip()
        if not text:
            return

        lower = text.lower()
        parts = text.split()

        self.memory.increment_conv()

        # ── Special Commands ──────────────────

        if lower in ["help", "bantuan", "?"]:
            show_help()
            return

        if lower in ["clear", "cls"]:
            os.system("cls" if os.name == "nt" else "clear")
            print_banner()
            return

        if lower in ["riwayat", "history", "topik"]:
            topics = self.memory.data["topics_learned"]
            if topics:
                self.arina_print("📚 Topik yang sudah kamu pelajari:\n  " + "\n  ".join(f"• {t}" for t in topics))
            else:
                self.arina_print("Kamu belum mempelajari topik apapun. Coba ketik 'python' atau 'linux'! 😊")
            return

        if lower in ["profil", "profile", "statistik", "stats"]:
            show_profile(self.memory)
            return

        if lower in ["tips", "tip"]:
            self.arina_print(random.choice(ALL_TIPS))
            return

        # Quiz command: "quiz python" / "quiz linux"
        if parts[0].lower() == "quiz":
            topic = parts[1].lower() if len(parts) > 1 else ""
            run_quiz(topic, self.memory)
            return

        # Calculator: "hitung 2 + 2 * 3"
        if parts[0].lower() in ["hitung", "kalkulator", "calc", "kalkulasi"]:
            expr = " ".join(parts[1:])
            result = safe_eval_math(expr)
            if result is not None:
                self.arina_print(f"🧮 {expr} = {c(str(result), C.YELLOW, C.BOLD)}")
            else:
                self.arina_print("⚠️  Ekspresi tidak valid. Contoh: hitung 2 + 3 * (4 / 2)")
            return

        # Notes: "catatan ..."
        if parts[0].lower() in ["catatan", "note", "notes"]:
            handle_notes(parts, self.memory)
            return

        # ── Inline math detection ─────────────
        math_match = re.search(r'\b(\d[\d\s\+\-\*\/\(\)\.%]+\d)\b', text)
        if math_match and any(op in text for op in ['+', '-', '*', '/']):
            result = safe_eval_math(math_match.group(1))
            if result is not None:
                self.arina_print(f"🧮 {math_match.group(1)} = {c(str(result), C.YELLOW, C.BOLD)}")
                return

        # ── Knowledge & Smalltalk ─────────────
        response = find_response(text, self.memory)
        if response:
            self.arina_print(response)
            return

        # ── Fallback ──────────────────────────
        fallbacks = [
            f"Hmm, Arina belum tahu tentang itu. 🤔 Coba ketik 'help' untuk melihat topik yang tersedia!",
            f"Menarik! Tapi Arina masih belajar tentang hal itu. Coba tanya tentang Python, Linux, cybersecurity, atau web dev! 😊",
            f"Arina belum bisa jawab itu. Ketik 'tips' untuk tips teknologi, atau 'quiz python' untuk kuis! 🎯",
        ]
        self.arina_print(random.choice(fallbacks))

    def run(self):
        self.greet()

        while True:
            try:
                name = self.memory.data.get("name") or "Kamu"
                prompt = c(f"\n  {name} › ", C.GREEN, C.BOLD)
                user_input = input(prompt).strip()
                self.process(user_input)
            except KeyboardInterrupt:
                print()
                self.arina_print("Sampai jumpa! Semangat belajarnya! 👋✨")
                break
            except EOFError:
                break

# ─────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────
if __name__ == "__main__":
    bot = Arina()
    bot.run()
