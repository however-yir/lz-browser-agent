from lz_browser_agent.runtime.provider_settings import (
	resolve_browser_use_api_key,
	resolve_browser_use_base_url,
	resolve_ollama_host,
)


def test_resolve_api_key_prefers_explicit(monkeypatch):
	monkeypatch.setenv('LZ_BROWSER_AGENT_API_KEY', 'env-key')

	assert resolve_browser_use_api_key('explicit-key') == 'explicit-key'


def test_resolve_api_key_uses_new_namespace_first(monkeypatch):
	monkeypatch.setenv('BROWSER_USE_API_KEY', 'legacy-key')
	monkeypatch.setenv('LZ_BROWSER_AGENT_API_KEY', 'new-key')

	assert resolve_browser_use_api_key() == 'new-key'


def test_resolve_base_url_fallback_order(monkeypatch):
	monkeypatch.delenv('LZ_BROWSER_AGENT_LLM_URL', raising=False)
	monkeypatch.delenv('BROWSER_USE_LLM_URL', raising=False)
	assert resolve_browser_use_base_url() == 'https://llm.api.browser-use.com'

	monkeypatch.setenv('BROWSER_USE_LLM_URL', 'http://legacy-llm.local/v1')
	assert resolve_browser_use_base_url() == 'http://legacy-llm.local/v1'

	monkeypatch.setenv('LZ_BROWSER_AGENT_LLM_URL', 'http://new-llm.local/v1')
	assert resolve_browser_use_base_url() == 'http://new-llm.local/v1'


def test_resolve_ollama_host_supports_aliases(monkeypatch):
	monkeypatch.delenv('LZ_BROWSER_AGENT_OLLAMA_HOST', raising=False)
	monkeypatch.delenv('BROWSER_USE_OLLAMA_HOST', raising=False)
	monkeypatch.setenv('OLLAMA_HOST', 'http://fallback-ollama.local:11434')
	assert resolve_ollama_host() == 'http://fallback-ollama.local:11434'

	monkeypatch.setenv('BROWSER_USE_OLLAMA_HOST', 'http://legacy-ollama.local:11434')
	assert resolve_ollama_host() == 'http://legacy-ollama.local:11434'

	monkeypatch.setenv('LZ_BROWSER_AGENT_OLLAMA_HOST', 'http://new-ollama.local:11434')
	assert resolve_ollama_host() == 'http://new-ollama.local:11434'
