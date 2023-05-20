"""Testing character's responses to questions when given a game state context"""

from setup.logic import conversations, QA_CHAIN
from setup.story import CONVO_CONTEXT, PLAYER_NAME, NPC_NAME

conversations.new(CONVO_CONTEXT, {PLAYER_NAME, NPC_NAME})
conversations.append(CONVO_CONTEXT, NPC_NAME, 'What do you want to ask me, detective?')

# Start chatbot
while True:
    line = conversations.get(CONVO_CONTEXT)["log"][-1]
    speaker = line[0]
    utterance = line[1]
    print(f"{speaker}: {utterance}")
    print()

    new_utterance = input("{}: ".format(PLAYER_NAME))
    if new_utterance == "quit":
        break

    conversations.append(CONVO_CONTEXT, PLAYER_NAME, new_utterance)
    print()
    new_utterance = new_utterance.replace("your", "Jason William's")
    new_utterance = new_utterance.replace("Your", "Jason William's")
    new_utterance = new_utterance.replace("you", "Jason William")
    new_utterance = new_utterance.replace("You", "Jason William")
    # print("Formatted query {}".format(new_utterance)) # Debug TODO remove from final version
    history = QA_CHAIN.run(new_utterance)
    # If the history string is too long, chances are the question is off-topic
    # if len(history) > 300:
    #     history = "Jason does not want to respond."

    # print("Returned context {}".format(history)) # Debug TODO remove from final version
    conversations.generate(CONVO_CONTEXT, history, {PLAYER_NAME})
    