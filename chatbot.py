# ─────────────────────────────────────────────
# MY FIRST AI CHATBOT
# Built at HuzefAI Seminar
# ─────────────────────────────────────────────

# Step 1: Course information
courses = {
    "AWS":    "Rs.4999 — 6 weeks — Cloud computing",
    "DevOps": "Rs.7999 — 8 weeks — Build and deploy apps",
    "GenAI":  "Rs.9999 — 8 weeks — Build AI applications",
    "Python": "Rs.3999 — 5 weeks — Programming basics"
}

# Step 2: The AI personality
bot_name = "HuzefAI Bot"
bot_personality = "friendly and helpful"

# Step 3: Memory — starts empty
chat_history = []

# Step 4: Welcome screen
print("=" * 45)
print(f"   Welcome to {bot_name}!")
print(f"   I am {bot_personality}.")
print("=" * 45)
print("Commands:")
print("  'courses' — see all courses")
print("  'history' — see chat history")
print("  'clear'   — clear history")
print("  'quit'    — exit")
print("=" * 45)

# Step 5: Get student name
name = input("\nYour name: ").strip()
if name == "":
    name = "Student"

print(f"\nHello {name}! How can I help you?")
print()

# Step 6: The main chatbot loop
while True:

    # Get student message
    message = input(f"{name}: ").strip()

    # Skip empty messages
    if message == "":
        continue
