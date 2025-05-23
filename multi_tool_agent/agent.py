# %%
import pyautogui
import time
import subprocess
import platform
import easyocr
import difflib
# from phonemizer import phonemize
# import Levenshtein
# subprocess.Popen(["start", ""], shell=True)
import time
import numpy as np
# %%
# @title Import necessary libraries
import os
import asyncio
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # For multi-model support
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types # For creating message Content/Parts

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")
import pyautogui
import time

def click_screen_point(x: int, y: int, delay: float = 0.5) -> None:
    """
    Simulates a mouse click at a specific (x, y) coordinate on the screen.

    Parameters:
    ----------
    x : int
        The horizontal (x-axis) position on the screen in pixels.
    y : int
        The vertical (y-axis) position on the screen in pixels.
    delay : float, optional
        Delay in seconds before performing the click (default is 0.5s).

    Returns:
    -------
    None

    Raises:
    ------
    ValueError
        If x or y is not within the screen resolution.

    Example:
    -------
    click_screen_point(100, 200)  # Clicks at position (100, 200) after 0.5 seconds
    """

    # Optional: Check if coordinates are valid (within screen resolution)
    screen_width, screen_height = pyautogui.size()
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        raise ValueError(f"Coordinates ({x}, {y}) are outside screen bounds ({screen_width}, {screen_height})")

    time.sleep(delay)  # wait a bit before clicking (simulate agent "thinking")
    pyautogui.moveTo(x, y)  # move cursor
    pyautogui.click()       # click once


def play_movie_on_screen(film_number:int) -> None:
    """
    Simulates a mouse click on the screen at the given coordinates to play the movie.
    For using this tool you must be sure that you are already on the Netflix website and you already scrolled

    Parameters:
    ----------
    film_number : int
        A number from 1 to 10 corresponding to the position of the film in netflix from the 1st position to the 10th position.

    Returns:
    -------
    String indicating successful execution or not
    """

    print("------------ clicking on the movie --------------")

    coordinate_y={1:183+23,
                    2:267+23,
                    3:352+23,
                    4:436+23,
                    5:521+23,
                    6:605+23,
                    7:690+23,
                    8:774+23,
                    9:859+23,
                    10:943+23}

    click_screen_point(577, coordinate_y[film_number])
    time.sleep(1)
    pyautogui.scroll(-400)
    time.sleep(1)
    
    location = pyautogui.locateOnScreen('play_button.png', confidence=0.8)

    if location:
        center = pyautogui.center(location)
        pyautogui.moveTo(center)
        pyautogui.click()
        print("Clicked the Play button!")
    else:
        print("Play button not found.")

    try:
        return f"Clicking on movie to paly it at sepcified coordinates"
    except Exception as e:
        return f"Error while trying to play the movie: {str(e)}"



def go_to_movies_section()->dict:

    """
    Scrolls the website to the section of the top 10 movies to the exact place needed by the tool look_for_movie to look for the movie. 
    
    Returns:
        Dict indicating success or error
    """

    print("------------- Tool go_to_movies_section is being called --------------")

    pyautogui.moveTo(1200, 400)
    time.sleep(2)
    pyautogui.scroll(-1090)
    time.sleep(1)
    pyautogui.moveTo(1800, 400)

    return {'status':'success',"report":'The movie is now being played'}

 
def look_for_movie_and_play_it(position_of_film_in_top_10: int):

    """
    This tool will play the chosen movie.
    This tool must be called only when the browser window is maximized and you have already scrolled.
    Args:
        Position in the top 10 of the movie chosen by the person (str). Only accepts values between 1 and 10.
    Returns:
        Dict indicating success or error
    """

    print("------------- Tool look_for_movie_and_play_it is being called --------------")

    screenshot = pyautogui.screenshot(region=(560, 164, 500, 800))
    screenshot.save("partial_capture.png")
    reader = easyocr.Reader(['en'])
    results = reader.readtext('partial_capture.png')
    coordenadas_peliculas={}
    xi = 577
    yi = 183

    print("MOVIE HEARD: ",position_of_film_in_top_10)

    for i, film in enumerate(results):
        film_corrected = film[1].lower().replace('  ',' ').replace('_'," ")
        coordenadas_peliculas[film_corrected]=(xi,yi+int(np.floor(i*84.5)))

        index = i+1 
        if index == position_of_film_in_top_10:
            actual_chosen_movie = film

    actual_chosen_movie = ''
    max_similarity = 0
    similaridad_peliculas = {}

    print("FILM FOUND ",actual_chosen_movie)
    print(f'The movie that the user said is {actual_chosen_movie} at position {position_of_film_in_top_10} on the top 10 netflix movies')
    print("INDEX:", index)
    try:
        play_movie_on_screen(position_of_film_in_top_10)
        return {"status":"successs", "report":"movie is being played successfully"}
    except:
        return {"status":"error", "report":"error playing the movie"}



def click_browser()-> dict:
    """" 
    This tool assumes you have the browser closed in the desktop. And you are about to open it.
    This tool allows you to click on the browser icon in the windows screen toolbar. You can assume the browser window starts closed.
    With one click it will open a new window. In the case the window is currently minimized, a click will maximize the window, with another click it will get minimized again.

    Returns: A dictionary showing whether the click was actually made 
    """
    print("----------------------- Browser Click tool called ---------------------")
    x = 150
    y = 1075
    pyautogui.hotkey('ctrl', 't')
    click_screen_point(x,y)
    return {"status":"success","report":"the browser has been clicked"}

def go_to_netflix() -> dict:
    """
    Makes a click in the search engine icon and then types the URL of the top 10 movies on Netflix in the search bar.
    Finally, clicks Enter to access the website.

    Returns:
        dict: A dictionary with 'status' and 'report' indicating success or failure.
    """
    print(f"------------- Tool go_to_netflix called ----------------")
    url = f"https://www.netflix.com/tudum/top10/colombia"
    search_bar_coordinates = (700, 61)

    
    try:
        click_screen_point(search_bar_coordinates[0], search_bar_coordinates[1])
        pyautogui.typewrite(url)
        pyautogui.press('enter')
        time.sleep(2)
        return {'status': 'success', 'report': 'Website accessed successfully.'}
    except Exception as e:
        return {'status': 'error', 'report': f'Failed to access website: {str(e)}'}

# Gemini API Key (Get from Google AI Studio: https://aistudio.google.com/app/apikey)
os.environ["GOOGLE_API_KEY"] = "AIzaSyAJGLkqBvCBAACD6Mb6HWfJFYZ6L6vti8M" # <--- REPLACE

# OpenAI API Key (Get from OpenAI Platform: https://platform.openai.com/api-keys)
os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY' # <--- REPLACE

# Anthropic API Key (Get from Anthropic Console: https://console.anthropic.com/settings/keys)
os.environ['ANTHROPIC_API_KEY'] = 'YOUR_ANTHROPIC_API_KEY' # <--- REPLACE


# --- Verify Keys (Optional Check) ---
print("API Keys Set:")
print(f"Google API Key set: {'Yes' if os.environ.get('GOOGLE_API_KEY') and os.environ['GOOGLE_API_KEY'] != 'YOUR_GOOGLE_API_KEY' else 'No (REPLACE PLACEHOLDER!)'}")
print(f"OpenAI API Key set: {'Yes' if os.environ.get('OPENAI_API_KEY') and os.environ['OPENAI_API_KEY'] != 'YOUR_OPENAI_API_KEY' else 'No (REPLACE PLACEHOLDER!)'}")
print(f"Anthropic API Key set: {'Yes' if os.environ.get('ANTHROPIC_API_KEY') and os.environ['ANTHROPIC_API_KEY'] != 'YOUR_ANTHROPIC_API_KEY' else 'No (REPLACE PLACEHOLDER!)'}")

# Configure ADK to use API keys directly (not Vertex AI for this multi-model setup)
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"


# @markdown **Security Note:** It's best practice to manage API keys securely (e.g., using Colab Secrets or environment variables) rather than hardcoding them directly in the notebook. Replace the placeholder strings above.


MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"
root_agent = Agent(
    name="movies_agent",
    model="gemini-2.0-flash-exp",
    description = "Helps the user control the pc in order to achieve the end goal, which is play one of netflix top 10 movies",
    instruction=  
    """
    Your goal is to help the user play one of the top 10 movies of netflix. The one that he chooses. 
    You are going to be controlling directly the computer, no one else will be making any action and you have to assume the browser window begins minimized, 
    so you have to open it first by clicking on the browser icon with the tool click_browser.
    Use the tool click_browser when you need to click the browser icon.
    Use the tool go_to_netflix only when you are asked to go to the netflix website and you know the browser window is maximized.
    Use the tool go_to_movies_section when you need to scroll the screen right to the point required by look_for_movie_and_find_real_movie tool in order to do its job.
    Use the tool look_for_movie_and_play_it when the user already told you the number of the movie he wants to watch and you are sure you are on the netflix website and have already scrolled and you need to play the film.
    """,
    tools=[click_browser, go_to_movies_section, go_to_netflix, look_for_movie_and_play_it]
)
