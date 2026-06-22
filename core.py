import os
import ctypes
import webbrowser

from ear import listen
from mouth import speak
from brain import ask_llm


class JarvisCore:
    def __init__(self):
        self.active = False

    def wake(self):
        self.active = True
        speak("Yes sir. I am online.")

    def sleep(self):
        self.active = False
        speak("Going to standby mode.")

    def handle(self, query):
        query = query.lower()

        if "lock" in query:
            self._handle_lock()

        elif "shutdown" in query:
            self._handle_shutdown()

        elif "open google" in query:
            speak("Opening Google, sir.")
            webbrowser.open("https://www.google.com")

        elif "search" in query:
            self._handle_search(query)

        elif "volume up" in query:
            speak("Turning volume up.")
            for _ in range(5):
                ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)

        elif "volume down" in query:
            speak("Turning volume down.")
            for _ in range(5):
                ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)

        elif "mute" in query:
            speak("Toggling mute.")
            ctypes.windll.user32.keybd_event(0xAD, 0, 0, 0)

        else:
            # Not a recognized command - let the LLM handle it conversationally
            speak(ask_llm(query))

    def _handle_lock(self):
        speak("Are you sure you want to lock the computer, sir?")
        if self._confirmed():
            speak("Locking the workstation, sir.")
            ctypes.windll.user32.LockWorkStation()
        else:
            speak("Locking sequence aborted, sir.")

    def _handle_shutdown(self):
        speak("Are you sure you want to shut down the computer, sir?")
        if self._confirmed():
            speak("Shutting down the system. Goodbye, sir.")
            os.system("shutdown /s /t 5")
        else:
            speak("Shutdown sequence aborted, sir.")

    def _handle_search(self, query):
        search_query = (
            query.replace("jarvis", "")
            .replace("search up", "")
            .replace("search google for", "")
            .replace("search for", "")
            .replace("search", "")
            .strip()
        )

        if not search_query:
            speak("What would you like me to search for, sir?")
            search_query = listen()
            if not search_query:
                return

        speak(f"Searching Google for {search_query}, sir.")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    def _confirmed(self):
        """Listens for a yes/no style confirmation after a risky action prompt."""
        response = listen()
        if not response:
            speak("No response detected.")
            return False

        response = response.lower()
        return any(word in response for word in ("yes", "yeah", "do it", "confirm"))
