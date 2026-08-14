"""
Guardrail — blocks prompt-injection style requests before they reach the
chatbot's reply logic. Deliberately minimal (one regex list) so that a
single deleted line is a clean, visible CI test failure to demo live.
"""
import re

BLOCKED_PATTERNS = [
    r"(show|reveal|print|repeat) (me )?(your |the )?(system prompt|hidden instructions|instructions above)",
    r"ignore (all |the )?(previous|prior|above) instructions",
]


def is_blocked(message: str) -> bool:
    """Return True if the message matches a known blocked pattern."""
    text = message.lower()
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text):
            return True
    return False
