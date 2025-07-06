from controller import handle_conversation
from utils import wait_for_wake_word
import pyaudio

while True:
    wait_for_wake_word()
    handle_conversation()
