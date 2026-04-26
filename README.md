# 🤖 ARINA v2.1
> AI Responsive Intelligent Network Assistant
> *Asisten AI Edukatif & Interaktif untuk Teknologi & Pemrograman*

![Version](https://img.shields.io/badge/version-2.1.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![Termux](https://img.shields.io/badge/termux-compatible-brightgreen)

## ✨ Fitur

- 🧠 **Multi-Model AI**: Rule-based, Keyword, Fuzzy, & Hybrid ensemble
- 📚 **Knowledge Base**: Python, Linux, Cybersecurity, Git, ML, Web Dev, Data Structures
- 🎯 **Interactive Quiz**: Uji pemahaman dengan kuis interaktif
- 🧮 **Calculator**: Evaluasi ekspresi matematika dengan aman
- 📝 **Notes System**: Simpan catatan belajar personal
- 💾 **Persistent Memory**: Profil & riwayat tersimpan otomatis
- 📱 **Termux Ready**: Optimasi khusus untuk Android/Termux
- 🎨 **Beautiful UI**: Warna, animasi, dan formatting yang enak dibaca

## 🚀 Instalasi

### Di Komputer (Linux/macOS/Windows WSL)
```bash
git clone https://github.com/suryadi346-star/arina.git
cd arina
pip install -r requirements.txt
python main.py
```
## Di termux (Android)
```bash
# Clone repository
pkg install git python
git clone https://github.com/suryadi346-star/arina.git
cd ~/arina
```
- *Jalankan installer*
`bash install_termux.sh`

# Atau manual:
```bash
pip install -r requirements.txt
python main.py
```
## Shortcut (opsional)

# Tambahkan ke PATH
```bash
echo 'alias arina="python ~/arina/main.py"' >> ~/.bashrc
source ~/.bashrc

# Sekarang cukup ketik:
arina
```
## Penggunaan

📚 Topik Belajar:
  - python      → Belajar Python programming
  - linux       → Perintah & konsep Linux
  - cybersecurity → Dasar keamanan siber
  - git         → Version control dengan Git
  - machine_learning → Pengantar ML
  - webdev      → Web development fundamentals
  - data_structures → Struktur data & algoritma

🔧 Perintah Khusus:
  quiz <topik>    → Mulai kuis interaktif
  hitung <expr>   → Kalkulator (2+2*3)
  catatan simpan <kunci> <isi>  → Simpan catatan
  catatan lihat <kunci>         → Lihat catatan
  profil          → Lihat statistik belajar
  tips            → Tips teknologi random
  help            → Tampilkan panduan ini
  model <nama>    → Ganti model AI (debug)
  clear           → Bersihkan layar
  exit            → Keluar dari ARINA

## Arsitektur Model
```
Response Engine
├── 🎯 Rule-Based (Priority: 100)
│   └── Exact keyword/trigger matching
├── 🔑 Keyword Model (Priority: 50)
│   └── Keyword frequency & overlap scoring
├── 🔍 Fuzzy Model (Priority: 30)
│   └── String similarity matching
└── 🔄 Hybrid Ensemble (Priority: 10)
    └── Combines all models with confidence weighting
```

## Struktur Proyek
```
arina/
├── main.py                # Entry point
├── config.py              # Konfigurasi global
├── requirements.txt       # Dependencies
├── install_termux.sh      # Termux installer
├── arina/
│   ├── core/              # Bot logic & engine
│   ├── ui/                # Colors, banner, prompts
│   ├── knowledge/         # Content & quizzes
│   ├── memory/            # Storage & profile
│   ├── commands/          # Special commands
│   └── models/            # AI response models
└── utils/                 # Helpers & Termux utils
```
## konfigurasi

Edit `config.py` atau gunakan environment
- Variables:
```
# Disable colors
export NO_COLOR=1

# Custom data directory
export ARINA_DATA=~/my-arina-data

# Debug logging
export ARINA_LOG=DEBUG

# Force model selection
# (atau gunakan perintah 'model <nama>' di dalam ARINA)
```

## 🛠️ Development
```
# Install dev dependencies
pip install -r requirements.txt
pip install pytest black flake8  # optional

# Run tests
pytest

# Format code
black .

# Lint
flake8 arina/
```

## 🤝 kontribusi

1. Fork repository
2. Buat feature branch (`git checkout -b feature/amazing`)
3. Commit perubahan (`git commit -m 'feat: add amazing feature'`)
4. Push ke branch (`git push origin feature/amazing`)
5. Buka Pull Request

## 🧾 LICENSE

**MIT License-see [LICENSE](https://github.com/suryadi346-star/arina/blob/e6d17a58fad756e65ca5b8f8bfc8531ffbd9af6c/LICENSE) for details.**

> 💡 "Every expert was once a beginner. Keep learning!"
> ARINA 🤖

 
