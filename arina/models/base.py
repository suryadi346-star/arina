#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ARINA - Base Model Interface"""

from abc import ABC, abstractmethod
from typing import Optional

class ResponseModel(ABC):
    """Abstract base class for response models"""
    
    name: str = "base"
    priority: int = 0  # Higher = checked first
    
    @abstractmethod
    def match(self, user_input: str, context: dict) -> Optional[dict]:
        """
        Try to match user input and return response metadata.
        Returns None if no match, or dict with:
        {
            "response": str,      # The response text
            "confidence": float,  # 0.0-1.0 match confidence
            "metadata": dict,     # Optional extra data
        }
        """
        pass
    
    def format_response(self, match: dict) -> str:
        """Format the matched response for display"""
        return match.get("response", "")
    
    def __repr__(self):
        return f"{self.__class__.__name__}(priority={self.priority})"
