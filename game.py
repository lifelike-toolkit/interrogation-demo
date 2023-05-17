"""Testing character's responses to questions when given a game state context"""
from langchain.llms import LlamaCpp
from lifelike import brain

from setup.build_sequence_tree import llm, retrievalQA

# Initialize Characters
characters = brain.Characters('characters.json')

player = "Player"
character = "Jason William"
character_background = "Jason William is a 20-year old professional software developer. He is extremely egotistical and believes that he is the only rightful heir to his father's fortune. \
    He will not reveal the fact that he killed Emily William. He will also not reveal his debt.\
    He was meant to kill his father so he can take over the inheritance sooner. However, he accidentally killed Emily William instead. "
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
    if new_utterance == "quit":
        break

    conversations.append(CONTEXT, "Player", new_utterance)
    print()
    new_utterance = new_utterance.replace("your", "Jason William's")
    new_utterance = new_utterance.replace("Your", "Jason William's")
    new_utterance = new_utterance.replace("you", "Jason William")
    new_utterance = new_utterance.replace("You", "Jason William")
    # print("Formatted query {}".format(new_utterance)) # Debug TODO remove from final version
    history = retrievalQA.run(new_utterance)
    # If the history string is too long, chances are the question is off-topic
    # if len(history) > 300:
    #     history = "Jason does not want to respond."

    # print("Returned context {}".format(history)) # Debug TODO remove from final version
    conversations.generate(CONTEXT, history, {"Player"})
    