#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Main Bot Class"""

import sys
import time
from arina.ui.colors import c, Colors
from arina.ui.banner import print_banner, print_box
from arina.core.typer import typer
from arina.core.engine import ResponseEngine
from arina.memory.storage import Storage
from arina.commands.help import show_help
from arina.commands.calculator import handle_calculation
from arina.commands.notes import handle_notes
from arina.knowledge.quizzes import run_quiz
from arina.knowledge.tips import get_random_tip
from arina.memory.profile import show_profile
from config import IS_TERMUX

class ArinaBot:
    """Main ARINA bot controller"""
    
    def __init__(self):
        self.storage = Storage()
        self.engine = ResponseEngine(
            model_name=self.storage.get("preferences.model", "hybrid")
        )
        self.context = {}  # Conversation context
    
    def _get_prompt(self) -> str:
        """Generate input prompt"""
        name = self.storage.get("name") or "Kamu"
        return c(f"\n  {name} › ", Colors.GREEN, Colors.BOLD)
    
    def _print_response(self, text: str):
        """Print bot response with proper formatting"""
        prefix = c("  Arina › ", Colors.CYAN, Colors.BOLD)
        print(f"\n{prefix}")
        for line in text.split("\n"):
            print(f"  {line}")
        print()
    
    def _handle_special_commands(self, text: str) -> bool:
        """Handle special commands, return True if handled"""
        parts = text.strip().split()
        if not parts:
            return False
        
        cmd = parts[0].lower()
        
        # Help
        if cmd in ["help", "bantuan", "?"]:
            show_help()
            return True
        
        # Clear screen
        if cmd in ["clear", "cls"]:
            import os
            os.system("cls" if os.name == "nt" else "clear")
            print_banner()
            return True
        
        # Profile
        if cmd in ["profil", "profile", "stats", "statistik"]:
            show_profile(self.storage)
            return True
        
        # Tips
        if cmd in ["tips", "tip"]:
            self._print_response(get_random_tip())
            return True
        
        # History
        if cmd in ["riwayat", "history", "topik"]:
            topics = self.storage.data.get("topics_learned", [])
            if topics:
                self._print_response("📚 Topik yang sudah dipelajari:\n  " + "\n  ".join(f"• {t}" for t in topics))
            else:
                self._print_response("Kamu belum mempelajari topik apapun. Coba ketik 'python' atau 'linux'! 😊")
            return True
        
        # Quiz
        if cmd == "quiz":
            topic = parts[1].lower() if len(parts) > 1 else ""
            run_quiz(topic, self.storage)
            return True
        
        # Calculator
        if cmd in ["hitung", "kalkulator", "calc"]:
            expr = " ".join(parts[1:])
            result = handle_calculation(expr)
            if result is not None:
                self._print_response(f"🧮 {expr} = {c(str(result), Colors.YELLOW, Colors.BOLD)}")
            else:
                self._print_response("⚠️  Ekspresi tidak valid. Contoh: hitung 2 + 3 * (4 / 2)")
            return True
        
        # Notes
        if cmd in ["catatan", "note", "notes"]:
            handle_notes(parts, self.storage)
            return True
        
        # Model switch (debug)
        if cmd == "model" and len(parts) > 1:
            if self.engine.switch_model(parts[1]):
                self.storage.set("preferences.model", parts[1])
                self._print_response(f"✅ Model diubah ke: {parts[1]}")
            else:
                self._print_response(f"⚠️  Model '{parts[1]}' tidak tersedia. Pilihan: {', '.join(self.engine.MODEL_REGISTRY.keys())}")
            return True
        
        return False
    
    def _process_input(self, user_input: str):
        """Process user input and generate response"""
        if not user_input.strip():
            return
        
        # Handle special commands first
        if self._handle_special_commands(user_input):
            return
        
        # Update conversation count
        self.storage.increment("conversation_count")
        
        # Get response from engine
        response, metadata = self.engine.get_response(user_input, self.context)
        
        if response:
            # Record topic if from knowledge base
            if metadata.get("topic"):
                self.storage.record_topic(metadata["topic"])
            self._print_response(response)
        else:
            # Fallback response
            self._print_response(self.engine.get_fallback_response())
    
    def _greet_user(self):
        """Initial greeting and name setup"""
        print_banner()
        
        name = self.storage.get("name")
        conv_count = self.storage.get("conversation_count", 0)
        
        if name:
            msg = f"Selamat datang kembali, {c(name, Colors.YELLOW, Colors.BOLD)}! "
            if conv_count > 0:
                msg += f"Ini percakapan ke-{conv_count + 1} kita. 😊"
            print(c(f"  {msg}", Colors.WHITE))
        else:
            self._print_response("Halo! Aku ARINA 🤖 Siapa namamu?")
            try:
                nama = input(c("  Kamu › ", Colors.GREEN, Colors.BOLD)).strip()
                if nama:
                    self.storage.set("name", nama)
                    self._print_response(f"Senang kenal, {c(nama, Colors.YELLOW, Colors.BOLD)}! Aku siap menemani belajarmu. 🚀")
            except (KeyboardInterrupt, EOFError):
                pass
        print()
    
    def run(self):
        """Main bot loop"""
        self._greet_user()
        
        while True:
            try:
                prompt = self._get_prompt()
                user_input = input(prompt).strip()
                
                # Exit commands
                if user_input.lower() in ["exit", "quit", "keluar", "bye", "dadah"]:
                    print(c("\n  Sampai jumpa! Semangat belajarnya! 👋✨", Colors.CYAN))
                    time.sleep(0.5)
                    break
                
                self._process_input(user_input)
                
            except KeyboardInterrupt:
                print()
                self._print_response("Sampai jumpa! Semangat belajarnya! 👋✨")
                break
            except EOFError:
                break
            except Exception as e:
                if IS_TERMUX:
                    print(c(f"\n⚠️  Error: {e}\n", Colors.YELLOW))
                else:
                    raise
