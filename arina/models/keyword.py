#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Keyword Extraction Model"""

import re
from typing import Optional, List
from collections import Counter
from arina.models.base import ResponseModel
from arina.knowledge.base import KNOWLEDGE

class KeywordModel(ResponseModel):
    """Keyword frequency-based matching"""
    
    name = "keyword"
    priority = 50
    
    # Stopwords to ignore (Indonesian + English)
    STOPWORDS = {
        'dan', 'atau', 'yang', 'di', 'ke', 'dari', 'pada', 'untuk',
        'the', 'a', 'an', 'is', 'are', 'in', 'on', 'at', 'to', 'for',
        'saya', 'aku', 'kamu', 'anda', 'dia', 'mereka', 'ini', 'itu',
        'apa', 'siapa', 'mengapa', 'bagaimana', 'kapan', 'dimana'
    }
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract meaningful keywords from text"""
        # Normalize and tokenize
        words = re.findall(r'\b[a-zà-ÿ]+\b', text.lower())
        # Filter stopwords and short words
        return [w for w in words if w not in self.STOPWORDS and len(w) > 2]
    
    def match(self, user_input: str, context: dict) -> Optional[dict]:
        keywords = self._extract_keywords(user_input)
        if not keywords:
            return None
        
        # Score each topic by keyword overlap
        scores = {}
        for topic, data in KNOWLEDGE.items():
            topic_keywords = set(kw.lower() for kw in data.get("keywords", []))
            match_count = sum(1 for k in keywords if k in topic_keywords)
            if match_count > 0:
                # Confidence based on match ratio
                confidence = match_count / max(len(keywords), len(topic_keywords))
                scores[topic] = {
                    "matches": match_count,
                    "confidence": confidence,
                    "data": data
                }
        
        if not scores:
            return None
        
        # Return best match above threshold
        best = max(scores.items(), key=lambda x: x[1]["confidence"])
        topic, info = best
        
        if info["confidence"] >= 0.3:  # Minimum threshold
            return {
                "response": info["data"]["intro"] + ("\n" + info["data"].get("detail", "") if info["data"].get("detail") else ""),
                "confidence": info["confidence"],
                "metadata": {
                    "topic": topic,
                    "matched_keywords": [k for k in keywords if k in info["data"].get("keywords", [])],
                    "model": self.name
                }
            }
        
        return None
