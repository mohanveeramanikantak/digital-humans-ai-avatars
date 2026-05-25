# Facial Recognition Simulation

import random

users = ["Mohan", "Alex", "Sophia", "David"]

recognized_user = random.choice(users)

confidence = random.randint(80, 99)

print("📷 Scanning Face...")

print("👤 Recognized User:", recognized_user)
print("🔍 Confidence:", str(confidence) + "%")

if confidence > 90:
    print("✅ Identity Verified")
else:
    print("⚠️ Verification Weak - Retry Scan")
