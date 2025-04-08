import speech_recognition as sr

def listen_and_respond():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening for 5 seconds...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        print("Processing...")

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        respond_to(text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def respond_to(text):
    # Basic response logic – you can expand this
    if "hello" in text.lower():
        print("Hi there!")
    else:
        print("I heard you!")

if __name__ == "__main__":
    listen_and_respond()
