"""Configuration values and environment-backed settings for the coding agent."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Absolute path to the root of this MVP project.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
# Directory containing the agent's prompt templates.
PRMPTS_DIR = PROJECT_ROOT / "prompts"

# Default location where the agent is allowed to work with project files.
DEFAULT_WORKING_DIR = PROJECT_ROOT / "workspace"

# Human-readable name used to identify the agent.
AGENT_NAME = "CodingAgent"

# Runtime limits read from environment variables, with safe defaults.
MAX_MODEL_PER_RUN = int(os.getenv("MAX_MODEL_PER_RUN", "10"))
MAX_READ_BYTES = int(os.getenv("MAX_READ_BYTES", "1000000"))  # 1 MB


def hitl_enabled() -> bool:
    """Return whether human-in-the-loop approval is enabled by configuration."""
    return os.getenv("HITL_ENABLED", "true").lower() in ("true", "1", "yes")

def get_working_dir() -> Path:
    """Return the configured working directory, falling back to the project workspace."""
    override = os.getenv("WORKING_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()
    return DEFAULT_WORKING_DIR.resolve()


print(DEFAULT_WORKING_DIR)


