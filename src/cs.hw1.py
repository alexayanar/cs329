from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum


# TODO: Update the State enum as needed
# questions: how to classify states?
class State(Enum):
    START = 0
    PROMPT = 1
    ERR = 2
    ROUND1 = 3


# TODO: create the ontology as needed
ontology = {
    "ontology": {

        }
}


knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)
#how to change paths based from their answer
#possible to have bank of questions to refer to and keep ticking off? 
df.add_system_transition(State.START, State.PROMPT, '"Today is December 31st, 1999 and we are a few minutes from'
                                                    'midnight, and ultimately, the destruction of computers and '
                                                    'technology because of the y2k bug. I am your computer. '
                                                    'I am sentient and have knowledge of what '
                                                    'the world and its techologies would have looked like two decades'
                                                    'into the future if computers had survived the bug. '
                                                    'Do you understand?"') #starting prompt--further clarification
                                                    #if needed

df.add_user_transition(State.PROMPT, State.ROUND1, '')
df.set_error_successor(State.PROMPT, State.ERR)
# TODO: create your own dialogue manager


df.run(debugging=False)

# dictionaries + reg expressions
res.re_yn = re.compile(r'(?:\s|^)(yes|yeah)|(no|not really)(?:\s|,|\.|$)')
