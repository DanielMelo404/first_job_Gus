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


## 🚀 How It Works
The AI agent is programmed to simulate how a user would:

1. Click the browser icon on the taskbar.

2. Navigate to Netflix Top 10 (Colombia).

3. Scroll to the "Top 10 Movies" section.

4. Use OCR to detect and locate the movie in the list.

5. Click "Play" on the selected movie.

## ✅ Supported Agent Tools

Tool | Description
click_browser() | Opens/minimizes the browser
go_to_netflix() | Navigates to Netflix Top 10 page
go_to_movies_section() | Scrolls to movie list section
look_for_movie_and_play_it() | Detects and clicks the selected movie from the top 10 list

## ⚠️ Important Notes

- Assumes your screen resolution and UI layout match the hardcoded coordinates.

- Netflix browser window starts minimized or closed.

- This bot does not perform login. You must already be signed in to Netflix.