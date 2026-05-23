# Emotion Detection Simulation

import random

emotions = ["Happy", "Sad", "Excited", "Neutral"]

detected_emotion = random.choice(emotions)

print("😊 Detected Emotion:", detected_emotion)

if detected_emotion == "Sad":
    print("💬 AI Avatar: Stay Positive!")

elif detected_emotion == "Happy":
    print("💬 AI Avatar: Great to see you smiling!")

else:
    print("💬 AI Avatar: Emotion Analysis Completed")
