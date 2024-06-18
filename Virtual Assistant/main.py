import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Rajatyadav: {query}\n ION: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except openai.error.OpenAIError as e:
        print(f"Error calling OpenAI API: {e}")
        say("Sorry, I encountered an error. Please try again later.")
        return ""

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except openai.error.OpenAIError as e:
        print(f"Error calling OpenAI API: {e}")
        say("Sorry, I encountered an error while using artificial intelligence. Please try again later.")
        return ""

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")


    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

    return text


def say(text):
    os.system(f'say "{text}"')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(f"Error recognizing speech: {e}")
            say("Sorry, I couldn't understand you. Please try again.")
            return ""


if __name__ == '__main__':
    print('Welcome to ION A.I')
    say("ION A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath = "/Users/rajatyadav/Desktop/songs/YadavBrand2.mp3"
            os.system(f"open {musicPath}")

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is{strfTime}")

        if "open Calculator".lower() in query.lower():
            os.system(f"open /System/Applications/Calculator.app")

        if "open Asphalt9".lower() in query.lower():
            os.system(f"open /Applications/Asphalt9.app")
