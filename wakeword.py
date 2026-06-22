import speech_recognition as sr


def listen_for_wake_word():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Waiting for wake word 'jarvis'...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                text = recognizer.recognize_google(audio).lower()

                if "jarvis" in text:
                    print("Wake word detected.")
                    return True

            except (sr.UnknownValueError, sr.WaitTimeoutError):
                # Nothing useful heard, just keep listening
                continue
            except Exception as e:
                print(f"Wake word error: {e}")
                continue
