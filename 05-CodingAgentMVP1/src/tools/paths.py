"""Path helpers that normalize paths and keep file access inside the workspace."""

import fnmatch
from pathlib import Path

from config.config import get_working_dir

# File and directory patterns that the agent must not access.
BLOCKED_PATH_PATTERNS = [
    ".env",
    "venv",
    ".pem",
    ".key",
    ".crt",
    ".p12",
    ".log",
    ",git",
    "secrets"
]

def normalize_path(path: str) -> str:
    """Convert a path to POSIX format and remove a leading ``./`` prefix."""
    normalized = Path(path).as_posix()
    if normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized

def is_path_blocked(path: str) -> bool:
    """Return whether a path matches one of the blocked access patterns."""
    normalized_path = normalize_path(path)
    return any(fnmatch(normalized_path, pattern) for pattern in BLOCKED_PATH_PATTERNS)

def resolve_work_path(path: str) -> Path:
    """Resolve a path inside the configured working directory.

    Raises:
        ValueError: If the resolved path would escape the working directory.
    """
    working_dir = get_working_dir()
    working_dir.mkdir(parents=True, exist_ok=True)
    candidate = (working_dir / path).resolve()   
    try:
        candidate.relative_to(working_dir)
    except ValueError:
        raise ValueError(f"Path {candidate} is outside the working directory {working_dir}")

