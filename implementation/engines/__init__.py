"""
LLM SSOT Harness - 자동화 엔진
"""

from .meeting_engine import MeetingEngine
from .ssot_engine import SSOTEngine

__version__ = "2.0.0-phase1"
__all__ = [
    "MeetingEngine",
    "SSOTEngine",
]
