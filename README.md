# Desktop-AI (for Windows ONLY)
This is a desktop AI called 'Jarvis" which uses an API key to connect to Gemini then perform various tasks.
Fetures are( IT REQUIRES AN ANTIVE INTERNET CONNECTION.):
1. Wake word detection ("Jarvis")
2.  Voice verification - only responds to the owner's voice
3. System controls: lock, shutdown (with confirmation)
4. Google search by voice
5. Volume up / down / mute
6. Falls back to Gemini for general conversation
7. Text-to-speech replies via edge-tts
SEtUP:
Clone the repo and install dependencies:
pip install -r requirements.txt
  Record a 5-10 second clip of your own voice, save it as `owner.wav`,
   and place it in a `voices/` folder in the project root.
 Get a free Gemini API key from
   [Google AI Studio](https://aistudio.google.com/app/apikey) and set it
   as an environment variable:
   setx GEMINI_API_KEY "your-key-here"
   IT REQUIRES AN ANTIVE INTERNET CONNECTION.
