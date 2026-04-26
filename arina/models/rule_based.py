#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Rule-Based Response Model"""

import re
from typing import Optional
from arina.models.base import ResponseModel
from arina.knowledge.responses import RESPONSES
from arina.knowledge.base import KNOWLEDGE

class RuleBasedModel(ResponseModel):
    """Exact keyword/trigger matching model"""
    
    name = "rule_based"
    priority = 100  # Highest priority for exact matches
    
    def match(self, user_input: str, context: dict) -> Optional[dict]:
        text = user_input.lower().strip()
        
        # Check small talk responses
        for category, data in RESPONSES.items():
            if any(trigger in text for trigger in data.get("triggers", [])):
                import random
                return {
                    "response": random.choice(data["replies"]),
                    "confidence": 1.0,
                    "metadata": {"category": category, "model": self.name}
                }
        
        # Check knowledge topics
        for topic, data in KNOWLEDGE.items():
            if any(kw in text for kw in data.get("keywords", [])):
                return {
                    "response": data["intro"] + ("\n" + data.get("detail", "") if data.get("detail") else ""),
                    "confidence": 0.95,
                    "metadata": {"topic": topic, "model": self.name}
                }
        
        # Check command patterns
        commands = {
            r'^help$|^bantuan$|^\?$': "HELP_COMMAND",
            r'^clear$|^cls$': "CLEAR_COMMAND",
            r'^profil$|^profile$|^stats$': "PROFILE_COMMAND",
            r'^tips?$': "TIPS_COMMAND",
            r'^quiz\s+(\w+)$': ("QUIZ_COMMAND", r'^quiz\s+(\w+)$'),
            r'^hitung\s+(.+)$': ("CALC_COMMAND", r'^hitung\s+(.+)$'),
            r'^catatan\s+(.+)$': ("NOTES_COMMAND", r'^catatan\s+(.+)$'),
        }
        
        for pattern, cmd in commands.items():
            match = re.match(pattern, text)
            if match:
                if isinstance(cmd, tuple):
                    return {
                        "response": cmd[0],
                        "confidence": 1.0,
                        "metadata": {"args": match.groups(), "pattern": cmd[1], "model": self.name}
                    }
                return {
                    "response": cmd,
                    "confidence": 1.0,
                    "metadata": {"model": self.name}
                }
        
        return None
