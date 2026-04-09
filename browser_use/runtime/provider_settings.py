"""Centralized provider configuration resolution."""

from __future__ import annotations

import os


def _first_non_empty(*keys: str) -> str | None:
	for key in keys:
		value = os.getenv(key, '').strip()
		if value:
			return value
	return None


def resolve_browser_use_api_key(explicit_api_key: str | None = None) -> str | None:
	return explicit_api_key or _first_non_empty('LZ_BROWSER_AGENT_API_KEY', 'BROWSER_USE_API_KEY')


def resolve_browser_use_base_url(explicit_base_url: str | None = None) -> str:
	return (
		explicit_base_url
		or _first_non_empty('LZ_BROWSER_AGENT_LLM_URL', 'BROWSER_USE_LLM_URL')
		or 'https://llm.api.browser-use.com'
	)


def resolve_ollama_host(explicit_host: str | None = None) -> str | None:
	return explicit_host or _first_non_empty('LZ_BROWSER_AGENT_OLLAMA_HOST', 'BROWSER_USE_OLLAMA_HOST', 'OLLAMA_HOST')
