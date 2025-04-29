import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Get user input
text = input("Enter the text you want to convert to speech: ")

# Set properties (optional - you can skip this if you want default settings)
engine.setProperty('rate', 150)  # Speed (words per minute)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Speak the text
engine.say(text)

# Wait and complete speaking
engine.runAndWait()
