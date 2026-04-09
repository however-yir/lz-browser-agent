# 1. Install Ollama: https://github.com/ollama/ollama
# 2. Run `ollama serve` to start the server
# 3. Pull a model you want to use:
#    ollama pull qwen2.5:7b-instruct

from lz_browser_agent import Agent, ChatOllama

from examples.common.local_runtime import load_local_runtime_config

config = load_local_runtime_config(default_task='帮我查一下 browser-use 仓库的核心能力并总结 3 点')

llm = ChatOllama(model=config.ollama_model, host=config.ollama_host)

Agent(config.task, llm=llm).run_sync()
