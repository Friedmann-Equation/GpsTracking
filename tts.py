import os
import pygame
from gtts import gTTS

# Initialize pygame mixer
pygame.mixer.init()

# Test text in Indonesian
test_text = "Halo, ini adalah tes fungsi text-to-speech menggunakan Google Text-to-Speech."

# Print the test text to the console
print(test_text)

# Generate speech using gTTS in Indonesian
tts = gTTS(text=test_text, lang='id')

# Save the speech to a file
speech_file = "test_speech.mp3"
tts.save(speech_file)

# Play the speech file using pygame
pygame.mixer.music.load(speech_file)
pygame.mixer.music.play()

# Wait for the speech to finish
while pygame.mixer.music.get_busy():
    continue

# Clean up the speech file
os.remove(speech_file)