#!/usr/bin/env python3
def handle_notes(parts: list, storage):
    if len(parts) < 2:
        print("  Gunakan: catatan simpan <kunci> <isi> | catatan lihat <kunci> | catatan daftar")
        return
    action = parts[1].lower()
    if action == "simpan" and len(parts) >= 4:
        storage.add_note(parts[2], " ".join(parts[3:]))
        print(f"  ✅ Catatan '{parts[2]}' disimpan!")
    elif action == "lihat" and len(parts) >= 3:
        val = storage.get_note(parts[2])
        print(f"  📝 {parts[2]}: {val}" if val else f"  ⚠️  Catatan tidak ditemukan.")
    elif action == "daftar":
        notes = storage.list_notes()
        if notes:
            for k, v in notes.items():
                print(f"    • {k}: {v}")
        else:
            print("  📋 Belum ada catatan.")
    elif action == "hapus" and len(parts) >= 3:
        if storage.delete_note(parts[2]):
            print(f"  🗑️  Catatan dihapus.")
