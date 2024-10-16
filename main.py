import os
import pyaudio
import json
import vosk

# Path to the Vosk model directory
MODEL_PATH = r"D:\voice_To_Text\vosk-model-small-en-us-0.15"

# Initialize Vosk model
if not os.path.exists(MODEL_PATH):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

# Load the model
model = vosk.Model(MODEL_PATH)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open the microphone stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Recognizer object to process the audio
recognizer = vosk.KaldiRecognizer(model, 16000)

print("Listening for the wake word 'Sunday'...")

def process_transcription(transcription):
    if "Sunday" in transcription:
        print("Wake word detected!")
        # Only display the part after 'Sunday'
        sunday_index = transcription.index("Sunday")
        command = transcription[sunday_index + len("Sunday "):]
        print(f"Command: {command}")
    else:
        print("No wake word detected.")

try:
    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_json = json.loads(result)
            if result_json['text']:
                transcription = result_json['text']
                print(f"Detected speech: {transcription}")
                process_transcription(transcription)

except KeyboardInterrupt:
    print("Stopping...")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
