
# import required libraries
import random

# define bot's responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi! How can I assist you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day."],
    "default": ["I'm sorry, I didn't understand what you meant. Can you please rephrase?", 
                "I'm not sure what you mean. Could you please provide more context?"]
}

# define function to generate bot's response
def get_bot_response(user_message):
    if user_message in responses:
        return random.choice(responses[user_message])
    else:
        return random.choice(responses["default"])

# start chatting with the bot
while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        break
    bot_response = get_bot_response(user_message.lower())
    print("Bot: " + bot_response)

'''



from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot', read_only=True)
trainer = ListTrainer(bot)

# Training data
trainer.train([
    "Hi, can I help you",
    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",
    "Where do you operate?",
    "We operate from Singapore",
    "What payment methods do you accept?",
    "We accept debit cards and major credit cards",
    "I would like to speak to your customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
])

trainer.train([
    "What payment methods do you offer?",
    "We accept debit cards and major credit cards",
    "How to contact customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
])

# Chat loop
while True:
    request = input('You: ')
    if request.lower() == 'ok':
        print('Bot: Bye!')
        break
    else:
        response = bot.get_response(request)
        print('Bot:', response)

        '''