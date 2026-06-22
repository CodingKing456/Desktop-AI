# Desktop-AI (JARVIS) (for Windows ONLY)
This is a desktop AI called 'Jarvis" which uses an API key to connect to Gemini then perform various tasks.
_____________________________________________________________________________________________________________________________
Requirements: 
 Installation of PYCharm
 !!Make a folder named jarvis and add all the files except owner.wav. You put owner.wav in voices folder made in the Jarvis folder.!!
1. py -m pip install google-generativeai
2.  py -m pip install SpeechRecognition
3. py -m pip install resemblyzer
4.  py -m pip install numpy
5.  py -m pip install edge-tts
6.  py -m pip install pygame
7.  py -m pip installpycaw
8.  py -m pip installcomtypes
 9. py -m pip install PyAudio
_____________________________________________________________________________________________________________________________
After doing the above activities copy and paste the run_jarvis.bat file in your laptop's startup folder so it always starts when you are online and when your laptop is on. It will have audio access at all times.
_____________________________________________________________________________________________________________________________
Features are( IT REQUIRES AN ANTIVE INTERNET CONNECTION.):
1. Wake word detection ("Jarvis")
2.  Voice verification - only responds to the owner's voice
3. System controls: lock, shutdown (with confirmation)
4. Google search by voice
5. Volume up / down / mute
6. Falls back to Gemini for general conversation
7. Text-to-speech replies via edge-tts
_____________________________________________________________________________________________________________________________
Make sure to download all the .py files and run them in pycharm to install all the needed packages.
_____________________________________________________________________________________________________________________________
SEtUP:
Clone the repo and install dependencies:
pip install -r requirements.txt
  Record a 5-10 second clip of your own voice, save it as `owner.wav`,
   and place it in a `voices/` folder in the project root.
 Get a free Gemini API key from
   [Google AI Studio](https://aistudio.google.com/app/apikey) and set it
   as an environment variable:
   setx GEMINI_API_KEY "your-key-here" (paste this with the GEmini API key in the PYcharm terminal)
You do not need to import your GEMINI API key in the code.
_____________________________________________________________________________________________________________________________
  !! IT REQUIRES AN ACTIVE INTERNET CONNECTION.!!
_____________________________________________________________________________________________________________________________
