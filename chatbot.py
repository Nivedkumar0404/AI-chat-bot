import os
from dotenv import load_dotenv
from anthropic import Anthropic

# load the secret key from .env
load_dotenv()
client = Anthropic()

# the conversation list = the memory
conversation = []

print("Study Assistant ready! Type 'quit' to exit.\n")

while True:
    # get the user's message
    user_input = input("You: ")

    # let the user exit
    if user_input == "quit":
        print("Goodbye! Keep up the great work.")
        break

    # add the user's message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # send the whole conversation to Claude, with a system prompt
    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=500,
        system="You are a friendly study assistant who helps students learn programming. Keep explanations clear and encouraging.",
        messages=conversation
    )

    # get Claude's reply
    reply = message.content[0].text

    # show it
    print("Claude: " + reply + "\n")

    # add Claude's reply to the conversation so it's remembered
    conversation.append({"role": "assistant", "content": reply})