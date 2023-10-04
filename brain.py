
import string
import random
import json
from create_model import response

with open('intents.json') as f:
    intents = json.load(f)


def brain(input_text):
    if input_text.lower().strip(string.punctuation) in intents['opening']['user_messages'] and len(input_text.lower().strip(string.punctuation)):
        return intents['opening']['bot_responses'][random.randrange(0, len(intents['opening']['bot_responses']))]
    elif input_text.lower().strip(string.punctuation) in intents['closing']['user_messages']:
        return intents['closing']['bot_responses'][random.randrange(0, len(intents['closing']['bot_responses']))]
    elif input_text.lower().strip(string.punctuation) in intents['gratitude']['user_messages'] and len(input_text.lower().strip(string.punctuation)):
        return intents['gratitude']['bot_responses'][random.randrange(0, len(intents['gratitude']['bot_responses']))]
    else:
        resp = response(input_text.lower().strip(string.punctuation))
        if resp:
            return resp
        else:
            return intents['confusion']['bot_responses'][random.randrange(0, len(intents['confusion']['bot_responses']))] + ". Please try again."