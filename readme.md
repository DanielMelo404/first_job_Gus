# 🎬 Netflix Top 10 Movie Player Bot

> An AI-powered bot that opens your browser, navigates to Netflix, and plays your chosen movie from the Top 10 list — just like a human would.

---

## ✨ Features

- 🖱️ Automates mouse movements and clicks using `pyautogui`
- 🔍 Uses OCR (`easyocr`) to read movie names from the screen
- 🤖 Built with Google’s Agent Development Kit (ADK)
- 🔑 Supports multiple LLMs: Gemini, OpenAI, and Anthropic
- 🧠 Intelligent agent that follows step-by-step instructions to achieve your goal

---

## 📦 Requirements

- Python 3.8 or higher  
- Netflix account (logged in)
- Compatible screen resolution for hardcoded clicks  
- Browser pinned to taskbar  
- Required Python libraries:

```bash
pip install pyautogui easyocr numpy google-generativeai
