#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Persistent Storage Handler"""

import json
import datetime
from pathlib import Path
from config import MEMORY_FILE

class Storage:
    """JSON-based persistent storage with auto-save"""
    
    DEFAULT_DATA = {
        "name": None,
        "topics_learned": [],
        "conversation_count": 0,
        "notes": {},
        "quiz_scores": [],
        "first_seen": None,
        "last_seen": None,
        "preferences": {
            "model": "hybrid",
            "typing_effect": True,
            "colors": True,
        }
    }
    
    def __init__(self, filepath: Path = None):
        self.filepath = filepath or MEMORY_FILE
        self.data = self.DEFAULT_DATA.copy()
        self._load()
    
    def _load(self):
        """Load data from file"""
        if self.filepath.exists():
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    # Merge with defaults for backward compatibility
                    self.data.update(loaded)
            except (json.JSONDecodeError, IOError):
                pass  # Use defaults on error
        
        # Set first_seen if new user
        if self.data["first_seen"] is None:
            self.data["first_seen"] = str(datetime.date.today())
        
        self.data["last_seen"] = str(datetime.date.today())
    
    def save(self):
        """Save data to file"""
        try:
            self.filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"⚠️  Gagal menyimpan data: {e}")
    
    def get(self, key: str, default=None):
        """Get value by key (dot notation supported)"""
        value = self.data
        for k in key.split('.'):
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
    
    def set(self, key: str, value):
        """Set value by key (dot notation supported)"""
        keys = key.split('.')
        target = self.data
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        self.save()
    
    def increment(self, key: str, amount: int = 1):
        """Increment a numeric value"""
        current = self.get(key, 0) or 0
        self.set(key, current + amount)
    
    def append_list(self, key: str, item):
        """Append item to a list"""
        current = self.get(key, []) or []
        if item not in current:
            current.append(item)
            self.set(key, current)
    
    def record_topic(self, topic: str):
        """Record a learned topic"""
        self.append_list("topics_learned", topic)
    
    def record_quiz_score(self, topic: str, score: float):
        """Record a quiz score"""
        entry = {
            "topic": topic,
            "score": score,
            "date": str(datetime.date.today()),
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.data["quiz_scores"].append(entry)
        self.save()
    
    def add_note(self, key: str, value: str):
        """Add or update a note"""
        notes = self.data.setdefault("notes", {})
        notes[key] = value
        self.save()
    
    def get_note(self, key: str) -> str | None:
        """Retrieve a note"""
        return self.data.get("notes", {}).get(key)
    
    def delete_note(self, key: str) -> bool:
        """Delete a note"""
        if key in self.data.get("notes", {}):
            del self.data["notes"][key]
            self.save()
            return True
        return False
    
    def list_notes(self) -> dict:
        """List all notes"""
        return self.data.get("notes", {}).copy()
    
    def get_stats(self) -> dict:
        """Get user statistics"""
        scores = self.data.get("quiz_scores", [])
        avg_score = (
            sum(s["score"] for s in scores) / len(scores) 
            if scores else 0
        )
        return {
            "name": self.data.get("name") or "Anonim",
            "topics_count": len(self.data.get("topics_learned", [])),
            "conversations": self.data.get("conversation_count", 0),
            "quizzes_taken": len(scores),
            "average_score": avg_score,
            "first_seen": self.data.get("first_seen"),
            "last_seen": self.data.get("last_seen"),
        }
