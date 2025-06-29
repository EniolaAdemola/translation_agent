# Translator Agent

---

This project is an AI-powered translation agent that translates English text to Spanish (or other languages) using OpenAI's GPT models. It is built with the [`genai-protocol`](https://pypi.org/project/genai-protocol/) library and is designed to run as a GenAI AgentOS agent, using the [genai-agentos](https://github.com/genai-works-org/genai-agentos) setup with Docker Compose.

---

## Features

- Translates English text to Spanish (or other languages)
- Handles idiomatic expressions for natural-sounding translations
- Uses OpenAI's GPT models (e.g., `gpt-4o-mini`)
- Easily integrates with GenAI AgentOS

---

## Requirements

- Python 3.8+
- Docker & Docker Compose (for AgentOS)
- OpenAI API key
- GenAI JWT token

---

## Setup

### 1. Clone the repository and install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up environment variables

Create a `.env` file in the project root with the following content:

```env
OPENAPI_KEY=your_openai_api_key_here
```

### 3. Configure your GenAI JWT token

Edit `agent.py` and set your JWT token in the `GenAISession` constructor:

```python
genai_session = GenAISession(jwt_token="<your_jwt_token_here>")
```

### 4. (Optional) Set WebSocket URL if using a remote AgentOS instance

Uncomment and set the `ws_url` parameter in `GenAISession` if needed:

```python
# genai_session = GenAISession(jwt_token="...", ws_url="wss://your-ngrok-url")
```

---

## Running the Agent

### Standalone (for development)

```bash
python agent.py
```

### With GenAI AgentOS (Docker Compose)

Follow the instructions in the [genai-agentos GitHub repo](https://github.com/genai-works-org/genai-agentos) to start the AgentOS stack. Then run your agent as above.

---

## Usage

The agent exposes a function:

- **Name:** `translate_en_to_es`
- **Description:** Translate English text to Spanish, handling idioms
- **Parameters:**
  - `text` (string): English text to translate
  - `language` (string): Code of the language to translate to (e.g. 'es')

**Example call:**

```json
{
  "text": "How are you?",
  "language": "es"
}
```

**Example response:**

```json
{
  "translation": "¿Cómo estás?"
}
```

---

## Libraries Used

- [`genai-protocol`](https://pypi.org/project/genai-protocol/)
- [`openai`](https://pypi.org/project/openai/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

---

## References

- [genai-protocol on PyPI](https://pypi.org/project/genai-protocol/)
- [genai-agentos GitHub](https://github.com/genai-works-org/genai-agentos)

**Video Overview:**
[Watch here](https://drive.google.com/file/d/1-HtlYfjnZR198ATFs_NVA_iynjC--KA9/view?usp=sharing)

**App Screenshots:**

![Screenshot 2025-06-29 at 23 48 01](https://github.com/user-attachments/assets/2a2719e7-967a-4d78-a03b-5ca39de9f9f3)
![Screenshot 2025-06-29 at 23 48 21](https://github.com/user-attachments/assets/0a7e5ce7-cb54-406d-b73e-054c55fe9e3e)
![Screenshot 2025-06-29 at 23 48 40](https://github.com/user-attachments/assets/45115495-4e85-47c6-9e3c-98d5bd4376e0)
![Screenshot 2025-06-29 at 23 49 59](https://github.com/user-attachments/assets/73c27ded-9b8e-4745-9187-983eddf79636)
![Screenshot 2025-06-29 at 23 50 09](https://github.com/user-attachments/assets/566edfc6-0acd-4009-87fc-f501d6c7dc58)
