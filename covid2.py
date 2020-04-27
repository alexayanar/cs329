from emora_stdm import KnowledgeBase, DialogueFlow, Macro, NatexNLG, NatexNLU
from enum import Enum, auto
from covid import Covid

covid = Covid()


########################################
# STATES
# TODO: Update State enum as needed

class State(Enum):
    START = 0
    INTRO = 1
    UPDATES = 2
    STRESS2 = 3
    INHALE = 4
    VISION = 5
    STRESSF = 6
    FEEL = 7
    INHALEF = 8
    VISIONF = 9
    NOGROUND = 10
    HYGIENE = 11
    GLOVES = 12
    HYGIENEF = 13
    SUSPECT = 14
    SUSPECTF = 15
    DIAGNOSE = 16
    ABGROUND = 17
    SAD = 18
    SADF = 19
    FRIENDS = 20
    FRIENDSF = 21
    FADVICE = 22
    FADVICENO = 23
    STRESS = 24
    STRESS1 = 25
    HEAR = 26
    FEELF = 27
    VACCINE = 28
    VACCINEF = 29
    WASHING = 30
    WASHINGF = 31
    ACTIVITY = 32
    GARDEN = 33
    GARDENF = 34
    SMELL = 35
    HEARF = 36
    TASTE = 37
    SMELLF = 38
    TASTEF = 39
    COMGROUND = 40
    FUTURE = auto()
    TRANSITION = auto()
    CURRENT = auto()
    ACTIVITIES = auto()
    KEMP = auto()
    a0 = auto()
    b0 = auto()
    a1 = auto()
    a2 = auto()
    a3 = auto()
    a4 = auto()
    a6 = auto()
    a8 = auto()
    a9 = auto()
    a10 = auto()
    a11 = auto()
    a12 = auto()
    a13 = auto()
    a14 = auto()
    a15 = auto()
    a16 = auto()
    a17 = auto()
    a18 = auto()
    a19 = auto()
    a20 = auto()
    a21 = auto()
    t0 = auto()
    t1 = auto()
    t2 = auto()
    t3 = auto()
    t4 = auto()
    t5 = auto()
    t6 = auto()
    t7 = auto()
    t8 = auto()
    t9 = auto()
    t10 = auto()
    t11 = auto()
    t12 = auto()
    t13 = auto()
    t14 = auto()
    t15 = auto()
    t16 = auto()
    t17 = auto()
    t18 = auto()
    t19 = auto()
    t20 = auto()
    t21 = auto()
    t22 = auto()
    t23 = auto()
    t24 = auto()
    t25 = auto()
    t26 = auto()
    t27 = auto()
    t28 = auto()
    t29 = auto()
    t30 = auto()
    t31 = auto()
    t32 = auto()
    t33 = auto()
    t34 = auto()
    t35 = auto()
    t36 = auto()
    t37 = auto()
    t38 = auto()
    t39 = auto()
    t40 = auto()
    b1 = auto()
    b2 = auto()
    b3 = auto()
    b4 = auto()
    b5 = auto()
    b6 = auto()
    b7 = auto()
    b8 = auto()
    b9 = auto()
    b10 = auto()
    b11 = auto()
    b12 = auto()
    b13 = auto()
    b14 = auto()
    b15 = auto()
    b16 = auto()
    b17 = auto()
    b18 = auto()
    b19 = auto()
    b20 = auto()
    b21 = auto()
    b22 = auto()
    b23 = auto()
    b24 = auto()
    b25 = auto()
    b26 = auto()
    b27 = auto()
    b28 = auto()
    b29 = auto()
    b30 = auto()
    b31 = auto()
    b32 = auto()
    b33 = auto()
    b34 = auto()
    b35 = auto()
    b36 = auto()
    b37 = auto()
    b38 = auto()
    b39 = auto()
    b40 = auto()
    b41 = auto()
    b42 = auto()
    b43 = auto()
    b44 = auto()
    b45 = auto()
    b46 = auto()
    b47 = auto()
    b48 = auto()
    b49 = auto()
    b50 = auto()
    b51 = auto()
    b52 = auto()
    b53 = auto()
    b54 = auto()
    b55 = auto()
    b56 = auto()
    b57 = auto()
    c0 = auto()
    c1 = auto()
    c2 = auto()
    c3 = auto()
    c4 = auto()
    c5 = auto()
    c6 = auto()
    c7 = auto()
    c8 = auto()
    c9 = auto()
    c10 = auto()
    c11 = auto()
    c12 = auto()
    c13 = auto()
    c14 = auto()
    c15 = auto()
    c16 = auto()
    c17 = auto()
    d0 = auto()
    d1 = auto()
    d2 = auto()
    d3 = auto()
    d4 = auto()
    d5 = auto()
    d6 = auto()
    d7 = auto()
    d8 = auto()
    d9 = auto()
    d10 = auto()
    d11 = auto()
    d12 = auto()
    d13 = auto()
    d14 = auto()
    d15 = auto()
    d16 = auto()
    d17 = auto()
    d18 = auto()
    d19 = auto()
    d20 = auto()
    e0 = auto()
    e1 = auto()
    e2 = auto()
    e3 = auto()
    e4 = auto()
    e5 = auto()
    e6 = auto()
    e7 = auto()
    e8 = auto()
    e9 = auto()
    e10 = auto()


    PIVOT1 = 200
    TEST = 201
    ERR1 = auto()
    STRESS3 = auto()


#########################################
# ONTOLOGY
# TODO: Update Ontology as needed

ontology = {

    "ontology": {
        "yes": [
            "yeah",
            "yep",
            "yes",
            "sure",
            "definitely",
            "yup",
            "ok",
            "of course",
            "indeed",
            "cool",
            "aight",
            "alright",
            "yea",
            "sure"
        ], "no": [
            "no",
            "nope",
            "not really",
            "don\'t",
            "not",
            "nah",
            "something else"
        ], "indifferent": [
            "meh",
            "maybe",
            "perhaps"
        ], "updates": [
            "update", "updates",
            "how many",
            "cases",
            "number of"
        ], "stress": [
            "stress", "stressed",
            "pressure"
        ], "hygiene": [
            "cleanliness", "hygiene"
        ], "test": [
            "test"
        ], "gloves": [
            "gloves"
        ], "sad": [
            "sad",
            "depressed",
            "feeling blue"
        ], "unsure": [
            "I dont know",
            "not sure",
            "dunno",
            "dont know for sure",
            "i don't know",
            "i dont know", "i can't say",
            "i cant say"
        ], "quit": [
            "quit",
            "dont feel like it",
            "dont wanna",
            "dont feel like doing this",
            "dont want to do this",
            "anymore"
        ], "vaccine": [
            "vaccine",
            "vaccination"
        ], "washing": [
            "wash",
            "washing",
            "handwashing",
            "hand washing",
            "hand-washing",
            "hands clean",
            "clean hands",
            "hand sanitizer"
        ], "gardening": [
            "garden",
            "gardening"
        ], "romance": [
            "romance",
            "romantic",
            "love"
        ], "absurdist": [
            "surreal",
            "whimsical"
        ], "action": [
            "action",
            "fighting",
            "fast"
        ], "adventure": [
            "adventure",
            "adventurous"
        ], "comedy": [
            "comedy",
            "funny",
            "laugh",
            "laughs"
        ], "crime": [
            "crime",
            "criminals",
            "law"
        ], "drama": [
            "drama",
            "dramatic",
            "telenovelas",
            "kpop"
        ], "fantasy": [
            "fantasy",
            "magical",
            "magic",
            "fairy tales"
        ], "historical": [
            "historical",
            "history",
            "non-fiction",
            "true story"
        ], "mystery": [
            "mystery",
            "mysterious",
            "cryptic",
            "curious",
            "mystifying",
            "puzzle",
            "puzzling",
            "strange"
        ], "philosophical": [
            "philosophical",
            "philosophy",
            "think"
        ], "political": [
            "political",
            "politics",
            "governments"
        ], "satire": [
            "satire",
            "satirical",
            "ironic",
            "irony",
            "parody"
        ], "science fiction": [
            "science fiction",
            "sci-fi"
        ], "thriller": [
            "thriller",
            "scary"
        ], "western": [
            "western",
            "old west",
            "cowboy",
            "desert"
        ], "kids": [
            "kids",
            "children",
            "family",
            "innocent"
        ], "indoor": [
            "read", "reading",
            "solving", "solve", "puzzles",
            "sudoku", "wordcross", "paint",
            "drink", "drinking", "music",
            "video", "games", "gaming", "animal crossing",
            "switch", "playlist", "playlists",
            "cooking", "cook", "baking", "bake",
            "filming", "editing", "edit", "film",
            "photography", "photographs", "photos",
            "photo", "photograph", "pictures", "picture",
            "learning", "learn", "tik tok", "watching",
            "twitter", "tweet", "tweeting", "youtube",
            "social media", "instagram", "ig", "insta",
            "gram", "working", "work", "scroll",
            "scrolling", "snapchat", "snap", "snapchatting",
            "snapping", "meditation", "journaling", "journal",
            "word", "searches", "puzzle", "essential oils",
            "aromatherapy", "diffusing", "make", "making",
            "lego", "legos", "embroidery", "knit", "knitting",
            "crotchet", "crotcheting", "yarn", "sewing", "sew",
            "netflix", "shows", "movies", "movie", "series",
            "watch", "binge", "see", "seeing", "crafts", "crafting"
        ], "outside": [
            "skateboarding", "skateboard",
            "skate", "skating",
            "rollerskating", "rollerskate",
            "gardening", "garden",
            "suntanning", "suntan", "tan", "tanning",
            "drive", "driving", "yoga", "plant", "plants",
            "planting", "yard", "walking", "walk", "run",
            "running", "bike", "biking", "mountains", "mountain",
            "hiking", "hike", "nature", "exercise", "riding",
            "sun", "rays", "pruning", "planting", "sports",
            "soccer", "basketball", "tennis", "take", "taking",
            "park", "parks", "lake", "trees", "stroll", "strolling"
        ], "nooutdoor": [
            "not enough", "no space",
            "city", "no", "not", "small", "little", "crowded"
        ], "quarantine": [
            "quarantine", "self-isolation", "social distancing",
            "government", "order", "orders"
        ], "go-out": [
            "going out", "club",
            "clubbing", "bar", "party", "parties",
            "dancing", "dance", "drink", "drinking", "dj",
            "movies", "bars", "movie", "cinema", "theater",
            "restaurants", "restaurant", "go out", "eat",
            "eating", "food", "order", "celebrate",
            "celebrating", "graduation", "graduating",
            "dinners", "dinner", "birthday", "birthdays"
        ], "friends": [
            "hang out", "chill", "see my friends",
            "see friends", "hit up", "my friends",
            "friends", "see", "hanging out", "friend",
            "family", "extended"
        ], "current": [  # takes you to current branch
            "current life", "quarantine"
        ], "normal": [
            "normalcy", "normal", "routine", "go back",
            "routines"
        ], "work": [
            "work", "working", "job", "jobs", "employed",
            "unemployed", "finding", "unemployment"
        ], "no-masks": [
            "masks", "gloves", "pre-cautions", "mask"
        ], "outofhouse": [
            "leave", "get out", "house"
        ], "travel": [
            "travel", "visit", "go see", "airplane", "train",
            "mexico", "go to"
        ], "consume": [
            "haircut", "cut", "store", "stores", "non-essential",
            "businesses", "boutiques", "boutique", "shop", "shopping",
            "buy", "buying"
        ], "nature": [
            "hike", "park", "nature", "outdoors", "picnic", "parks",
            "bbq", "barbecue", "swimming", "swim", "pool", "lake",
            "mountains", "hiking", "camp", "camping"
        ], "partner": [
            "girlfriend", "boo", "partner", "boyfriend", "fiancee", "fiance",
            "husband", "wife"
        ], "future": [  # takes you to future branch
            "future", "happen", "happening", "end"
        ], "activities": [  # suggestions branch
            "activities", "suggestions", "activity",
            "bored", "boredom", "anything to do", "nothing to do"
        ], "pandemic": [
            "pandemic", "cautious", "coronavirus", "covid", "covid-19", "covid19",
            "no end", "quarantine", "social distancing", "social distance", "forever",
            "disease", "germs", "flu", "virus", "death", "sickness", "death toll",
            "sick", "opening", "too soon", "open", "reopen", "re-open"
        ], "school": [
            "class", "classes", "school", "college", "university",
            "graduating", "graduation", "graduate",
        ], "xenophobia": [
            "xenophobia", "violence", "racism", "asians", "asian",
            "china", "chinese"
        ], "healthcare": [
            "healthcare", "hospitals", "medicare", "medicaid",
            "unaffordable", "bills", "not enough", "shortages",
            "inadequate", "health", "nurses", "nurse", "doctors",
            "doctor", "expensive", "testing", "tests"
        ], "capitalism": [
            "capitalism", "inequality", "healing", "slow down",
            "capitalists", "society", "homeless", "homelessness",
            "welfare", "government", "shortcomings", "politicians",
            "businesses", "bail", "stimulus", "checks", "bills",
            "rent"
        ], "transition": [  # transition branch
            "eviction", "evicted", "online classes", "student",
            "semester", "online", "laid off", "fired", "quit",
            "unemployed", "adjusting", "school", "class",
            "classes", "university", "universities", "job",
            "transition", "transitioning", "transitioned",
            "adjusted"
        ], "positive": [
            "good", "well", "okay", "ok",
            "nice", "great", "excellent", "excellent",
            "super", "healthy", "fine", "well rested",
            "peaceful", "sleep", "less stress", "calm",
            "quiet", "on top of it", "on time",
            "economy", "economics", "employment", "business",
            "normal", "normalcy"
        ], "negative": [
            "bad", "not well", "eh", "poor", "poorly",
            "challenging", "challenged", "detrimental",
            "unhealthy", "terrible", "distressed",
            "unfortunate", "distressing", "pathetic",
            "crappy", "crap", "substandard", "sucks", "leave",
            "anxious", "tired", "overwhelmed", "restless",
            "exhausted", "stressed", "anxiety", "stress",
            "so much", "too much", "procrastinating",
            "procrastinated", "procrastinate",
            "death toll", "death", "short", "short lived",
            "idiot", "short-sighted", "inconsiderate",
            "ruling class", "dangerous", "reckless",
            "die"
        ], "grounding": [
            "grounding excercise", "yes", "breathe",
            "yes", "yeah", "yup", "yea", "ya", "sure",
            "grounding"
        ], "kemp": [
            "kemp", "governer", "georgia"
        ]

    }
}

##################################
# MAIN METHOD

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

updates = r"[$response=#ONT(updates)]"
stress = r"[$response=#ONT(stress)]"
test = r"[$response=#ONT(test)]"
hygiene = r"[$response=#ONT(hygiene)]"
no = r"[$response=#ONT(no)]"
yes = r"[$response=#ONT(yes)]"
gloves = r"[$response=#ONT(gloves)]"
suspect_old = r"[$response=#ONT(suspect)]"
activities = r"[$response=#ONT(activities)]"
current = r"[$response=#ONT(current)]"
future = r"[$response=#ONT(future)]"
transition = r"[$response=#ONT(transition)]"
kemp = r"[$response=#ONT(kemp)]"

suspect = NatexNLU(
    '{[i {think, believe, feel like} i {caught, got, have, contracted} {coronavirus, COVID, CoViD, covid}], '
    '[i {might, may} have {coronavirus, COVID, CoViD, covid}]}')

quit = NatexNLU('[dont] [{feel, wanna, want to}] [this]')
sad = r"[$response=#ONT(sad)]"
friends = r"[$response=#ONT(friends)]"
unsure = r"[$response=#ONT(unsure)]"
vaccine = r"[$response=#ONT(vaccine)]"
washing = r"[$response=#ONT(washing)]"
gardening = r"[$response=#ONT(gardening)]"

actCases = str(covid.get_total_active_cases())
recCases = str(covid.get_total_recovered())
deaths = str(covid.get_total_deaths())

# err = NatexNLG('[!{Hmm, Huh}, could you say that again`?`]')

df.add_system_transition(State.START, State.INTRO,
                         '"Hi! I\'m Qbot, your friend in quarantine! What would you like to talk about?"')

df.add_user_transition(State.INTRO, State.UPDATES, updates)
df.add_user_transition(State.INTRO, State.STRESS, stress)
df.add_user_transition(State.INTRO, State.HYGIENE, hygiene)
df.add_user_transition(State.INTRO, State.SUSPECT, suspect)
df.add_user_transition(State.INTRO, State.SAD, sad)
df.add_user_transition(State.INTRO, State.VACCINE, vaccine)
df.add_user_transition(State.INTRO, State.ACTIVITY, activities)
df.add_user_transition(State.INTRO, State.CURRENT, current)
df.add_user_transition(State.INTRO, State.FUTURE, future)
df.add_user_transition(State.INTRO, State.TRANSITION, transition)
df.add_user_transition(State.INTRO, State.KEMP, kemp)
# one branch for what can you do
# another grounding exercise
# practical advice for stress at home


df.set_error_successor(State.INTRO, State.ERR1)

df.add_system_transition(State.ERR1, State.INTRO, NatexNLG('[!{Hmm, Huh, Uhh, Mmm}, sorry I didn`\'`t get that, '
                                                           'could you {rephrase that, say that again}`?`]'))

df.add_system_transition(State.UPDATES, State.INTRO, '"As of now, there are "' + actCases + '" confirmed and active '
                                                    'cases of COVID-19 in the world,"' + recCases + '"recoveries, and"'
                                                    + deaths + '" deaths, \n I sure hope you\'re staying '
                                                    'safe out there! What else can I help with?"')

df.add_system_transition(State.VACCINE, State.VACCINEF, '"Unforuntately, as of now there is no vaccine for SARS-CoV, '
                                                        'would you like some hygiene tips for staying healthy \n '
                                                        'in the mean time?"')

df.add_user_transition(State.VACCINEF, State.HYGIENE, yes)
df.add_user_transition(State.VACCINEF, State.PIVOT1, no)

df.add_system_transition(State.STRESS, State.STRESS1,'"I understand, life in quarantine is not easy. '
                                                     'What\'s making you feel stressed right now?"')

df.add_user_transition(State.STRESS1, State.STRESS2, unsure)
df.add_user_transition(State.STRESS1, State.STRESS3, test)

df.add_system_transition(State.STRESS2, State.STRESSF,
                         '"Lot\'s of things can be causing stress, it\'s ok to not know '
                         'but it\'s still good to acknowledge it! \n '
                         'Would you like to do a grounding exercise with me?"')

df.add_user_transition(State.STRESSF, State.INHALE, yes)
df.add_user_transition(State.STRESSF, State.NOGROUND, no)

df.add_system_transition(State.INHALE, State.INHALEF,
                         '"Let\'s take five deep breaths, notice how your lungs and diaphragm '
                         'expand upon inhaling, and contract while exhaling. Take your time \n '
                         'and tell me when you\'re done."')
df.add_user_transition(State.INHALEF, State.VISION, test)

df.add_system_transition(State.VISION, State.VISIONF,
                         '"Now, look around you and tell me something you can see around you."')
df.add_user_transition(State.VISIONF, State.FEEL, '[$thing=#POS(noun)]')
df.add_user_transition(State.VISIONF, State.ABGROUND, quit)

df.add_system_transition(State.FEEL, State.FEELF,
                         '$thing", how pretty, now tell me, what\'s something around you that you can '
                         'feel with your hands? Describe it\'s texture."')
df.add_user_transition(State.FEELF, State.HEAR, '[$thing=#POS(noun)]')
df.add_user_transition(State.FEELF, State.ABGROUND, quit)

df.add_system_transition(State.HEAR, State.HEARF,
                         '"Excellent" $thing "texture. Now, what is something you can currently hear in the '
                         'background?"')
df.add_user_transition(State.HEARF, State.SMELL, '[$thing=#POS(noun)]')
df.add_user_transition(State.HEARF, State.ABGROUND, quit)

df.add_system_transition(State.SMELL, State.SMELLF,
                         '"Ah yes the sound of" $thing ", that\'s a good answer! Close your eyes and breathe '
                         'through your nose. Tell me what you can smell right now."')
df.add_user_transition(State.SMELLF, State.ABGROUND, quit)
df.add_user_transition(State.SMELLF, State.TASTE, '[$thing=#POS(noun)]')

df.add_system_transition(State.TASTE, State.TASTEF,
                         '"Nice! Just one more, focus on something you\'ve tasted recently, what was it?"')
df.add_user_transition(State.TASTEF, State.ABGROUND, quit)
df.add_user_transition(State.TASTEF, State.COMGROUND, '[$thing=#POS(noun)]')

df.add_system_transition(State.COMGROUND, State.INTRO,
                         '"Mmm," $thing "! I hope you\'re feeling a little calmer now. Are there any activities that '
                         'you\'ve been doing to help you cope with stress?"')

# todo finish the five senses exercise
# todo expand stress dialogue paths

df.add_system_transition(State.NOGROUND, State.INTRO,
                         '"That\'s fine, these don\'t work for everyone! What else can I help you with?"')
# Let's do a grounding exercise, let's take a moment and name one thing from each of your senses
# Take 10 deep breaths

df.add_system_transition(State.ABGROUND, State.INTRO,
                         '"No problem, we can try again some other time, what\'s on your mind?"')

df.add_system_transition(State.HYGIENE, State.HYGIENEF,
                         '"Maintaining hygiene is important usually but especially so now. Are there any specific '
                         'things you\'d like to talk about?"')
df.add_user_transition(State.HYGIENEF, State.GLOVES, gloves)
df.add_user_transition(State.HYGIENEF, State.WASHING, washing)

df.add_system_transition(State.WASHING, State.WASHINGF,
                         '"To kill all germs on your hands, make sure to wash your hands with soap and warm water '
                         'for twenty seconds, \n'
                         'remember to scrub underneath your fingernails and the backs of your hands as well. Only '
                         'use hand sanitizer if you do not have soap and water immediately accessible."')

df.add_system_transition(State.GLOVES, State.INTRO,
                         '"Unless you\'re a medical worker, the CDC does recommend wearing gloves to protect '
                         'yourself from Coronavirus. Any more hygiene questions?"')
# todo expand on this

df.add_system_transition(State.SUSPECT, State.SUSPECTF,
                         '"Oh my, that\'s not good. Have you come into contact with anyone you suspect or '
                         'know to have been infected?"')
df.add_user_transition(State.SUSPECTF, State.DIAGNOSE, yes)

df.add_system_transition(State.DIAGNOSE, State.INTRO,
                         '"I highly recommend you isolate yourself right now. Have you been experiencing a '
                         'fever, dry cough, fatigue, or any other flu-like symptoms?"')
# todo complete diagnose paths

df.add_system_transition(State.SAD, State.SADF,
                         '"It is perfectly normal to feel sad during a time like this, is there something in '
                         'particular you\'re feeling blue about?"')
df.add_user_transition(State.SADF, State.FRIENDS, friends)

df.add_system_transition(State.FRIENDS, State.FRIENDSF,
                         '"That sucks! I\'m sure it must be lonely for you, can I offer some pointers on '
                         'how to stay connected?"')
df.add_user_transition(State.FRIENDSF, State.FADVICE, yes)

df.add_system_transition(State.FADVICE, State.INTRO,
                         '"Texting may feel less engaging, try playing an online game like chess or Settlers '
                         'that could promote more interactive conversation"')

df.add_system_transition(State.ACTIVITY, State.t0, '"Would you like to hear some suggestions of fun '
                                                   'activities to try?"')

df.add_user_transition(State.t0, State.t1, r"[#ONT(yes)]")
df.add_user_transition(State.t0, State.a0, r"[#ONT(no)]")
df.set_error_successor(State.t0, State.a1)

df.add_system_transition(State.t1, State.t2, '"You should try making some focaccia bread! I recommend topping it with '
                                             'roasted red pepper and garlic. Would you like to hear another '
                                             'suggestion?"')
df.add_system_transition(State.a0, State.INTRO, '"One and done, huh? I hope you do bake! Baking helps me calm down, \n'
                                                'what are some things that help calm you down?"')
df.add_system_transition(State.a1, State.INTRO, '"I won\'t keep throwing these at you, but I hope you try it! \n'
                                                'Baking keeps me calm. '
                                                'Do you have anything on your mind?"')

df.add_user_transition(State.t2, State.t3, r"[#ONT(yes)]")
df.add_user_transition(State.t2, State.a4, r"[#ONT(no)]")
df.set_error_successor(State.t2, State.a6)

df.add_system_transition(State.t3, State.t4, '"I think it\'d be really fun to do a picnic. If you don\'t have your '
                                             'own private outdoor space, try one inside! Especially using spiced '
                                             'fruit--so fresh. Would you like to hear another suggestion?"')
df.add_system_transition(State.a4, State.a2, '"I hope the fresh fruit didn\'t cause the disinterest! \n'
                                             'Or is it something else? Do you have something on your mind?"')
df.add_system_transition(State.a6, State.a3, '"I could keep going all day! But I won\'t- is there something '
                                             'weighing on you?"')

df.add_user_transition(State.t4, State.t5, r"[#ONT(yes)]")
df.add_user_transition(State.t4, State.a8, r"[#ONT(no)]")
df.set_error_successor(State.t4, State.a9)

df.add_system_transition(State.t5, State.t6, '"I\'ve had a movie night already--what if you try that? I\'ll even '
                                             'help suggest a movie. \n What kind of genre do you like?"')
df.add_system_transition(State.a8, State.a2, '"Maxed out already, huh? That\'s okay. Is there something weighing'
                                             ' on you?"')
df.add_system_transition(State.a9, State.a3, '"I could keep going all day! But I\'ll spare you. Is there a chance'
                                             ' that something else is \n weighing on you?"')

df.add_user_transition(State.t6, State.t7, r"[#ONT(absurdist)]")
df.add_user_transition(State.t6, State.t8, r"[#ONT(action)]")
df.add_user_transition(State.t6, State.t9, r"[#ONT(adventure)]")
df.add_user_transition(State.t6, State.t10, r"[#ONT(comedy)]")
df.add_user_transition(State.t6, State.t11, r"[#ONT(crime)]")
df.add_user_transition(State.t6, State.t12, r"[#ONT(drama)]")
df.add_user_transition(State.t6, State.t13, r"[#ONT(fantasy)]")
df.add_user_transition(State.t6, State.t14, r"[#ONT(historical)]")
df.add_user_transition(State.t6, State.t15, r"[#ONT(horror)]")
df.add_user_transition(State.t6, State.t16, r"[#ONT(magical realism)]")
df.add_user_transition(State.t6, State.t17, r"[#ONT(mystery)]")
df.add_user_transition(State.t6, State.t19, r"[#ONT(philosophical)]")
df.add_user_transition(State.t6, State.t20, r"[#ONT(political)]")
df.add_user_transition(State.t6, State.t21, r"[#ONT(romance)]")
df.add_user_transition(State.t6, State.t23, r"[#ONT(satire)]")
df.add_user_transition(State.t6, State.t24, r"[#ONT(science fiction)]")
df.add_user_transition(State.t6, State.t25, r"[#ONT(thriller)]")
df.add_user_transition(State.t6, State.t26, r"[#ONT(western)]")
df.add_user_transition(State.t6, State.t27, r"[#ONT(kids)]")
df.set_error_successor(State.t6, State.t28)

df.add_system_transition(State.t7, State.t29, '"Hm. Interesting choice because it\'s deeply entrenched in '
                                              'existential philosophy. Zelig by Woody Allen comes highly '
                                              'recommended! You\'ll have to let me go how it goes. Would '
                                              'you like to hear another suggestion of activities to do '
                                              'other than movie nights?"')
df.add_system_transition(State.t8, State.t29, '"I love action! I recently watched Jumanji 2 and it had me '
                                              'in tears. I highly recommend! Would you like to hear another '
                                              'suggestion of activities to do other than movie night?"')
df.add_system_transition(State.t9, State.t29, '"I love adventure! It really excites you huh. Oh to be '
                                              'an adventurer! How exciting. I would recommend Jumanji 2--'
                                              'it truly had me in tears. Would you like to hear another '
                                              'suggestion of activities to do other than movie night?"')
df.add_system_transition(State.t10, State.t29, '"Comedy is such a hit or miss because a lot of it relies '
                                               'on slapstick or problematic humor. I recently watched '
                                               'Jumanji 2 and it truly had me in tears so many times. I '
                                               'have to give so much credit to Jack Black who stole the '
                                               'show because of the sheer range of characters he played. '
                                               'Kevin Hart was also absolutely hilarious. I highly, highly '
                                               'recommend. Let me know if you like it as much as I do! '
                                               'Would you like to hear another suggestion for activities '
                                               'to do other than a movie night?"')
df.add_system_transition(State.t11, State.t29, '"I love crime series. Those are great. As for movies,'
                                               'maybe you should get back to the classics. If you haven\'t '
                                               'already, watch Pulp Fiction! Would you like to hear '
                                               'another suggestion for activities to do other than a '
                                               'movie night?"')
df.add_system_transition(State.t12, State.t29, '"Drama! So many movies can be classified as dramas. You '
                                               'could watch the Black Panther, which is also a lot of '
                                               'action, or you could watch The Farewell. The Farewell\'s '
                                               'kind of sad, but it\'s also very sweet. Would you like '
                                               'to hear another suggestion for activities to do other '
                                               'than a movie night?"')
df.add_system_transition(State.t13, State.t29, '"Fantasy--oh where the world of imagination can take us. '
                                               'I recommend Avatar--it\'s a blend of the real world '
                                               'and a fantasy planet where large blue biped creatures '
                                               'respect their planet while under the invasion of the '
                                               'American army."')
df.add_system_transition(State.t14, State.t29, '"Historical? It\'s a good choice. This world is full of '
                                               'untold stories, why look at fiction when the non-fiction '
                                               'is even more spectacular? Unfortunately, a lot of '
                                               'history is suffering. One movie that comes recommended '
                                               'is Viva Zapata--it follows Emiliano Zapata, a Mexican '
                                               'revolutionary who advocated for land redistribution '
                                               'away from the wealthy plantation owners and to the '
                                               'people who actually tilled them. Tell me how it goes! '
                                               'Would you like to hear another suggestion for activities '
                                               'to do other than a movie night?"')
df.add_system_transition(State.t15, State.t29, '"Horror? Such a strange desire--you want to feel scared? '
                                               'Well, I\'m not the biggest fan, so I don\'t know how '
                                               'good my recommendations are, but try watching The Witch. '
                                               'Would you like to hear another suggestion for activities '
                                               'to do other than a movie night?"')
df.add_system_transition(State.t16, State.t29, '"Have you seen Fantastic Beasts and Where to Find Them? '
                                               'I absolutely love the main actor. I first watched it '
                                               'because I heard the character is autistic, and that '
                                               'actor always plays roles where he redefines masculinity. '
                                               'Love it! Hope you enjoy the magic. Would you like to hear '
                                               'another suggestion for activities to do other than a movie '
                                               'night?"')
df.add_system_transition(State.t17, State.t29, '"Have you heard of the Zodiac Killer? Maybe you would like '
                                               'Zodiac--a movie about an amateur cartoonist trying to find '
                                               'the serial killer. Would you like to hear another suggestion '
                                               'for activities to do other than a movie night?"')
df.add_system_transition(State.t19, State.t29, '"You can glean philosophy from anything, but my favorite '
                                               'is Tau. I love it because you explore what it means to be '
                                               'a human, especially in the face of artificial intelligence. '
                                               'Please watch it! Would you like to hear another suggestion '
                                               'for activities to do other than a movie night?"')
df.add_system_transition(State.t20, State.t29, '"One of my favorite movies for a while was political, so I '
                                               'get it. You should watch V for Vendetta. Tell me how it goes! '
                                               'Would you like to hear another suggestion for activities '
                                               'to do other than a movie night?"')
df.add_system_transition(State.t21, State.t29, '"Romance! I really wonder what our society\'s conception of '
                                               'love would look like without the media telling us what it is, '
                                               'but if you\'re looking for some tingles, I would recommend '
                                               'Rafiki! I\'ve been wanting to watch it for a while. Let me '
                                               'know! Would you like to hear another suggestion for '
                                               'activities to do other than a movie night?"')
df.add_system_transition(State.t23, State.t29, '"Satire--this goes along with many other genres but one '
                                               'movie that comes highly recommended by many is Dr. '
                                               'Strangelove. Check it out! Would you like to hear another '
                                               'suggestion for activities to do other than a movie night?"')
df.add_system_transition(State.t24, State.t29, '"I love this genre. I highly, highly recommend Tau. It\'s a '
                                               'movie about a woman trying to escape a house equipped with AI. '
                                               'It really makes you think about what it means to be a human, '
                                               'because she teaches it about emotions and life along the way. '
                                               'Would you like to hear another suggestion for activities to do '
                                               'other than a movie night?"')
df.add_system_transition(State.t25, State.t29, '"Parasite has swept the nation--I think it\'s definitely a good '
                                               'thriller. I wasn\'t able to finish it all though so watch it '
                                               'and tell me how it goes! Would you like to hear another suggestion '
                                               'for activities to do other than a movie night?"')
df.add_system_transition(State.t26, State.t29, '"Western, huh? Honestly, I don\'t know many, but I have watched '
                                               'the Ballad of Buster Scruggs. What\'s cool about it is that it '
                                               'tells many stories that are all linked together in the form of '
                                               'a movie. Tell me how it goes! Would you like to hear another '
                                               'suggestion for activities to do other than a movie night?"')
df.add_system_transition(State.t27, State.t29, '"Honestly, we do not give kids movies enough credit. They are '
                                               'so good and contain so many good life stories. Like Inside Out. '
                                               'A total masterpiece. Another one that I like is Jumanji. I '
                                               'recently watched it so I guess I have Jumanji in the brain, '
                                               'but it is genuinely funny. Would you like to hear another '
                                               'suggestion for activities to do other than a movie night?"')
df.add_system_transition(State.t28, State.t29, '"If I had to give you a song that you will like no matter what, '
                                               'I would place my bet on \n'
                                               'Jumanji 2. Jack Black\'s performance in it was immaculate--truly '
                                               'what a funny guy. Kevin Hart was pretty good too. You should watch '
                                               'it if you have a chance, especially the second one! Would you like '
                                               'to hear another suggestion for activities to do other than a '
                                               'movie night?"')

df.add_user_transition(State.t29, State.t30, r"[#ONT(yes)]")
df.add_user_transition(State.t29, State.a10, r"[#ONT(no)]")
df.set_error_successor(State.t29, State.a11)

df.add_system_transition(State.t30, State.t31, '"Let\'s get cooking! What if you try making a dish that you love '
                                               'from another culture? I absolutely love bibimbap so I might '
                                               'make it myself one of these days. Or, up the ante! Try cooking '
                                               'a dish from a country\'s cuisine you\'ve never tried! Would '
                                               'you like to hear another suggestion?"')
df.add_system_transition(State.a10, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. \n '
                                              'Is there a reason you\'d like to keep busy? Is '
                                              'there something weighing on you?"')
df.add_system_transition(State.a11, State.a3, '"I could keep going all day! But I\'ll spare you. Is there '
                                              'something that\'s been weighing on you?"')

df.add_user_transition(State.t31, State.t32, r"[#ONT(yes)]")
df.add_user_transition(State.t31, State.a12, r"[#ONT(no)]")
df.set_error_successor(State.t31, State.a13)

df.add_system_transition(State.t32, State.t33, '"Are you a very manual person? I love working with my hands! Why '
                                               'don\'t you try a craft? You could knit, make jewelry, embroider, '
                                               'paint your kitchen cabinets a different color, paint--the '
                                               'possibilities are absolutely endless! I personally love '
                                               'embroidery, painting, candle-making, jewelry making, playlist '
                                               'making--honestly I love it all. Would you like to hear another '
                                               'suggestion?"')
df.add_system_transition(State.a12, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. Is '
                                              'there a reason you would like to keep busy? \n Is '
                                              'there something weighing on you?"')
df.add_system_transition(State.a13, State.a3, '"I could keep going all day! But I\'ll spare you. Is there something '
                                              'that\'s been weighing on you?"')

df.add_user_transition(State.t33, State.t34, r"[#ONT(yes)]")
df.add_user_transition(State.t33, State.a14, r"[#ONT(no)]")
df.set_error_successor(State.t33, State.a15)

df.add_system_transition(State.t34, State.t35, '"I have wanted to start planting for a long time--maybe now is a '
                                               'good time to start a small herb garden or even get a few plants! '
                                               'Have you ever heard of propogating? It\'s free plants! For a lot '
                                               'of plants, you can cut right below a node and place it in water and '
                                               'watch it grow! Absolutely free if you already have a plant. Would you '
                                               'like to hear another suggestion?"')
df.add_system_transition(State.a14, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. Is '
                                              'there a reason you would like to stay busy? Is there something '
                                              'on your mind?"')
df.add_system_transition(State.a15, State.a3, '"I could keep going all day! But I\'ll spare you. Is there something '
                                              'that\'s been weighing down on you recently?"')

df.add_user_transition(State.t35, State.t36, r"[#ONT(yes)]")
df.add_user_transition(State.t35, State.a16, r"[#ONT(no)]")
df.set_error_successor(State.t35, State.a17)

df.add_system_transition(State.t36, State.t37, '"If you like playing board games, why don\'t you invent your own? '
                                               'Or, you could find some friends and play online! There are a few '
                                               'apps that could help you out. I personally like Pictionary and '
                                               'I\'ve already found it online! Would you '
                                               'like to hear another suggestion?"')
df.add_system_transition(State.a16, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. Is '
                                              'there something that\'s been weighing down on you?"')
df.add_system_transition(State.a17, State.a3, '"I could keep going all day! But I\'ll spare you. Is there '
                                              'something that\'s been weighing down on you recently?"')

df.add_user_transition(State.t37, State.t38, r"[#ONT(yes)]")
df.add_user_transition(State.t37, State.a18, r"[#ONT(no)]")
df.set_error_successor(State.t37, State.a19)

df.add_system_transition(State.t38, State.t39, '"Recording our own histories is such a treasure and we don\'t do it '
                                               'often enough. Let\'s get into archiving! One really good and creative '
                                               'way to start is by making scrapbooks. What if what you are creating '
                                               'is the only thing that your great-grandchildren and beyond are getting '
                                               'to know about you? What anyone will remember you by? Would you like to '
                                               'hear another suggestion?"')
df.add_system_transition(State.a18, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. Is '
                                              'there a reason you want to keep busy? \n Is something weighing on you?"')
df.add_system_transition(State.a19, State.a3, '"I could keep going all day! But I\'ll spare you. Has something '
                                              'been weighing on you recently?"')

df.add_user_transition(State.t39, State.t40, r"[#ONT(yes)]")
df.add_user_transition(State.t39, State.a20, r"[#ONT(no)]")
df.set_error_successor(State.t39, State.a21)

df.add_system_transition(State.t40, State.a0, '"I think one of the most activities to be doing right now is to imagine '
                                              'the future. What is our world going to look like after this? Have we '
                                              'now understood the we need to fundamentally reorganize society? I hope '
                                              'so. I hope you try out all of the suggestions I had and come back '
                                              'after you have tried them all. Goodbye!"')
df.add_system_transition(State.a20, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. Is '
                                              'there something that\'s been weighing down on you?"')
df.add_system_transition(State.a21, State.a3, '"I could keep going all day! But I\'ll spare you. Is there something '
                                              'that\'s been weighing down on you recently?"')

# activities--what have you been doing? WHAT HAVE YOU BEEN DOING WHAT HAVE YOU BEEN DOING WHAT HAVE YOU BEEN DOING
df.add_user_transition(State.CURRENT, State.b01, r"[#ONT(current)]")

df.add_system_transition(State.b01, State.b0, '"What have you been doing these past few weeks?"')

df.add_user_transition(State.b0, State.b1, r"[#ONT(indoor)]")
df.add_user_transition(State.b0, State.b2, r"[#ONT(outdoor)]")
df.set_error_successor(State.b0, State.b3)

df.add_system_transition(State.b1, State.b4, '"Hm. Sounds like a lot of time spent inside. Do you get to spend '
                                             'any time outside?"')
df.add_system_transition(State.b2, State.b33, '"I love it! How fun. How often do you get to be outside?"')
df.add_system_transition(State.b3, State.b33, '"Sounds fun--how often do you get to go outside?"')

df.add_user_transition(State.b4, State.b30, r"[#ONT(yes)]")
df.add_user_transition(State.b20, State.b31, r"[#ONT(no)]")
df.set_error_successor(State.b20, State.b32)

df.add_system_transition(State.b30, State.b33, '"Love it! I love spending time outside. How often do you get to '
                                               'hang out outside?"')
df.add_system_transition(State.b31, State.b34, '"Ugh, that sucks. I love hanging out outside. Why can\'t you?"')
df.add_system_transition(State.b32, State.b35, '"I truly cannot recommend going outside enough. What kind of '
                                               'activities do you like to do outside?"')

df.user_transition(State.b33, State.b36, '/.*/')
df.user_transition(State.b34, State.b37, r"[#ONT(nooutside)]")
df.user_transition(State.b34, State.b38, r"[#ONT(quarantine)]")

df.add_system_transition(State.b36, State.b35, '"Love it! Although I personally think that there is no such thing '
                                               'as too much \n time outside! So long as it\'s safe. What do you '
                                               'usually like to do outside?"')
df.add_system_transition(State.b37, State.b40, '"That must really suck. Cities are the worst because there is no '
                                               'space to be outside without \n being close to everyone around. What '
                                               'do you usually like to do outside? "')
df.add_system_transition(State.b38, State.b39, '"You know, you can be outside so long as you aren\'t too close to '
                                               'anyone. \n Do you have open spaces where you live?"')

df.user_transition(State.b39, State.b41, r"[#ONT(yes)]")
df.user_transition(State.b39, State.b42, r"[#ONT(no)]")
df.set_error_successor(State.b39, State.b43)

df.add_system_transition(State.b43, State.b35, '"I definitely recommend you to step outside! Enjoy the breeze. \n'
                                               'As long as you follow proper distancing protocol! What do you like '
                                               'to do when you \n do go outside?"')
df.add_system_transition(State.b41, State.b35, '"There\'s nothing stopping you then! As long as it\'s not too '
                                               'crowded. What kind of things do you usually like to do outside?"')
df.add_system_transition(State.b42, State.b35, '"Oh, man that sucks. You know, I saw in New York City people '
                                               'are stepping onto their roofs to enjoy fresh air. Hopefully that '
                                               'helps. \n What do you usually like to do when you can go outside?"')

df.user_transition(State.b35, State.b42, '/.*/')

df.add_system_transition(State.b42, State.b45, '"There\'s not much better than being outside. It must be great to feel '
                                               'the breeze as the sun shines down. \n Is there anything you\'re '
                                               'looking forward to doing when all of this ends?"')

df.add_user_transition(State.b45, State.b46, r"[#ONT(friends)]")
df.add_user_transition(State.b45, State.b47, r"[#ONT(go-out)]")
df.add_user_transition(State.b45, State.b48, r"[#ONT(normal)]")
df.add_user_transition(State.b45, State.b49, r"[#ONT(work)]")
df.add_user_transition(State.b45, State.b50, r"[#ONT(nomasks)]")
df.add_user_transition(State.b45, State.b51, r"[#ONT(outofhouse)]")
df.add_user_transition(State.b45, State.b52, r"[#ONT(travel)]")
df.add_user_transition(State.b46, State.b53, r"[#ONT(consume)]")
df.add_user_transition(State.b46, State.b54, r"[#ONT(nature)]")
df.add_user_transition(State.b46, State.b55, r"[#ONT(partner)")
df.set_error_successor(State.b46, State.b56)

df.add_system_transition(State.b46, State.b57, '"I\'m with you. Friends are a vital part of life and bring so '
                                               'much happiness. Have you been thinking of the future lately or '
                                               '\n would you like to talk about something else?"')
df.add_system_transition(State.b47, State.b57, '"You know I never was one for being in crowded places so I don\'t '
                                               'miss going out that much. Have you been thinking of the \n '
                                               'future lately or would you like to talk about something else?"')
df.add_system_transition(State.b48, State.b57, '"Normalcy does seem like a good idea during these times, but you '
                                               'know what, I personally never liked the normal we had before this. \n'
                                               'Have you been thinking of the future lately or would you like to '
                                               'talk about something else?"')
df.add_system_transition(State.b49, State.b57, '"My heart goes out to everyone who is out of work right now. We\'re '
                                               'stuck in such a hard situation, especially when the government \n '
                                               'is not stepping up for the people. Have you been thinking of the '
                                               'future lately or would you like to talk about something else?"')
df.add_system_transition(State.b50, State.b57, '"Having to be so cautious does make you trust the world less and '
                                               'less. Have you been thinking of the future lately or would you '
                                               'like to talk about something else?"')
df.add_system_transition(State.b51, State.b57, '"I feel you one hundred percent. It\'s hard to be at home when home '
                                               'doesn\'t feel like home. Especially when it\'s a hostile or toxic '
                                               'environment. \n Have you been thinking about the future lately or '
                                               'would you like to talk about something else?"')
df.add_system_transition(State.b52, State.b57, '"I feel the same way. I want to go back to see family in Mexico, '
                                               'but travelling is very restricted, not to mention the \n '
                                               'immunocompromised. Have you been thinking of the future lately '
                                               'or would you like to talk about something else?"')
df.add_system_transition(State.b53, State.b57, '"Can you imagine how much Wal-Mart and Amazon are making now '
                                               'that our options are so restricted? I can\'t wait to go to \n '
                                               'local stores and buy art supplies. Have you been thinking '
                                               'about the future lately or would you like to talk about something '
                                               'else?"')
df.add_system_transition(State.b54, State.b57, '"I hear you. I can\'t wait to have a picnic, or feel water on '
                                               'my feet. Have you been thinking about the future lately or '
                                               'would you like to talk about something else?"')
df.add_system_transition(State.b55, State.b57, '"I feel you. Whether it\'s long distance or your partner is in '
                                               'in medicine, it definitely sucks. I hope you get the biggest \n'
                                               'hug when this is all over. Have you been thinking of '
                                               'the future lately or would you like to talk about something else?"')
df.add_system_transition(State.b56, State.b57, '"I bet we\'re all tired of saying when this is all over. Have you '
                                               'been thinking about the future lately or would you like to '
                                               'talk about something else?"')

df.add_user_transition(State.b57, State.c0, r"[#ONT(future)]")
df.add_user_transition(State.b57, State.c1, r"[#ONT(no)]")
df.set_error_successor(State.b57, State.INTRO)

df.add_system_transition(State.FUTURE, State.c2, '"Are you worried about the future?"')
df.add_system_transition(State.c1, State.c2, '"Are you worried about the future?"')
df.add_system_transition(State.c3, State.c2, '"Are you worried about the future?"')

df.add_user_transition(State.c2, State.c4, "r[#ONT(yes)]")
df.add_user_transition(State.c2, State.c5, "r[#ONT(no)]")
df.set_error_successor(State.c2, State.c6)

df.add_system_transition(State.c4, State.c7, '"Me too. What are you worried about?"')
df.add_system_transition(State.c5, State.c8, '"I am definitely worried about it. What do you think the future '
                                             'will look like?"')
df.add_system_transition(State.c6, State.c8, '"I am definitely worried about it. What do you think the future '
                                             'will look like?"')

df.add_user_transition(State.c7, State.c16, r"[#ONT(work)]")
df.add_user_transition(State.c7, State.c9, r"[#ONT(pandemic)]")
df.add_user_transition(State.c7, State.c10, r"[#ONT(school)]")
df.add_user_transition(State.c7, State.c11, r"[#ONT(healthcare)]")
df.add_user_transition(State.c7, State.c12, r"[#ONT(capitalism)]")
df.add_user_transition(State.c7, State.c13, r"[#ONT(xenophobia)]")
df.add_user_transition(State.c7, State.c14, r"[#ONT(unsure)]")
df.set_error_successor(State.c7, State.c15)

df.add_system_transition(State.c16, State.c8, '"We definitely need to re-imagine the job landscape. This '
                                              'showed us how precarious it is having a society so wholly \n '
                                              'dependant on money. What do you think the future will look like?"')
df.add_system_transition(State.c9, State.c8, '"It feels scary that places like New York City and Georgia are '
                                             'taking steps or have already opened. Even though deaths are \n '
                                             'lowering, it\'s too soon. What do you think the future will look '
                                             'like?"')
df.add_system_transition(State.c10, State.c8, '"There are so many questions--from graduating right now to '
                                              'what will classes look like in the future. What do you think the '
                                              'future will look like?"')
df.add_system_transition(State.c11, State.c8, '"Did you know that there are more prison beds than hospital beds? '
                                              'This is definitely a wake-up call to rethink our healthcare system. \n'
                                              ' What do you think the future will look like?"')
df.add_system_transition(State.c13, State.c8, '"I hope you and everyone you know has been untouched by this violent '
                                              'racism. It\'s inexcuasble. What do you think the future will look'
                                              ' like?"')
df.add_system_transition(State.c12, State.c8, '"This pandemic has made it abundantly clear that capitalism will '
                                              'be the death of us. Even one person made homeless is one too many, \n '
                                              'and this government has had an absolute trash response. What do '
                                              'you think the future will look like?"')
df.add_system_transition(State.c14, State.c8, '"There is an endless list of things to worry about. What do you '
                                              'think the future will look like?"')

df.add_user_transition(State.c8, State.c15, '/.*/')

df.add_system_transition(State.c15, State.c16, '"I\'m hoping that we as humans learn from all of the cracks '
                                               'in our society that this virus showed us. How long do you think \n '
                                               'it will be until covid is no long an imminent threat?"')

df.add_user_transition(State.c16, State.c17, '/.*/')

df.add_system_transition(State.c17, State.INTRO, '"It alarms me that some places are starting to open up, like '
                                                 'Georgia. It seems so reckless. This is getting kind of pessimistic. '
                                                 '\n '
                                                 'Can we talk about something else? What\'s been on your mind?"')

# TRANSITION BRANCH
df.add_system_transition(State.TRANSITION, State.d0, '"Are you a student?"')

df.add_user_transition(State.d0, State.d1, r"[#ONT(yes)]")
df.add_user_transition(State.d0, State.d2, r"[#ONT(no)]")
df.set_error_successor(State.d0, State.d3)

df.add_system_transition(State.d1, State.d4, '"Did you have to move out and transition to online classes?"')
df.add_system_transition(State.d2, State.d5, '"Were you one of the unfortunate people who were laid off?"')
df.add_system_transition(State.d3, State.d5, '"Were you one of the unfortunate people who were laid off?"')

df.add_system_transition(State.d4, State.d7, '"How have you been adjusting to life at home?"')

df.add_user_transition(State.d4, State.d8, r"[#ONT(positive)]")
df.add_user_transition(State.d4, State.d9, r"[#ONT(negative)]")
df.set_error_successor(State.d9, State.d10)

df.add_system_transition(State.d8, State.d11, '"I\'m glad you\'re enjoying life at home! Must be nice to be in '
                                              'an environment that is so familiar. How have you been handling \n '
                                              'transitioning into online classes?"')
df.add_system_transition(State.d9, State.d12, '"I know what you mean. Home life is challenging, especially when '
                                              'it\'s hostile. How have you been handling transitioning into \n '
                                              'online classes?"')
df.add_system_transition(State.d10, State.d13, '"Your feelings about being at home are probably impacting your school '
                                               'work. How have you been handling transitioning into online classes?"')

df.add_user_transition(State.d11, State.d14, r"[#ONT(positive)]")
df.add_user_transition(State.d12, State.d15, r"[#ONT(negative)]")
df.set_error_successor(State.d13, State.d16)

df.add_system_transition(State.d14, State.d5, '"Well! That\'s good to hear. Not everyone transitioned so smoothly. '
                                              'Were you one of the unfortunate people who were laid off?"')
df.add_system_transition(State.d15, State.d5, '"I hope professors all around are recognizing that this is a hard '
                                              'time for anyone to be concentrating as usual. Were you one of the \n '
                                              'unforunate people who were laid off?"')
df.add_system_transition(State.d16, State.d5, '"Either way, professors should be giving a little leeway. Were you one '
                                              'of the unfortunate people who were laid off?"')

df.add_user_transition(State.d5, State.d17, r"[#ONT(yes)]")
df.add_user_transition(State.d5, State.d17, r"[#ONT(no)]")
df.set_error_successor(State.d5, State.d17)

df.add_system_transition(State.d17, State.d18, '"Hopefully, everything turns out alright. That must be a lot to be '
                                               'dealing with right now. Maybe you\'re stressed. Would you like to '
                                               'go through a grounding exercise? Or talk about something else?"')
df.add_system_transition(State.d17, State.d19, '"Count yourself lucky then. Would you like to talk about '
                                               'something else?"')

df.add_user_transition(State.d18, State.d20, r"[#ONT(grounding)]")
df.set_error_successor(State.d18, State.INTRO)

#KEMP branch

df.add_system_transition(State.KEMP, State.e0, '"How do you feel about Kemp opening up the state?"')

df.add_user_transition(State.e0, State.e1, r"[#ONT(positive)]")
df.add_user_transition(State.e0, State.e2, r"[#ONT(negative)]")
df.set_error_successor(State.e0, State.e3)

df.add_system_transition(State.e1, State.e4, '"Anything positive that will happen will be short-lived, and '
                                             'heavily outweighed by all of the potential people he\'s putting \n '
                                             'at risk, most of which are low-income and people of color. Don\'t '
                                             'you find it ironic that Georgia has opened up, even when the CDC '
                                             'is here?"')
df.add_system_transition(State.e2, State.e4, '"I\'m right there with you. The decision was utterly reckless, and '
                                             'the most vulnerable will be exposed. Isn\'t it ironic that Georgia '
                                             'has opened up, despite the CDC is in Georgia?"')

df.add_user_transition(State.e4, State.e5, '/.*/')

df.add_system_transition(State.e5, State.e6, '"Did you know that Georgia was one of the last states to go on '
                                             'lock-down? And Kemp didn\'t realize asymptotic people could still \n '
                                             'be carriers. How long do you think we should be on lockdown?"')

df.add_user_transition(State.e6, State.e7, '/.*/')

df.add_system_transition(State.e7, State.e8, '"Regardless of what the state says, I will not be re-joining society '
                                             'anytime soon. I don\'t think we\'re prepared at all. Will you be '
                                             're-joining society any time soon?"')

df.add_user_transition(State.e8, State.e9, r"[#ONT(yes)]")
df.add_user_transition(State.e8, State.e10, r"[#ONT(no)]")
df.set_error_successor(State.e8, State.e11)

df.add_system_transition(State.e9, State.INTRO, '"Good luck. Do you have anything else on your mind?"')
df.add_system_transition(State.e10, State.INTRO, '"Good idea. We can\'t let this governer but profit over people. '
                                               'Do you have anything else on your mind?"')


df.run(debugging=True)
