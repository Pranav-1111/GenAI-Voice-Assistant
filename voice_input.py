import whisper
import speech_recognition as sr
import shutil
  
print("ffmpeg path:", shutil.which("ffmpeg"))


# Load Whisper model
model = whisper.load_model("base")

def listen_to_microphone():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
    
    print("🧠 Transcribing...")
    
    with open("temp.wav", "wb") as f:
        f.write(audio.get_wav_data())
    
    result = model.transcribe("temp.wav")
    return result["text"]
