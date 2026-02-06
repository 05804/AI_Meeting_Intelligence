import whisper

print("Loading AI model...")
model = whisper.load_model("base")

print("Listening to meeting audio...")
result = model.transcribe("ai meeting.mp3")


with open("transcript.txt", "w", encoding="utf-8") as file:
    file.write(result["text"])

print("Done! Transcript saved as transcript.txt")
