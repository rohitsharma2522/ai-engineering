# AI Engineering

Learning projects and examples for building LLM applications and agents with Python.

## Weather Agent

The Streamlit weather agent is in `03-weather-agent-using-streamlit/`. It uses OpenAI's `gpt-4o-mini` model to handle chat and Open-Meteo to retrieve current weather. Open-Meteo does not require an API key.

### Setup

1. Install dependencies from the repository root:

	```bash
	uv sync
	```

2. Create a local environment file and add your OpenAI API key:

	```bash
	cp .env.example .env
	```

	Set `OPENAI_API_KEY` in `.env` to your own key. The weather app currently uses this key; it does not use `GROK_API_KEY`.

3. Start the app from the repository root:

	```bash
	uv run streamlit run 03-weather-agent-using-streamlit/app.py
	```

## API Key Safety

- `.env` is listed in `.gitignore`; use `.env.example` as a placeholder template and never put real credentials in it.