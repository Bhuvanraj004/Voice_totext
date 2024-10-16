# Voice to Text with Vosk

This project implements a voice recognition system that listens for the wake word "Sunday" and processes commands that follow it. It utilizes the Vosk speech recognition toolkit and PyAudio for audio input.

## Features

- Real-time voice recognition
- Wake word detection for the word "Sunday"
- Displays commands after the wake word

## Requirements

- Python 3.6 or higher
- Libraries:
  - `pyaudio`
  - `vosk`
  - `json`
  
You can install the required libraries using pip:

```bash
pip install pyaudio vosk
Model Download
You need to download the Vosk model to use this program. Follow these steps:

Download the model from the Vosk Models page.
Unpack the downloaded model and place it in the D:\voice_To_Text\ directory, ensuring the path is set in the code.
The expected model directory structure should look like this:

makefile
Copy code
D:\
└── voice_To_Text\
    └── vosk-model-small-en-us-0.15\
Usage
Ensure your microphone is connected and configured correctly.
Run the script:
bash
Copy code
python your_script_name.py
The program will start listening for the wake word "Sunday." Upon detection, it will print the command that follows.
Example Output
When the wake word is detected, you might see output like:

arduino
Copy code
Listening for the wake word 'Sunday'...
Detected speech: Sunday turn on the lights
Wake word detected!
Command: turn on the lights
Notes
Make sure you have the correct permissions to access the microphone on your system.
You can modify the wake word and commands in the process_transcription function as needed.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

markdown
Copy code

### Instructions to Create the README.md File

1. **Create a new file**: In your project directory (e.g., `D:\voice_To_Text\Voice_totext`), create a file named `README.md`.

2. **Copy and paste the content**: Copy the content provided above and paste it into the `README.md` file.

3. **Save the file**: Make sure to save the file.

4. **Push to GitHub**: If you have already initialized a Git repository and added this README file, you can push your changes to GitHub:

   ```bash
   git add README.md
   git commit -m "Add README for voice-to-text project"
   git push origin main
