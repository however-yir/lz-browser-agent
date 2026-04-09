"""Utilities for loading local development runtime settings."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class LocalRuntimeConfig:
	"""Runtime values used by example scripts."""

	task: str
	ollama_model: str
	ollama_host: str | None


def load_local_runtime_config(
	*,
	default_task: str,
	default_model: str = 'qwen2.5:7b-instruct',
) -> LocalRuntimeConfig:
	"""
	Load runtime values from environment variables for local examples.

	Supported variables:
	- ``BROWSER_USE_DEFAULT_TASK``
	- ``BROWSER_USE_OLLAMA_MODEL``
	- ``BROWSER_USE_OLLAMA_HOST``
	"""
	return LocalRuntimeConfig(
		task=os.getenv('BROWSER_USE_DEFAULT_TASK', default_task),
		ollama_model=os.getenv('BROWSER_USE_OLLAMA_MODEL', default_model),
		ollama_host=os.getenv('BROWSER_USE_OLLAMA_HOST'),
	)
