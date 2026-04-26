#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Response Engine with Multi-Model Support"""

import random
from typing import Optional
from config import DEFAULT_MODEL, MODELS_ENABLED
from arina.models.base import ResponseModel
from arina.models.hybrid import HybridModel
from arina.models.rule_based import RuleBasedModel
from arina.models.keyword import KeywordModel
from arina.models.fuzzy import FuzzyModel

class ResponseEngine:
    """Multi-model response selection engine"""
    
    MODEL_REGISTRY = {
        "rule_based": RuleBasedModel,
        "keyword": KeywordModel,
        "fuzzy": FuzzyModel,
        "hybrid": HybridModel,
    }
    
    def __init__(self, model_name: str = None):
        self.model_name = model_name or DEFAULT_MODEL
        self.model: Optional[ResponseModel] = self._load_model()
        
        # Fallback models if primary fails
        self.fallbacks = [
            RuleBasedModel(),  # Always have rule-based as safety net
        ]
    
    def _load_model(self) -> Optional[ResponseModel]:
        """Load the configured model"""
        if self.model_name not in self.MODEL_REGISTRY:
            return HybridModel()  # Default fallback
        
        model_class = self.MODEL_REGISTRY[self.model_name]
        try:
            return model_class()
        except Exception:
            return HybridModel()
    
    def get_response(self, user_input: str, context: dict) -> tuple[str, dict]:
        """
        Get response for user input.
        Returns: (response_text, metadata_dict)
        """
        # Try primary model
        if self.model:
            try:
                result = self.model.match(user_input, context)
                if result and result.get("confidence", 0) >= 0.5:
                    return result["response"], result.get("metadata", {})
            except Exception:
                pass
        
        # Try fallback models
        for fallback in self.fallbacks:
            try:
                result = fallback.match(user_input, context)
                if result:
                    return result["response"], result.get("metadata", {})
            except Exception:
                continue
        
        # Return None match
        return None, {}
    
    def get_fallback_response(self) -> str:
        """Get a generic fallback response"""
        fallbacks = [
            "Hmm, Arina belum tahu tentang itu. 🤔 Coba ketik 'help' untuk topik tersedia!",
            "Menarik! Arina masih belajar tentang hal itu. Coba tanya Python, Linux, atau cybersecurity! 😊",
            "Arina belum bisa jawab itu. Ketik 'tips' untuk tips teknologi, atau 'quiz python' untuk kuis! 🎯",
        ]
        return random.choice(fallbacks)
    
    def switch_model(self, model_name: str) -> bool:
        """Switch to a different model at runtime"""
        if model_name not in self.MODEL_REGISTRY:
            return False
        try:
            self.model = self.MODEL_REGISTRY[model_name]()
            self.model_name = model_name
            return True
        except Exception:
            return False
