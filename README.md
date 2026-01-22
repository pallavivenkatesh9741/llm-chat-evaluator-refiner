## LLaMA Multi-LLM Chat Aggregator Flask App
### 📌 Project Overview

The LLaMA Multi-LLM Chat Aggregator is a web application built with Flask that integrates multiple Large Language Models (LLMs) to generate high-quality AI responses.
It queries three LLaMA models simultaneously, evaluates their responses, and produces a final aggregated answer for enhanced reliability and accuracy.

This project demonstrates an end-to-end workflow for integrating multiple LLMs with Flask, logging interactions, and returning structured JSON responses.
___

### 🎯 Objective

The objectives of this project are to:

Build a multi-model conversational AI system using LLaMA models

Aggregate outputs from multiple LLMs to produce higher-quality responses

Log user prompts and model outputs for monitoring and evaluation

Deploy a REST API endpoint for chat-based interactions
___

### 🧠 Technology Stack

Language: Python

Web Framework: Flask

Large Language Models: LLaMA via Groq API

Logging: Python logging module

Frontend: HTML (Jinja2 Templates)

Data Format: JSON
___

### 🏗️ Project Structure
project/
- │
- ├── app.py                  # Flask application with LLaMA chat endpoints
- ├── README.md               # Project documentation
- ├── templates/
- │   └── index.html          # Frontend page for user input
- └── llama_chat1.log         # Logged interactions (auto-generated)
