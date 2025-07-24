# Codsoft.task1
TASK 1
🛠️ Step-by-Step Processing
1. Start the Program
You run the Python file in IDLE. The bot starts with a friendly greeting and waits for user input using input().
user _input = input("You: ").lower()
- This takes what the user types and converts it to lowercase, making the matching easier.
2. Pattern Matching or Conditional Checks
You use either:
- If-Else Statements (for exact matches):
if user_input == "hello":
    print("ChatBot: Hi there!")
- Regular Expressions (for flexible matching):
import re
if re.search(r"\bhello\b|\bhi\b|\bhey\b", user_input):
    print("ChatBot: Hello there!")
- The \b in regex means “word boundary”—this helps avoid matching unwanted fragments like “shellow.”
- | means “or,” so it catches multiple greetings.

3. Generate Response
Once a match is found, you display a response using print():
print("ChatBot: I'm just a bunch of code, but I'm doing great!")


If the input doesn’t match any rule, fallback with:
print("ChatBot: Sorry, I didn't understand that.")



4. Loop Until User Exits
You wrap all this inside a while True: loop, and add a condition to break the loop:
if user_input == "exit":
    print("ChatBot: Catch you later!")
    break


So it keeps talking until the user wants to end the session.

🔁 Full Flow Example
- User types: hello
- Bot matches that to a rule or pattern
- Responds: Hi there! 👋
- Waits for next input
- If user types: exit, the bot says goodbye and ends
