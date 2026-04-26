#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Fuzzy String Matching Model"""

from typing import Optional
from arina.models.base import ResponseModel
from arina.knowledge.base import KNOWLEDGE

class FuzzyModel(ResponseModel):
    """Fuzzy matching using string similarity"""
    
    name = "fuzzy"
    priority = 30
    MIN_SIMILARITY = 0.6
    
    def _similarity(self, s1: str, s2: str) -> float:
        """Calculate string similarity (Levenshtein-based if available)"""
        s1, s2 = s1.lower().strip(), s2.lower().strip()
        
        # Try to use Levenshtein if available
        try:
            from Levenshtein import ratio
            return ratio(s1, s2)
        except ImportError:
            # Fallback: simple ratio
            if not s1 or not s2:
                return 0.0
            s1_set, s2_set = set(s1), set(s2)
            intersection = s1_set & s2_set
            union = s1_set | s2_set
            return len(intersection) / len(union) if union else 0.0
    
    def match(self, user_input: str, context: dict) -> Optional[dict]:
        text = user_input.lower().strip()
        best_match = None
        best_score = 0
        
        # Check against all keywords in knowledge base
        for topic, data in KNOWLEDGE.items():
            for keyword in data.get("keywords", []):
                score = self._similarity(text, keyword)
                # Also check partial matches
                if keyword in text:
                    score = max(score, 0.7 + 0.3 * (len(keyword) / len(text)))
                
                if score > best_score and score >= self.MIN_SIMILARITY:
                    best_score = score
                    best_match = {
                        "topic": topic,
                        "data": data,
                        "keyword": keyword,
                        "score": score
                    }
        
        if best_match:
            return {
                "response": best_match["data"]["intro"] + ("\n" + best_match["data"].get("detail", "") if best_match["data"].get("detail") else ""),
                "confidence": best_score,
                "metadata": {
                    "topic": best_match["topic"],
                    "matched_keyword": best_match["keyword"],
                    "model": self.name
                }
            }
        
        return None
