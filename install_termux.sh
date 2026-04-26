#!/data/data/com.termux/files/usr/bin/bash
# ARINA - Termux Installation Script
# Usage: bash install_termux.sh

set -e

echo "🔧 Installing ARINA for Termux..."

# Update packages
pkg update -y

# Install Python and dependencies
pkg install -y python git clang libffi openssl

# Create project directory
mkdir -p ~/arina
cd ~/arina

# Clone or copy files (assuming files are in current directory)
if [ -d ".git" ]; then
    echo "📦 Using existing repository..."
else
    echo "⚠️  Please ensure all ARINA files are in ~/arina directory"
fi

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt 2>/dev/null || echo "⚠️  Some optional dependencies skipped"

# Make main script executable
chmod +x main.py

# Create launcher script
cat > ~/arina.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/arina
python main.py "$@"
EOF
chmod +x ~/arina.sh

echo ""
echo "✅ ARINA installed successfully!"
echo ""
echo "🚀 Cara menjalankan:"
echo "   ~/arina.sh              # Jalankan ARINA"
echo "   ~/arina.sh --help      # Lihat opsi"
echo ""
echo "💡 Tips Termux:"
echo "   • Tekan Volume+Q untuk exit"
echo "   • Gunakan 'pkg install termux-api' untuk notifikasi"
echo "   • Backup data di ~/.arina/memory.json"
echo ""
echo "🎉 Selamat belajar dengan ARINA! 🤖"
