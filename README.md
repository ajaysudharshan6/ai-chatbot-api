# AI Chatbot API

A conversational AI API built with FastAPI, featuring memory management and LLM integration.
NOTE: This is for testing purposes only.

## Features

- RESTful chat API endpoints
- Conversation memory management
- Multi-user support
- LLM service integration (OpenAI compatible)
- CORS enabled
- Docker support
- Environment-based configuration

## Quick Start

### Prerequisites
- Python 3.11+
- pip or conda

### Installation

1. Clone the repository:
```bash
git clone <repo-url>
cd ai-chatbot-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

4. Run the application:
```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Chat
- `POST /api/v1/chat` - Send a message and get a response
- `GET /api/v1/history/{user_id}` - Get conversation history
- `DELETE /api/v1/history/{user_id}` - Clear conversation history

### Health
- `GET /health` - Health check endpoint

## Docker

Build and run with Docker:

```bash
docker build -t ai-chatbot-api .
docker run -p 8000:8000 --env-file .env ai-chatbot-api
```

## Project Structure

```
ai-chatbot-api/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── api/routes/chat.py     # Chat endpoints
│   ├── services/llm_service.py # LLM integration
│   ├── models/schemas.py       # Pydantic models
│   ├── core/config.py          # Configuration
│   ├── memory/                 # Memory management
│   └── utils/helpers.py        # Utility functions
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── .env                        # Environment variables
└── README.md                   # This file
```

## Configuration

Edit `.env` to configure:
- LLM model and API key
- Memory settings
- CORS origins
- Temperature and max tokens

## Development

### Running Tests
```bash
pytest
```

### Linting
```bash
black app/
flake8 app/
```

## License

MIT License

## Contributing

Contributions are welcome! Please create a pull request with your changes.
