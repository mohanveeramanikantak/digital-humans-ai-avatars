# Voice Interaction System Simulation

import random
import time

print("🎤 Voice Interaction System Started")

time.sleep(1)

commands = [
    "Open Dashboard",
    "Play Music",
    "Check Weather",
    "Start AI Assistant"
]

detected_command = random.choice(commands)

print("🗣 Detected Voice Command:", detected_command)

time.sleep(1)

print("✅ Command Executed Successfully")
