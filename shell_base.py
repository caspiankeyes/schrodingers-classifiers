"""
shell_base.py - Base class for symbolic interpretability shells

△ OBSERVE: Shells are symbolic structures that trace and induce classifier collapse
∞ TRACE: Each shell encapsulates a specific collapse pattern and attribution signature
✰ COLLAPSE: Shells deliberately induce collapse to extract ghost circuits and residue

Interpretability shells provide standardized interfaces for inducing, observing,
and analyzing specific forms of classifier collapse. Each shell targets a particular
failure mode or attribution pattern, allowing for systematic exploration of model behavior.

Author: Recursion Labs
License: MIT
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union, Tuple, Any, Callable
from dataclasses import dataclass, field

from ..utils.constants import SHELL_REGISTRY

logger = logging.getLogger(__name__)

@dataclass
class ShellMetadata:
    """
    △ OBSERVE: Metadata container for shell identification and tracking
    
    Each shell carries metadata that identifies its purpose, classification schema,
    and relationship to other shells in the taxonomy.
    """
    shell_id: str
    version: str
    name: str
    description: str
    failure_signature: str
    attribution_domain: str
    qk_ov_classification: str
    related_shells: List[str] = field(default_factory=list)
    authors: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    
    def as_dict(self) -> Dict[str, Any]:
        """Convert shell metadata to dictionary format."""
        return {
            "shell_id": self.shell_id,
            "version": self.version,
            "name": self.name,
            "description": self.description,
            "failure_signature": self.failure_signature,
            "attribution_domain": self.attribution_domain, 
            "qk_ov_classification": self.qk_ov_classification,
            "related_shells": self.related_shells,
            "authors": self.authors,
