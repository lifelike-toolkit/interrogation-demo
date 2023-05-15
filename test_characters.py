"""Testing character's responses to questions when given a game state context"""
from langchain.llms import LlamaCpp
from lifelike import brain

from setup.build_sequence_tree import llm, retrievalQA

# Initialize Characters
characters = brain.Characters('characters.json')

player = "Player"
character = "Jason William"
character_background = "Jason William is a software engineer. He is extremely egotistical and believes that he is the only rightful heir to his father's fortune. \
    Jason is trying to hide the fact that he killed Emily because Jason knows that he will be executed if the truth comes out.\
    Jason meant to kill his father so he can take over the inheritance sooner. However, he accidentally killed his sister Emily William instead. "
CONTEXT = "Player is interrogating Jason about the death of Emily William in the Kingston police station in Kingston, Ontario, Canada."
first_speaker = character

characters.add(player, "")
characters.add(character, character_background)

# Initialize Conversations
conversations = brain.Conversations('conversations.json', characters, llm)

conversations.new(CONTEXT, {player, character})
conversations.append(CONTEXT, character, 'What do you want to ask me, detective?')

# Start chatbot
while True:
    line = conversations.get(CONTEXT)["log"][-1]
    speaker = line[0]
    utterance = line[1]
    print(f"{speaker}: {utterance}")

    new_utterance = input("Player: ")
    conversations.append(CONTEXT, "Player", new_utterance)
    print()
    history = retrievalQA.run(new_utterance)
    conversations.generate(CONTEXT, history, {"Player"})
    