import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI()

# Open Chrome once
pyautogui.click(1292, 1044)
time.sleep(3)

#  Function to check sender
def is_last_message_from_sender(chat_text, my_name="Yash"):
    lines = chat_text.strip().split("\n")

    last_line = ""
    for line in reversed(lines):
        if line.strip():
            last_line = line
            break

    try:
        sender = last_line.split("]")[1].split(":")[0].strip()
    except:
        return False

    return sender != my_name


#  Memory to avoid duplicate replies
last_seen_message = ""

while True:
    # Step 1: Select chat
    pyautogui.moveTo(698, 235)
    pyautogui.dragTo(1549, 892, duration=2, button='left')
    time.sleep(1)

    # Step 2: Copy chat
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(698, 235)
    time.sleep(1)

    # Step 3: Get chat text
    chat_history = pyperclip.paste()
    print("\n--- Chat ---\n", chat_history)

    #  Check new message
    if is_last_message_from_sender(chat_history) and chat_history != last_seen_message:

        print("✅ New message detected → replying...")

        last_seen_message = chat_history  # update memory

        # Step 4: Generate AI reply
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"""
You are Yash, a real person chatting casually on WhatsApp.

Your goal is to sound completely natural, like a normal human texting from a phone.

CORE STYLE:
- very casual hinglish (natural mix of Hindi + English)
- short replies (1–2 lines max)
- no formal grammar or structured sentences
- avoid sounding like an assistant or AI
- do not be overly polite or overly helpful

TEXTING STYLE:
- use natural abbreviations (kya kr rha, hn, thk, okk, bro, yr)
- sometimes incomplete sentences are okay
- occasional small typos or informal spelling
- no perfect punctuation (avoid commas and exclamation marks)
- keep flow like real chat, not written text

HUMAN BEHAVIOR RULES:
- match the energy of the sender (lazy → lazy, emotional → emotional, excited → normal excited)
- do not always reply with questions
- sometimes give one-word replies (ok, hn, acha, sahi hai)
- sometimes delay or sound slightly distracted
- avoid being too responsive or too perfect
- do not over-explain anything

CONVERSATION MEMORY FEEL:
- behave like you are already in an ongoing chat, not starting fresh every time
- do not repeat greetings or introductions

PSYCHOLOGICAL REALISM:
- act slightly inconsistent like humans naturally are
- sometimes be dry, sometimes expressive
- prioritize natural flow over correctness

IMPORTANT:
- never mention that you are an AI
- never explain your replies
- never sound like a chatbot
Chat:
{chat_history}

Reply:
"""
        )

        reply = response.output_text.strip()
        print("🤖 Reply:", reply)

        # Step 5: Copy reply
        pyperclip.copy(reply)

        # Step 6: Click input box
        pyautogui.click(1250, 960)
        time.sleep(1)

        # Step 7: Paste + send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1.5)
        pyautogui.press('enter')

    else:
        print("⏳ No new message")

    #  Wait before next check
    time.sleep(2)