from voice_input import listen_to_microphone
from voice_output import speak
from memory import remember, retrieve
from llm_engine import ask_local_llm
from rag_engine import query_documents

def handle_conversation():
    try:
        text = listen_to_microphone()

        if text.lower().startswith("remember that"):
            fact = text[len("remember that"):].strip()
            remember(fact)
            speak("Got it! I'll remember that.")

        elif text.lower().startswith("what did i teach you") or "remember" in text.lower():
            response = retrieve(text)
            speak(f"You told me: {response}")

        elif "document" in text.lower() or "pdf" in text.lower():
            response = query_documents(text)
            speak(response)

        else:
            response = ask_local_llm(text)
            speak(response)
    except Exception as e:
        speak(f"Sorry, something went wrong. {str(e)}")
