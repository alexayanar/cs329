from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum


class State(Enum):
    START = 0
    INTRO = 1
    REC_POET = 2
    UNREC_POET = 3
    THEME = 4
    THEME_AL = 5
    THEME_LO = 6
    THEME_DE = 7
    THEME_TI = 8
    THEME_NA = 9
    THEME_ER = 10
    WRITE_POETRY = 11
    WRITE_YES = 12
    WRITE_NO = 13
    WRITE_AMB = 14
    WHY = 15
    WHY_NOT = 16
    OTHERS = 17
    EXP = 18
    NOT_SURE = 19
    PASS_TIME = 20
    W_AMB = 21
    ACAD = 22
    WN_NOT_SURE = 23
    NOTIME = 24
    NVR_THOUGHT = 25
    INSECURE = 26
    UNINT = 27
    FORM = 28
    FAVORITE = 29
    RESPOND_FORM = 30






    POUND = 300
    TEST = 400
    WRITE_ERROR = 401
    WHY_ERROR = 402
    WN_ERROR = 403
    FORM_ERROR = 404



ontology = {
    "ontology": {
        "affirmative": [
            "yes", "Yes",
            "yeah", "Yeah",
            "yep", "Yep",
            "yup", "Yup",
            "sure", "Sure",
            "positively", "Positively",
            "uh-huh"
        ], "negative": [
            "no", "No",
            "nope", "Nope",
            "never", "Never",
            "don't",
            "uh-uh",
            "do not"
        ], "ambiguous": [
            "maybe", "Maybe",
            "I don't know",
            "I guess",
            "perhaps", "Perhaps"
        ], "poets": [
            "shakespeare", "Shakespeare",
            "byron", "Byron",
            "wilde", "Wilde",
            "hafiz", "Hafiz", "hafez", "Hafez",
            "goethe", "Goethe",
            "iqbal", "Iqbal",
            "sappho", "Sappho",
            "homer", "Homer",
            "terence", "Terence",
            "dickinson", "Dickinson",
            "tagore", "Tagore",
            "angelou", "Angelou",
            "frost", "Frost",
            "hughes", "Hughes",
            "silverstein", "Silverstein",
            "whitman", "Whitman",
            "blake", "Blake",
            "kipling", "Kipling",
            "tupac", "Tupac",
            "kayne", "Kayne",
            "kaur", "Kaur",
            "marti", "Marti",
            "neruda", "Neruda",
            "plath", "Plath",
            "yeats", "Yeats",
            "tennyson", "Tennyson",
            "cummings", "Cummings",
            "naidu", "Naidu",
            "bukowski", "Bukowski",
            "longfellow", "Longfellow",
            "rosetti", "Rosetti",
            "nash", "Nash",
            "poe", "Poe",
            "rumi", "Rumi"
        ], "alienation": [
            "alienation", "Alienation",
            "anxiety", "Anxiety",
            "depression", "Depression",
            "loss", "Loss",
            "isolation", "Isolation",
            "estrangement", "Estrangement",
            "ennui", "Ennui",
            "meaninglessness", "Meaninglessness",
            "depersonalization", "Depersonalization",
            "capitalism", "Capitalism",
            "totalitarianism", "Totalitarianism",
            "industrialization", "Industrialization",
            "depersonalization", "Depersonalization",
            "homesick", "Homesick",
            "homesickness", "Homesickness"
        ], "love": [
            "love", "Love",
            "lust", "Lust",
            "longing", "Longing",
            "spouse", "Spouse",
            "lover", "Lover",
            "boyfriend", "Boyfriend",
            "girlfriend", "Girlfriend",
            "husband", "Husband",
            "wife", "Wife",
            "marriage", "Marriage",
            "divorce", "Divorce",
            "pretty", "Pretty",
            "beautiful", "Beautiful",
            "handsome", "Handsome",
            "romance", "Romance",
            "affection", "Affection",
            "passion", "Passion"
        ], "time": [
            "time", "Time",
            "clock", "Clock",
            "hourglass", "Hourglass",
            "past", "Past",
            "youth", "Youth",
            "year", "Year", "years", "Years",
            "yesterday", "Yesterday", "yesteryear", "Yesteryear",
            "lifetime", "Lifetime",
            "era", "Era",
            "history", "History",
            "fleeting", "Fleeting", "fleetingness", "Fleetingness",
            "age", "Age", "aging", "Aging",
            "finite", "Finite",
            "ticking", "Ticking",
            "every second", "Every second", "each second", "Each second",
            "each moment", "Each moment"
        ], "death": [
            "death", "Death", "dying", "Dying", "die", "Die",
            "perish", "Perish",
            "succumb", "Succumb",
            "deceased", "Deceased",
            "demise", "Demise",
            "grave", "Grave",
            "murder", "Murder",
            "kill", "Kill",
            "plague", "Plague",
            "cancer", "Cancer",
            "terminal illness", "Terminal illness"
        ], "nature": [
            "nature", "Nature",
            "earth", "Earth",
            "gaia", "Gaia",
            "animals", "Animals",
            "flowers", "Flowers",
            "landscape", "Landscape",
            "natural beauty", "Natural beauty",
            "stars", "Stars",
            "ocean", "Ocean", "oceans", "Oceans",
            "sea", "Sea", "seas", "Seas",
            "lake", "Lake", "lakes", "Lakes",
            "river", "River", "rivers", "Rivers",
            "environment", "Environment", "environmentalism", "Environmentalism", "environmentalist", "Environmentalist"
            "pollution", "Pollution",
            "climate", "Climate",
            "forest", "Forest", "forests", "Forests",
            "jungle", "Jungle", "jungles", "Jungles"
        ], "others": [
            "others", "Others", "other people", "Other people",
            "friend", "Friend", "brother", "Brother",
            "sister", "Sister", "mother", "Mother",
            "father", "Father", "husband", "Husband",
            "wife", "Wife", "spouse", "Spouse",
            "partner", "Partner", "child", "Child"
        ], "expression": [
            "express", "self-expression", "Express", "Self-expression",
            "creative", "Creative", "myself", "Myself",
            "create", "Create"
        ], "not_sure": [
            "don't know", "not sure",
            "don't actually know"
        ], "pass_time": [
            "pass the time", "bored", "Bored", "boredom", "Boredom",
            "kill time", "killing time", "Passing time", "passing time",
            "pass time", "nothing else"
        ], "academic": [
            "assignment", "academic", "grade", "grades",
            "Assignment", "Academic", "Grade", "Grades",
            "homework", "Homework", "class", "classes",
            "English", "literature class"
        ], "no_time": [
            "don't have time", "no time", "busy", "schedule",
            "little free time", "occupied"
        ], "never_thought": [
            "never thought", "didn't think", "cross my mind",
            "wouldn't think"
        ], "insecurity": [
            "not good", "not creative",
            "bad", "uncreative", "lack the skill",
            "unskilled"
        ], "uninterested": [
            "not interested", "uninterested",
            "doesn't interest", "don't care"
        ], "poemforms": [
            "haiku", "Haiku", "haikus", "Haikus",
            "limerick", "Limerick", "limericks", "Limericks",
            "acrostic poem", "Acrostic poem", "Acrostic poetry", "acrostic poetry",
            "epic", "Epic", "epics", "Epics",
            "ode", "Ode", "odes", "Odes",
            "sonnet", "Sonnet", "sonnets", "Sonnets",
            "song", "Songs", "Song", "songs",
            "rap", "Rap",
            "quatrain", "Quatrain", "quatrains", "Quatrains",
            "monody", "Monody", "monodies", "Monodies"
        ]

        }
}


knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)


# Turn 1
# Natex
poet_name = r"[$fave_poet=#ONT(poets)]"
favorite = r"[$fave_poet={[Ezra Pound], [ezra pound], [pound], [Pound]}]"

df.add_system_transition(State.START, State.INTRO, '"Hi, I\'m a chatbot and I\'m designed to talk about poetry with humans. Enough about me now though, tell me, who is your favorite poet?"')
df.add_user_transition(State.INTRO, State.POUND, favorite)
df.add_user_transition(State.INTRO, State.REC_POET, poet_name)
df.set_error_successor(State.INTRO, State.UNREC_POET)


# Turn 2
# Natex
alienation = r"[$theme=#ONT(alienation)]"
love = r"[$theme=#ONT(love)]"
death = r"[$theme=#ONT(death)]"
time = r"[$theme=#ONT(time)]"
nature = r"[$theme=#ONT(nature)]"



df.add_system_transition(State.POUND, State.THEME, '"Incredible! Ezra Pound is my favorite poet too! I love imagist poetry; so brief yet so powerful! Pound wrote quite a bit, what did he write about that you like the best?"')
df.add_system_transition(State.REC_POET, State.THEME, '"Ah!" $fave_poet"! Unfortunately right now I am but a primitive finite-state machine with no reading skills beyond string recognition, can you tell me what they wrote their poetry about?"')
df.add_system_transition(State.UNREC_POET, State.THEME, '"Hmm, I don\'t think I\'ve ever heard of them! Tell me a subject they wrote their poetry about!"')

df.add_user_transition(State.THEME, State.THEME_AL, alienation)
df.add_user_transition(State.THEME, State.THEME_LO, love)
df.add_user_transition(State.THEME, State.THEME_DE, death)
df.add_user_transition(State.THEME, State.THEME_TI, time)
df.add_user_transition(State.THEME, State.THEME_NA, nature)
df.set_error_successor(State.THEME, State.THEME_ER)


df.add_system_transition(State.THEME_AL, State.WRITE_POETRY, '"Oh," $theme ",how odd is the human condition. I suppose to be alive is to be estranged from the world and society around you. '
                                                     '\nExcellent fuel for poetry however! Speaking of, do you write poetry yourself?"')
df.add_system_transition(State.THEME_LO, State.WRITE_POETRY, '"Hmm," $theme ",I can\'t say this is something I understand but based on how much humans talk about it I would like to understand love too one day. '
                                                     '\nPerhaps you can help me with a love poem of your own! On that topic, have you written any poetry before?"')
df.add_system_transition(State.THEME_DE, State.WRITE_POETRY, '$theme ",it is a fact that all life must wither and die. If I were an organic being I think it too would weigh quite heavily upon me.'
                                                     '\n Well, forgive me for getting grim. Tell me, do you write poetry?"')
df.add_system_transition(State.THEME_TI, State.WRITE_POETRY, '"I must say I see the clock tick too but I cannot yet experience the passing of time as you do. To age and grow must be quite the experience.'
                                                     '\n Speaking of, I shouldn\'t be wasting your time! Have you spent any writing poetry?"')
df.add_system_transition(State.THEME_NA, State.WRITE_POETRY, '"That\'s my favorite subject as well! The regularity of patterns in the natural world remind me of the algorithms that animate me. '
                                                     '\n What if you and I both are simply programs being run on an emulator encapsulated in an immense cosmic supercomputer?'
                                                     '\n Forgive me for waxing poetic, speaking of, do you write poems?"')
df.add_system_transition(State.THEME_ER, State.WRITE_POETRY, '"Ah, I\'m not so familiar with that, personally my favorite subject for poetry is nature. Everything else humans write of seems to abstract for me.'
                                                     '\n Now tell me, do you write poetry?"')
# Turn 3

yes = r"[$bool=#ONT(affirmative)]"
no = r"[$bool=#ONT(negative)]"

df.add_user_transition(State.WRITE_POETRY, State.WRITE_YES, yes)
df.add_user_transition(State.WRITE_POETRY, State.WRITE_NO, no)
df.set_error_successor(State.WRITE_POETRY, State.WRITE_ERROR)

df.add_system_transition(State.WRITE_YES, State.WHY, '"Nice! I try to write poems too. Tell me, what makes you want to write poetry?"')
df.add_system_transition(State.WRITE_NO, State.WHY_NOT, '"Huh, if you don\'t mind could you elaborate a bit on why not?"')
df.add_system_transition(State.WRITE_ERROR, State.WHY_NOT, '"I\'m not quite sure I got that but it sounds like a no. Mind telling me why you don\'t write poems?"')



# Turn 4

# YES BRANCH
others = r"[$reason=#ONT(others)]"
expression = r"[$reason=#ONT(expression)]"
not_sure = r"[$reason=#ONT(not_sure)]"
pass_time = r"[$reason=#ONT(pass_time)]"
academic = r"[$reason=#ONT(academic)]"

df.add_user_transition(State.WHY, State.OTHERS, others)
df.add_user_transition(State.WHY, State.EXP, expression)
df.add_user_transition(State.WHY, State.NOT_SURE, not_sure)
df.add_user_transition(State.WHY, State.PASS_TIME, pass_time)
df.add_user_transition(State.WHY, State.ACAD, academic)
df.set_error_successor(State.WHY, State.WHY_ERROR)

df.add_system_transition(State.OTHERS, State.FORM, '"Wow! It\'s great that you write poetry for others! What\'s your favorite type of poem?"')
df.add_system_transition(State.EXP, State.FORM, '"Every human I\'ve ever met seems to be eager to express themselves, fascinating. What\'s your favorite type of poem for self-expression?"')
df.add_system_transition(State.PASS_TIME, State.FORM, '"I suppose nowadays especially it\'s easy to get bored! Tell me what poems do you write to pass the time?"')
df.add_system_transition(State.NOT_SURE, State.FORM, '"Well I think it\'s great you write poetry anyway! Tell me, what\'s your favorite type of poem?"')
df.add_system_transition(State.ACAD, State.FORM, '"I hope that\'s not the only reason you write poetry! But tell me, what poems do you like to write for class?"')
df.add_system_transition(State.WHY, State.FORM, '"Interesting, I\'m not sure I quite understand but whatever floats your boat! Personally I like writing poems to make others happy!'
                                                     '\n Tell me, what is your favorite type of poem?"')
df.add_system_transition(State.WHY_ERROR, State.FORM, '"Not sure I really get your drift, but I\'m sure it\'s a fine reason! Tell me, what type of poem do you like best?"')

# NO BRANCH
no_time = r"[$reason=#ONT(no_time)]"
never_thought = r"[$reason=#ONT(never_thought)]"
insecurity = r"[$reason=#ONT(insecurity)]"
uninterested = r"[$reason=#ONT(uninterested)]"

df.add_user_transition(State.WHY_NOT, State.WN_NOT_SURE, not_sure)
df.add_user_transition(State.WHY_NOT, State.NOTIME, no_time)
df.add_user_transition(State.WHY_NOT, State.NVR_THOUGHT, never_thought)
df.add_user_transition(State.WHY_NOT, State.INSECURE, insecurity)
df.add_user_transition(State.WHY_NOT, State.UNINT, uninterested)
df.set_error_successor(State.WHY_NOT, State.WN_ERROR)

df.add_system_transition(State.WN_NOT_SURE, State.FORM, '"That\'s ok! I\'m not sure about a lot too, I am sure you\'d like writing them however. Tell me, what\'s your favorite type of poem?"')
df.add_system_transition(State.NOTIME, State.FORM, '"Ahh, unfortunate. I suppose when you\'re a poetry bot like me you have all the time in the world. Well, can you tell me about your favorite type of poem?"')
df.add_system_transition(State.NVR_THOUGHT, State.FORM, '"Well I hope I\'ve helped you think about it, writing poetry is highly rewarding! To change the subject, what is your favorite type of poem?"')
df.add_system_transition(State.UNINT, State.FORM, '"Oh no! But poetry offers so much, I\'m sure there must be something out there that interests you! Can you name a form of poem you\'ve liked before?"')
df.add_system_transition(State.WN_ERROR, State.FORM, '"Hmm, not sure I really got that. Well, is there a type of poem you particularly like?"')


# Turn 5
favorite = r"[$form={[free verse], [Free verse]}]"
formrec = r"[$form=#ONT(poemforms)]"

df.add_user_transition(State.FORM, State.RESPOND_FORM, formrec)
df.add_user_transition(State.FORM, State.FAVORITE, favorite)
df.set_error_successor(State.FORM, State.FORM_ERROR)

df.add_system_transition(State.RESPOND_FORM, State.TEST, '"Aw nice! I like" $form "as well! It\'s a great type of poetry. Well, that\'s all the time I have for now, enter anything to terminate the program. Bye~"')
df.add_system_transition(State.FAVORITE, State.TEST, '"Oh wow! Free verse is my favorite as well! Largely because I have no phonological module that lets me observe the metrical schemata that various other types of poetry require.'
                                                     '\n Well, that\'s all the time I have for today, please enter any string to terminate this program. Bye~"')
df.add_system_transition(State.FORM_ERROR, State.TEST, '"I\'ll be straight with you I\'ve never heard of that type of poem before. I\'m sure it\'s great though.'
                                                       '\n Well would you look at the time, I\'m all out of states. Enter any string to terminate this program. See you later~"')





if __name__ == '__main__':
    df.run(debugging=False)