from voice_input import listen_to_microphone

def wait_for_wake_word(wake_word="jarvis"):
    print(f"👂 Waiting for wake word: '{wake_word}'")
    while True:
        text = listen_to_microphone().lower()
        if wake_word in text:
            print("🟢 Wake word detected!")
            return
