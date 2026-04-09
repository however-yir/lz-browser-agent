"""Primary package namespace for LZ Browser Agent.

This package keeps the codebase in the existing ``browser_use/`` tree while
exposing a renamed import namespace: ``lz_browser_agent``.
"""

from __future__ import annotations

import importlib
from pathlib import Path
from pkgutil import extend_path

# Keep namespace-package behavior and append legacy source path.
__path__ = extend_path(__path__, __name__)  # type: ignore[name-defined]
_legacy_source = Path(__file__).resolve().parent.parent / 'browser_use'
if _legacy_source.exists():
	__path__.append(str(_legacy_source))

_legacy_module = importlib.import_module('browser_use')


def __getattr__(name: str):
	return getattr(_legacy_module, name)


def __dir__():
	return sorted(set(globals().keys()) | set(dir(_legacy_module)))


__all__ = list(getattr(_legacy_module, '__all__', []))
