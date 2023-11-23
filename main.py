# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "6ed7adfd8c2c46889e0ae2f4c6dd5aed"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe()
transcript = transcriber.transcribe("C://Users//PC//Documents//Sound Recordings")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)
