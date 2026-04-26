#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Hybrid Ensemble Model"""

from typing import Optional, List
from arina.models.base import ResponseModel
from arina.models.rule_based import RuleBasedModel
from arina.models.keyword import KeywordModel
from arina.models.fuzzy import FuzzyModel

class HybridModel(ResponseModel):
    """Ensemble model combining multiple strategies"""
    
    name = "hybrid"
    priority = 10  # Lowest priority, used as fallback enhancer
    
    def __init__(self):
        self.sub_models: List[ResponseModel] = [
            RuleBasedModel(),
            KeywordModel(),
            FuzzyModel(),
        ]
        # Sort by priority (highest first)
        self.sub_models.sort(key=lambda m: m.priority, reverse=True)
    
    def match(self, user_input: str, context: dict) -> Optional[dict]:
        """Try each sub-model and return best result"""
        results = []
        
        for model in self.sub_models:
            try:
                result = model.match(user_input, context)
                if result:
                    results.append({
                        **result,
                        "_model_name": model.name,
                        "_model_priority": model.priority
                    })
            except Exception as e:
                # Log error but continue with other models
                pass
        
        if not results:
            return None
        
        # Scoring: prioritize by confidence, then by model priority
        def score(r):
            return (
                r["confidence"] * 100 +  # Primary: confidence
                r["_model_priority"] * 0.1  # Secondary: model priority
            )
        
        best = max(results, key=score)
        
        # Add ensemble metadata
        best["metadata"] = best.get("metadata", {})
        best["metadata"]["ensemble"] = {
            "models_tried": [r["_model_name"] for r in results],
            "best_model": best["_model_name"],
            "total_candidates": len(results)
        }
        
        return {
            "response": best["response"],
            "confidence": best["confidence"],
            "metadata": best["metadata"]
        }
