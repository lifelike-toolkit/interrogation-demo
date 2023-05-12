"""Testing character's responses to questions when given a game state context"""
from langchain.llms import LlamaCpp
from lifelike import brain

# Initialize LLM
llm = LlamaCpp(model_path='ggml-model-q4_0.bin', use_mlock=True)

# Initialize Characters
characters = brain.Characters('characters.json')

name1 = "Jason Mann"
name2 = "Peter Barlow"
background1 = "Police detective investigating the murder of Tina Barlow. He suspects Peter Barlow to have murdered Tina. He will not stop until Peter confesses"
background2 = "Tina Barlow's brother. He murdered Tina but is trying to hide it."
CONTEXT = "Jason is interrogating Peter in the police station. Jason is pressured to get Peter to confess to killing Tina."
first_speaker = "Peter Barlow"
first_utterance = "Why was I summoned here?"

characters.add(name1, background1)
characters.add(name2, background2)

# Initialize Conversations
conversations = brain.Conversations('conversations.json', characters, llm)

conversations.new(CONTEXT, {name1, name2})
conversations.append(CONTEXT, first_speaker, first_utterance)


# Start chatbot
counter = 0
while True:
    if counter % 2 == 0:
        print("{}: {}".format(name2, conversations.get(CONTEXT)['log'][-1][1]))
    else:
        print("{}: {}".format(name1, conversations.get(CONTEXT)['log'][-1][1], is_user=True))
    counter += 1
    last_speaker = conversations.get(CONTEXT)['log'][-1][0]
    out = conversations.generate(CONTEXT, {last_speaker})