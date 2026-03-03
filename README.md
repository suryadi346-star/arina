# arina
# ARINA — AI Responsive Intelligent Network Assistant

```
  ░█▀█░█▀▄░▀█▀░█▀█░█▀█
  ░█▀█░█▀▄░░█░░█░█░█▀█
  ░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀  v2.0
  AI Responsive Intelligent Network Assistant
```

> Asisten AI berbasis terminal yang interaktif, edukatif, dan personal — dirancang untuk menemani perjalanan belajar teknologimu.

**Dibuat oleh:** Suryadi  
**Versi:** 2.0  
**Bahasa:** Python 3.10+  
**Platform:** Linux · macOS · Windows (Terminal)

---

## Daftar Isi

- [Tentang ARINA](#tentang-arina)
- [Fitur Utama](#fitur-utama)
- [Instalasi & Menjalankan](#instalasi--menjalankan)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Topik yang Tersedia](#topik-yang-tersedia)
- [Perintah Lengkap](#perintah-lengkap)
- [Sistem Memori](#sistem-memori)
- [Struktur Proyek](#struktur-proyek)
- [Pengembangan Lanjutan](#pengembangan-lanjutan)
- [Lisensi](#lisensi)

---

## Tentang ARINA

ARINA adalah chatbot terminal berbasis Python yang dirancang untuk menjadi teman belajar teknologi. Berbeda dari chatbot biasa, ARINA:

- **Mengingat siapa kamu** — nama, topik yang sudah dipelajari, dan riwayat percakapan tersimpan secara lokal.
- **Mengajarkan, bukan sekadar menjawab** — setiap topik disertai penjelasan mendalam, contoh kode, dan sumber belajar.
- **Interaktif** — ada sistem kuis, kalkulator, catatan pribadi, tips harian, dan obrolan santai.
- **Tanpa dependensi eksternal** — hanya menggunakan library bawaan Python (stdlib).

---

## Fitur Utama

### 🎨 Tampilan Terminal yang Bersih
Banner ASCII art berwarna, output terstruktur dengan warna ANSI, dan prompt personal sesuai nama kamu.

### 🧠 Knowledge Base Terstruktur
Tujuh topik teknologi dengan penjelasan intro, detail, dan contoh kode nyata yang bisa langsung dicoba.

### 💬 Percakapan Natural
ARINA mengenali berbagai pola kalimat — sapaan, pertanyaan, motivasi, candaan — dan merespons dengan hangat.

### 🎯 Kuis Interaktif
Uji pemahamanmu dengan kuis multiple-choice. Skor tersimpan dan kamu bisa melihat rata-rata nilaimu dari waktu ke waktu.

### 🧮 Kalkulator Bawaan
Evaluasi ekspresi matematika langsung dari chat — termasuk deteksi otomatis jika kamu menuliskan ekspresi di tengah kalimat.

### 📝 Sistem Catatan Pribadi
Simpan, lihat, dan hapus catatan penting langsung dari percakapan. Catatan tersimpan secara persisten di file lokal.

### 💾 Memori Persisten
Semua data pengguna disimpan di `~/.arina_memory.json` — ARINA mengingat kamu bahkan setelah terminal ditutup.

### 💡 Tips Teknologi Harian
Lebih dari 15 tips praktis tentang coding, keamanan, produktivitas, dan workflow developer yang ditampilkan secara acak.

---

## Instalasi & Menjalankan

### Prasyarat

- Python **3.10** atau lebih baru
- Terminal yang mendukung warna ANSI (Linux/macOS Terminal, Windows Terminal)

### Langkah Instalasi

```bash
# 1. Clone atau unduh file
git clone https://github.com/suryadi346-star/arina.git
cd arina

# atau jika hanya punya file tunggal:
# letakkan arina.py di folder mana saja

# 2. Pastikan Python 3.10+ tersedia
python3 --version

# 3. Jalankan langsung (tidak perlu install library tambahan)
python3 arina.py
```

### Windows

```cmd
python arina.py
```

> **Catatan Windows:** Aktifkan "Virtual Terminal Processing" agar warna ANSI tampil dengan benar, atau gunakan Windows Terminal / PowerShell 7+.

---

## Panduan Penggunaan

Saat pertama kali dijalankan, ARINA akan meminta namamu. Setelah itu, cukup ketik pesan seperti bicara biasa.

```
  ░█▀█░█▀▄░▀█▀░█▀█░█▀█
  ...

  Halo! Aku ARINA 🤖 Siapa namamu?

  Kamu › Budi

  Arina ›
  Senang kenal, Budi! Aku siap menemani belajarmu. 🚀

  Budi › python
  Budi › quiz python
  Budi › hitung 15 * 4 + (100 / 5)
  Budi › catatan simpan deadline besok pukul 9 malam
  Budi › tips
  Budi › profil
```

---

## Topik yang Tersedia

Cukup ketik nama topik (atau kalimat yang mengandungnya) untuk mulai belajar.

| Topik | Kata Kunci | Isi |
|---|---|---|
| `python` | python, py, belajar python | Sintaks, contoh kode, tips belajar |
| `linux` | linux, ubuntu, terminal, bash, shell | Perintah dasar, distro, tips |
| `cybersecurity` | hack, security, keamanan, pentest, ctf | CIA triad, tools, sumber belajar etis |
| `git` | git, github, gitlab, commit, push | Perintah penting, GitFlow workflow |
| `machine_learning` | ml, ai, deep learning, tensorflow | Jenis ML, algoritma, framework Python |
| `webdev` | web, html, css, react, django, api | Frontend vs backend, tools, contoh API |
| `data_structures` | struktur data, array, stack, queue, tree | Kompleksitas, implementasi Python |

---

## Perintah Lengkap

### Obrolan & Umum

| Perintah | Deskripsi |
|---|---|
| `halo` / `hai` / `hello` | Sapa ARINA |
| `siapa kamu` | Kenalan dengan ARINA |
| `apa kabar` | Tanya kabar ARINA |
| `joke` / `lucu` | Minta candaan programmer |
| `motivasi` / `semangat` | Dapat kata-kata penyemangat |
| `bye` / `exit` / `quit` | Keluar dari ARINA |

### Belajar & Kuis

| Perintah | Deskripsi |
|---|---|
| `python` | Materi tentang Python |
| `linux` | Materi tentang Linux |
| `cybersecurity` | Materi keamanan siber |
| `git` | Materi Git & GitHub |
| `machine_learning` | Materi ML & AI |
| `webdev` | Materi web development |
| `data_structures` | Materi struktur data |
| `quiz <topik>` | Mulai kuis. Contoh: `quiz python` |
| `riwayat` | Lihat topik yang sudah dipelajari |
| `tips` | Tampilkan tips teknologi acak |

### Alat Bantu

| Perintah | Deskripsi | Contoh |
|---|---|---|
| `hitung <expr>` | Kalkulator | `hitung 2 + 3 * (10 / 2)` |
| `catatan simpan <kunci> <isi>` | Simpan catatan | `catatan simpan api https://myapi.com` |
| `catatan lihat <kunci>` | Lihat catatan | `catatan lihat api` |
| `catatan daftar` | Lihat semua catatan | `catatan daftar` |
| `catatan hapus <kunci>` | Hapus catatan | `catatan hapus api` |

### Navigasi & Info

| Perintah | Deskripsi |
|---|---|
| `help` / `bantuan` / `?` | Tampilkan panduan |
| `profil` / `statistik` | Lihat profil & statistik belajar |
| `clear` / `cls` | Bersihkan layar |

---

## Sistem Memori

ARINA menyimpan data pengguna secara lokal di:

```
~/.arina_memory.json
```

Data yang tersimpan:

```json
{
  "name": "Budi",
  "topics_learned": ["python", "linux", "git"],
  "conversation_count": 42,
  "notes": {
    "api": "https://myapi.com",
    "deadline": "besok pukul 9 malam"
  },
  "quiz_scores": [
    { "topic": "python", "score": 100.0, "date": "2025-02-19" }
  ],
  "first_seen": "2025-02-01"
}
```

Untuk mereset semua data (mulai dari awal):

```bash
rm ~/.arina_memory.json
```

---

## Struktur Proyek

```
arina/
├── arina.py          # File utama — semua logika ada di sini
├── README.md         # Dokumentasi ini
└── ~/.arina_memory.json  # Data pengguna (dibuat otomatis)
```

ARINA dirancang sebagai single-file project agar mudah dibagikan, dijalankan, dan dimodifikasi tanpa setup yang rumit.

---

## Pengembangan Lanjutan

Ingin berkontribusi atau mengembangkan ARINA? Berikut beberapa ide pengembangan:

**Menambah Topik Baru**  
Tambahkan entri baru ke dictionary `KNOWLEDGE` di dalam `arina.py` dengan format yang sama — `intro`, `detail`, dan `keywords`.

**Menambah Pertanyaan Kuis**  
Tambahkan item baru ke dictionary `QUIZZES` dengan struktur `{"q": ..., "a": ..., "options": [...]}`.

**Menambah Respons Smalltalk**  
Tambahkan entri baru ke dictionary `RESPONSES` dengan `triggers` (kata pemicu) dan `replies` (daftar balasan acak).

**Menambah Tips**  
Tambahkan string baru ke list `ALL_TIPS`.

**Integrasi API**  
Karena ARINA hanya menggunakan stdlib, integrasi LLM API seperti OpenAI atau Anthropic bisa ditambahkan sebagai fallback response untuk pertanyaan di luar knowledge base.

---

## Lisensi

Proyek ini bersifat open untuk dipelajari dan dikembangkan. Jika kamu memodifikasi atau mendistribusikan ulang, cantumkan kredit kepada pembuat aslinya.

---

<div align="center">

Dibuat dengan ❤️ oleh **Suryadi**

*"Every expert was once a beginner."*

</div>

<div align="center">
  
[⬆ Kembali ke atas](#️-arina)

</div>
