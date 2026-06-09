# AI Chatbot

A command-line chatbot with conversation memory, built in Python using the Claude API. The bot remembers the full conversation and responds as a friendly study assistant.

## Features

- Holds a continuous conversation with memory across turns
- Uses a system prompt to give the assistant a consistent, helpful personality
- Powered by Anthropic's Claude API
- Secure API key handling with a `.env` file

## Requirements

- Python 3.10 or higher
- An Anthropic API key

## Setup

1. Clone this repository:
git clone https://github.com/Nivedkumar0404/AI-chat-bot.git
2. Navigate into the folder:
cd AI-chat-bot
3. Create a virtual environment and activate it:
python -m venv venv
venv\Scripts\activate
4. Install the required libraries:
pip install anthropic python-dotenv
5. Create a `.env` file and add your API key:
ANTHROPIC_API_KEY=your-key-here

## How to Run
python chatbot.py

Type your messages to chat with the assistant. Type `quit` to exit.

## What I Learned

This project taught me how to work with an LLM API, manage conversation history (the "memory" pattern), use system prompts to control behavior, and handle secret keys securely with environment variables.