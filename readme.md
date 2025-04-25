🎬 Netflix Top 10 Movie Player Bot
This project automates the process of opening a browser, navigating to Netflix's Top 10 list, and playing a selected movie using computer vision, OCR, and AI agent orchestration.

💡 Overview
Using tools like pyautogui, easyocr, and Google’s Agent Development Kit (ADK), this bot simulates human-like interactions to:

Open your browser.

Navigate to Netflix's Top 10 movies.

Scroll to the right section.

Recognize the movie list visually.

Click to play the movie the user chooses by its position in the top 10.

🛠️ Features
🤖 AI Agent orchestration with Google ADK

🎯 Screen interaction via pyautogui

🔍 Optical Character Recognition (OCR) with easyocr

🔐 Multi-Model API Support: Gemini, OpenAI, and Anthropic

🚀 How It Works
The root_agent is configured to help the user play any movie from the Netflix Top 10 list. It uses tools such as:

click_browser(): Opens the browser from the taskbar.

go_to_netflix(): Navigates to the Netflix Top 10 page for Colombia.

go_to_movies_section(): Scrolls the screen to the required movie list.

look_for_movie_and_play_it(position): Uses OCR to identify and click the selected movie based on its ranking.

🧰 Requirements
Python 3.8+

pyautogui

easyocr

numpy

google-adk

A screen resolution compatible with the click coordinates used

Netflix account and browser already logged in

Install dependencies:

bash
Copiar
Editar
pip install pyautogui easyocr numpy google-generativeai
Optional: You may also need opencv-python for OCR and Pillow for screenshots.

🔑 API Keys
You must provide API keys for the following platforms:

Google Gemini (Gemini 2.0 Flash)

OpenAI (e.g., GPT-4)

Anthropic (Claude)

Set them in your environment or directly in the script (for testing only):

python
Copiar
Editar
os.environ["GOOGLE_API_KEY"] = "your_google_key"
os.environ["OPENAI_API_KEY"] = "your_openai_key"
os.environ["ANTHROPIC_API_KEY"] = "your_anthropic_key"
📌 Important Notes
The script assumes the Netflix browser tab starts closed or minimized.

The system must already be logged in to Netflix.

All screen actions are hardcoded with pixel coordinates; ensure your resolution and UI layout match.

The play_button.png image is required in the script directory for the play button to be recognized on screen.