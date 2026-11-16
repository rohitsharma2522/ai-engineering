"""LLM provider definitions and chat-model construction helpers."""

import os
from dotenv import load_dotenv
from dataclasses import dataclass
from langchain_openai import ChatOpenAI


load_dotenv()


@dataclass(frozen=True)
class Provider:
    """Store the configuration needed to connect to one LLM provider."""

    name: str
    env_var: str
    is_free: bool 
    base_url: str | None 
    model: str

# Providers supported by the coding agent and checked during provider selection.
PROVIDERS = [
    Provider(
        "OpenAI",
        "OPENAI_API_KEY",
        False,
        None,
        "gpt-4o-mini",
    )
]

def select_provider() -> Provider:
    """Return the first provider whose required API key exists in the environment.

    Raises:
        RuntimeError: If no configured provider has an available API key.
    """
    for provider in PROVIDERS:
        if os.getenv(provider.env_var):
            return provider
    
    raise RuntimeError("No provider found")

def build_chat_model() -> tuple[ChatOpenAI, Provider]:
    """Create a configured chat model and return it with its provider metadata."""
    provider = select_provider()
    kwargs: dict = {
        "model": provider.model,
        "api_key": os.getenv(provider.env_var),
    }
    if provider.base_url is not None:
        kwargs["base_url"] = provider.base_url
    return ChatOpenAI(**kwargs), provider
