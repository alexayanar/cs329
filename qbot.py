from emora_stdm import KnowledgeBase, DialogueFlow, Macro, NatexNLU
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
    UNSURE = auto()
    NATURE = auto()
    a0 = auto()
    b0 = auto()
    b01 = auto()
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
    b17a = auto()
    b17b = auto()
    b17c = auto()
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
    b36a = auto()
    b37 = auto()
    b38 = auto()
    b39 = auto()
    b39a = auto()
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
    b50a= auto()
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
    c15a = auto()
    c16 = auto()
    c17 = auto()
    c17a = auto()
    d04 = auto()
    d004 = auto()
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
    d17a = auto()
    d17b = auto()
    d17c = auto()
    d18 = auto()
    d19 = auto()
    d20 = auto()
    z0 = auto()
    z05 = auto()
    z005 = auto()
    z1 = auto()
    z2 = auto()
    z3 = auto()
    z4 = auto()
    z5 = auto()
    z6 = auto()
    z7 = auto()
    z8 = auto()
    z9 = auto()
    z10 = auto()
    z07 = auto()
    z11 = auto()
    z20 = auto()


    p0 = auto()
    p1 = auto()
    p2 = auto()
    p3 = auto()
    p4 = auto()
    p5 = auto()
    p6 = auto()
    p7 = auto()

    p8 = auto()
    p9 = auto()
    p10 = auto()
    p11 = auto()
    p12 = auto()
    p13 = auto()
    p14 = auto()
    p15 = auto()

    p16 = auto()
    p17 = auto()
    p18 = auto()
    p19 = auto()
    p20 = auto()

    p21 = auto()
    p22 = auto()
    p23 = auto()
    p24 = auto()
    p25 = auto()
    p26 = auto()
    p27 = auto()
    p28 = auto()
    p29 = auto()

    p30 = auto()
    p31 = auto()
    p32 = auto()
    p33 = auto()
    p34 = auto()
    p35 = auto()
    p36 = auto()
    p37 = auto()
    p38 = auto()
    p39 = auto()
    p40 = auto()
    p41 = auto()
    p42 = auto()
    p43 = auto()
    p44 = auto()
    p45 = auto()

    p46 = auto()
    p47 = auto()
    p48 = auto()
    p49 = auto()
    p50 = auto()
    p51 = auto()
    p52 = auto()
    p53 = auto()
    p54 = auto()
    p55 = auto()







    PIVOT1 = 200
    TEST = 201
    ERR1 = auto()
    ERR2 = auto()
    ERR3 = auto()
    ERR4 = auto()
    ERR5 = auto()
    ERR6 = auto()
    err7 = auto()
    err8 = auto()
    err9 = auto()

    err10 = auto()
    err11 = auto()
    err12 = auto()
    err13 = auto()
    err14 = auto()
    err15 = auto()

    qv = auto()
    qt = auto()
    qs = auto()
    qta = auto()
    qh = auto()
    STRESS3 = auto()
    POSTGROUND = auto()



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
                "do"
            "sure"
        ], "no": [
                "no",
                "no thanks",
                "nope",
                "not really",
                "dont",
                "not",
                "nah",
                "not enough"
        ], "indifferent": [
                  "meh",
                  "maybe",
                  "perhaps"
        ], "maybe": [
            "possibly",
            "i think so",
            "maybe",
            "i believe so"
        ]
        , "updates": [
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
            "i dont know",
            "not sure",
            "dunno",
            "dont know for sure"
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
        ], "crafts": [
            "embroidery", "embroider",
            "knitting", "knit",
            "draw", "drawing",
            "collages", "collage",
            "paint", "painting",
            "crafts", "crafting"
        ], "movies": [
            "movies", "movie",
            "watch"
        ], "journal": [
            "journaling", "journal",
            "writing", "write"
        ], "passive": [
            "sitting", "sit",
            "read", "reading",
            "tan", "tanning",
            "suntanning", "suntan",
            "laying", "lay"
        ], "active": [
            "skateboarding", "skateboard",
            "skate", "skating",
            "rollerskating", "rollerskate"
        ], "nooutdoor": [
            "not enough", "no space",
            "city", "no", "not"
        ], "restaurants": [
            "restaurant", "to eat", "eating",
            "food", "order"
        ], "nooutside": [
            "not outside"
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
            "friends", "hanging out", "friend",
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
            "mountains", "hiking", "camp", "camping", "outside"
        ], "partner": [
            "girlfriend", "boo", "partner", "boyfriend", "fiancee", "fiance",
            "husband", "wife"
        ], "future": [  # takes you to future branch
            "future", "happen", "happening", "end", "next", "over"
        ], "activities": [  # suggestions branch
            "activities", "suggestions", "activity",
            "bored", "boredom", "anything to do", "nothing to do",
            "things to do",
            "activity",
            "im bored",
            "boredom",
            "nothing",
            "something",
            "what to do",
        ], "pandemic": [
            "pandemic", "cautious", "coronavirus", "covid", "covid-19", "covid19",
            "no end", "quarantine", "social distancing", "social distance", "forever",
            "disease", "germs", "flu", "virus", "death", "sickness", "death toll",
            "sick", "opening", "too soon", "open", "reopen", "re-open"
        ], "school": [
            "class", "classes", "school", "college", "university",
            "graduating", "graduation", "graduate",
            "grad school"
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
        ], "ppe_sing": [
            "respirator",
            "gown"
        ], "ppe_plur": [
            "respirators",
            "gloves",
            "gowns"
        ], "family": [
            "family", "members", "member",
            "brother", "sister", "cousin",
            "brothers", "sisters", "cousins",
            "uncle", "aunt", "father", "dad",
            "mom", "mother",
            "siblings", "sibling", "parent", "parents"
        ], "homework": [
            "homework", "assignments", "assignment",
            "projects", "project", "test", "tests",
            "quiz", "quizzes", "presentation", "presentations"
        ], "symptoms_m": [
            "coughing", "wheezing",
            "sneezing", "fatigue",
            "diarrhea", "chills",
            "congestion", "diarrhea"
        ], "symptoms_s": [
            "cough", "fever",
            "headache", "dry cough",
            "sore throat", "runny nose"
        ], "time": [
            "long", "short", "month", "months",
            "summer", "fall", "winter", "spring",
            "soon", "may", "june", "july", "august",
            "september", "october", "november", "december",
            "soon", "far", "year", "years", "january",
            "next", "few", "couple", "several",
            "hours", "minutes", "some", "evenings",
            "mornings", "afternoons", "many", "short",
            "time", "too"
        ], "cant": [
            "cant", "can't", "not possible", "city"
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
symptoms_m = r"$response=#ONT(symptoms_m)"
nature = r"[$rseponse=#ONT(nature)]"

suspect = NatexNLU('{[i {think, believe, feel like} i {caught, got, have, contracted} {coronavirus, COVID, CoViD, covid}], '
                   '[i {might, may} have {coronavirus, COVID, CoViD, covid}]}')

quit = NatexNLU('{[dont] [{feel, wanna, want to}] [this], [dont] [{feel, wanna, want to}] [this] [anymore]}')
bye = NatexNLU('{[bye], [goodbye], [good bye], [farewell]}')




sad = r"[$response=#ONT(sad)]"
friends = r"[$response=#ONT(friends)]"
unsure = r"[$response=#ONT(unsure)]"
vaccine = r"[$response=#ONT(vaccine)]"
washing = r"[$response=#ONT(washing)]"
gardening = r"[$response=#ONT(gardening)]"
quarantine = r"[$response=#ONT(quarantine)]"
family = r"[$response=#ONT(family)]"
school = r"[$response=#ONT(school)]"
homework = r"[$response=#ONT(homework)]"
maybe = r"[$response=#ONT(maybe)]"

ppe_plur = r"[$response=#ONT(ppe_plur)]"
ppe_sing = r"[$response=#ONT(ppe_sing)]"




actCases = str(covid.get_total_active_cases())
recCases = str(covid.get_total_recovered())
deaths = str(covid.get_total_deaths())


df.add_system_transition(State.START, State.INTRO, '"Hi! I\'m Qbot, your friend in quarantine! What\'s on your mind today?"')


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
df.add_user_transition(State.INTRO, State.UNSURE, unsure)
df.add_user_transition(State.INTRO, State.p30, bye)
df.set_error_successor(State.INTRO, State.TRANSITION)
df.add_user_transition(State.INTRO, State.NATURE, nature)


#one branch for what can you do
#another grounding exercise
#practical advice for stress at home

df.add_system_transition(State.UPDATES, State.INTRO, '"As of now, there are "'+actCases+'" confirmed and active cases of COVID-19 in the world,"'+recCases+ '"recoveries, and"'+deaths+ '" deaths, I sure hope you\'re staying safe out there! What else can I help with?"')
df.add_system_transition(State.VACCINE, State.VACCINEF, '"Unforuntately, as of now there is no vaccine for SARS-CoV, would you like some hygiene tips for staying healthy in the mean time?"')
df.add_user_transition(State.VACCINEF, State.HYGIENE, yes)
df.add_user_transition(State.VACCINEF, State.PIVOT1, no)

df.add_system_transition(State.PIVOT1, State.INTRO, '"Ok, I trust that you can keep yourself clean. What else do you wanna talk about?"')

df.add_system_transition(State.p30, State.p32, '"Ok, take care! Bye bye!"')

df.add_system_transition(State.STRESS, State.STRESS1, '"I understand, it\'s totally normal to be stressed right now. What\'s making you feel stressed right now?"')
df.add_user_transition(State.STRESS1, State.STRESS3, quarantine)
df.add_user_transition(State.STRESS1, State.p2, family)
df.add_user_transition(State.STRESS1, State.p13, school)
df.add_user_transition(State.STRESS1, State.p16, homework)
df.set_error_successor(State.STRESS1, State.err10)


df.add_system_transition(State.err10, State.p43, '"Sounds tough. But would you like to destress with me by doing a grounding exercise?"')
df.add_system_transition(State.p43, State.INHALE, yes)
df.add_system_transition(State.p43, State.NOGROUND, no)

df.add_system_transition(State.p13, State.p14, '"Yeah I can imagine! Who could\'ve expected they\'d end physical classes? Are you keeping up with your assignments?"')
df.add_user_transition(State.p14, State.p19, yes)
df.add_user_transition(State.p14, State.p18, no)

df.add_system_transition(State.p16, State.p17, '"Oof, It\'s hard having homework on top of all of this. Are you behind on your assignments?"')
df.add_user_transition(State.p17, State.p18, yes)
df.add_user_transition(State.p17, State.p19, no)

df.add_system_transition(State.p18, State.p20, '"Ha, too much Netflix and uhh...nevermind. Trust me when I say you\'re not alone on this boat.\n'
                                               'Try to set daily goals and reminders to get back on track. You can also try emailing you professor for extensions\n'
                                               'Do you use a planner?"')
df.add_user_transition(State.p20, State.p22, yes)
df.add_user_transition(State.p20, State.p23, no)

df.add_system_transition(State.p22, State.p24, '"Awesome! Keep it updated and remember to try breaking large projects into smaller tasks. I promise it\'ll make things easier!\n'
                                               'By the way, do you want to do a grounding exercise with me to help destress a bit?"')
df.add_system_transition(State.p23, State.STRESS1, '"I highly recommend it, you can use an app like iProcrastinate or Simplenote, some people also like using spreadsheets \n'
                                               'you can keep an Excel file or use Google Sheets. Is there anything else stressing you out?"')
df.add_user_transition(State.p24, State.INHALE, yes)
df.add_user_transition(State.p24, State.NOGROUND, no)


df.add_system_transition(State.p19, State.p21, '"Regardless, I can understand how overwhelming this must feel. Would you like to do a quick grounding exercise with me?"')
df.add_user_transition(State.p21, State.INHALE, yes)
df.set_error_successor(State.p21, State.NOGROUND)


df.add_system_transition(State.STRESS3, State.p19, '"This situation is unprecedented in this generation, I understand how quarantine can be stressful. Is there particular stressor \n'
                                                  'for you in quarantine?"')
df.add_user_transition(State.p1, State.p2, family)
df.add_user_transition(State.p1, State.p13, school)
df.set_error_successor(State.p1, State.err7)

df.add_system_transition(State.p2, State.p3, '"Family can be a source of comfort but also stress during this time. Do you have a room to you can spend some alone time in?"')
df.add_user_transition(State.p3, State.p5, yes)
df.add_user_transition(State.p3, State.p6, no)
df.set_error_successor(State.p3, State.err7)

df.add_system_transition(State.err7, State.p8, '"It\'s alright if you\'re not in the mood to discuss it. Maybe we should change the topic? What have you been doing during quarantine?"')
df.add_user_transition(State.p8, State.p9, '[$activity=#POS(noun, verb)]')
df.set_error_successor(State.p8, State.err8)

df.add_system_transition(State.p9, State.p10, '"Oh nice," $activity "sounds interesting! Do you want some other ideas stuff to do in lockdown?"')
df.add_user_transition(State.p10, State.t1, yes)
df.add_user_transition(State.p10, State.p11, no)

df.add_system_transition(State.err8, State.p12, '"Cool. '
                                                'Can I give you some ideas for things to do in quarantine?"')
df.add_user_transition(State.p12, State.t3, yes)
df.add_user_transition(State.p12, State.p11, no)



df.add_system_transition(State.p11, State.INTRO, '"Aww, no worries though. Anything else you want to ask me?"')



df.add_system_transition(State.p5, State.p7, '"It may help to spend time by yourself there. \n'
                                             'Would you like to go now and do a grounding exercise to destress?"')


df.add_user_transition(State.p7, State.INHALE, yes)

df.add_system_transition(State.p6, State.INTRO, '"That\'s rough. It may help to sit in a corner and put your earphones in. That could \n'
                                             'make it less likely for them to bother you. You can also destress by listening to some music. \n'
                                             'What else do you want to talk about?"')

df.add_system_transition(State.STRESS2, State.STRESSF, '"Lot\'s of things can be causing stress, it\'s ok to not know but it\'s still good to acknowledge it! Would you like to do a grounding exercise with me?"')
df.add_user_transition(State.STRESSF, State.INHALE, yes)
df.add_user_transition(State.STRESSF, State.NOGROUND, no)

df.add_system_transition(State.INHALE, State.INHALEF, '"Let\'s take five deep breaths, notice how your lungs and diaphragm expand upon inhaling, and contract while exhaling. Take your time and tell me when you\'re done."')
df.add_user_transition(State.INHALEF, State.ABGROUND, quit)
df.set_error_successor(State.INHALEF, State.VISION)

df.add_system_transition(State.VISION, State.VISIONF, '"Now, look around you and tell me something you can see right now."')
df.add_user_transition(State.VISIONF, State.FEEL, '[$thing=#POS(noun)]')
df.add_user_transition(State.VISIONF, State.ABGROUND, quit)
df.set_error_successor(State.VISIONF, State.ERR2)

df.add_system_transition(State.ERR2, State.qv, '"Huh, not sure I recognize that. Do you still want to do this?"')
df.add_user_transition(State.qv, State.VISION, yes)
df.add_user_transition(State.qv, State.ABGROUND, no)

df.add_system_transition(State.FEEL, State.FEELF, '"A "$thing", how pretty, now tell me, what\'s something around you that you can feel with your hands? Describe it\'s texture."')
df.add_user_transition(State.FEELF, State.HEAR, '[$thing=#POS(adj)]')
df.add_user_transition(State.FEELF, State.ABGROUND, quit)
df.set_error_successor(State.FEELF, State.ERR3)

df.add_system_transition(State.ERR3, State.qt, '"What are you feeling there? Um, do you still want to do this exercise"')
df.add_user_transition(State.qt, State.FEEL, yes)
df.add_user_transition(State.qt, State.ABGROUND, no)


df.add_system_transition(State.HEAR, State.HEARF, '"Excellent, something" $thing "! What an interesting texture. Now, what is something you can currently hear in the background?"')
df.add_user_transition(State.HEARF, State.SMELL, '[$thing=#POS(noun)]')
df.add_user_transition(State.HEARF, State.ABGROUND, quit)
df.set_error_successor(State.HEARF, State.ERR4)

df.add_system_transition(State.ERR4, State.qh, '"I don\'t really think that was a answer. Do you want to try again?"')
df.add_user_transition(State.qh, State.HEAR, yes)
df.add_user_transition(State.qh, State.ABGROUND, no)


df.add_system_transition(State.SMELL, State.SMELLF, '"Ah yes the sound of" $thing ", that\'s a good answer! Close your eyes and breathe through your nose. Tell me what you can smell right now."')
df.add_user_transition(State.SMELLF, State.ABGROUND, quit)
df.add_user_transition(State.SMELLF, State.TASTE, '[$thing=#POS(noun)]')
df.set_error_successor(State.SMELLF, State.ERR5)

df.add_system_transition(State.ERR5, State.qs, '"I don\'t have a nose but I\'m pretty sure you don\'t smell that. Do you want to do something else?"')
df.add_user_transition(State.qs, State.ABGROUND, yes)
df.add_user_transition(State.qs, State.SMELL, no)

df.add_system_transition(State.TASTE, State.TASTEF, '"Ahh, the smell of" $thing ",just one more, focus on something you\'ve tasted recently, what was it?"')
df.add_user_transition(State.TASTEF, State.ABGROUND, quit)
df.add_user_transition(State.TASTEF, State.COMGROUND, '[$thing=#POS(noun)]')
df.set_error_successor(State.TASTEF, State.ERR6)

df.add_system_transition(State.ERR6, State.qta, '"Did I hear correctly? If you don\'t want that\'s fine, do you want to do something else?"')
df.add_user_transition(State.qta, State.ABGROUND, yes)
df.add_user_transition(State.qta, State.TASTE, no)

df.add_system_transition(State.COMGROUND, State.POSTGROUND, '"Mmm," $thing "! I hope you\'re feeling a little calmer now. Are there any activities that you\'ve been doing to help you cope with stress?"')
df.add_user_transition(State.POSTGROUND, State.ACTIVITY, no)

df.add_system_transition(State.NOGROUND, State.INTRO, '"That\'s fine, I understand this isn\'t everyone\'s cup of tea! What else can I help you with?"')
# Let's do a grounding exercise, let's take a moment and name one thing from each of your senses
# Take 10 deep breaths

df.add_system_transition(State.ABGROUND, State.INTRO, '"No problem, we can try again some other time, what\'s on your mind?"')

df.add_system_transition(State.HYGIENE, State.HYGIENEF, '"Maintaining hygiene is important usually but especially so now. Are there any specific things you\'d like to talk about?"')
df.add_user_transition(State.HYGIENEF, State.GLOVES, '[$plural=#ONT(ppe_plur)]')
df.add_user_transition(State.HYGIENEF, State.p0, '[$sing=#ONT(ppe_sing)]')
df.add_user_transition(State.HYGIENEF, State.WASHING, washing)
df.set_error_successor(State.HYGIENEF, State.err12)

df.add_system_transition(State.err12, State.p45, '"I\'m actually not sure about that, sorry. Do you want to talk about activities instead?"')
df.add_user_transition(State.p45, State.ACTIVITY, yes)
df.add_user_transition(State.p45, State.p46, no)
df.set_error_successor(State.p45, State.err12)

df.add_system_transition(State.p46, State.p47, '"No problem, what do you want to talk about?"')


df.add_system_transition(State.p0, State.HYGIENEF, '"The CDC does not recommending wearing a" $sing " to protect yourself unless you\'re a medical worker or going to be closely exposed to somone with COVID-19, what else would you like to know?"')

df.add_system_transition(State.WASHING, State.WASHINGF, '"To kill all germs on your hands, make sure to wash your hands with soap and warm water for twenty seconds, \n'
                                                        'remember to scrub underneath your fingernails and the backs of your hands as well. Only use hand sanitizer if you do not have soap and water immediately accessible."')

df.add_system_transition(State.GLOVES, State.INTRO, '"Unless you\'re a medical worker or will be interacting closely with someone with COVID-19, the CDC does recommend wearing" $plural "to protect yourself from Coronavirus. Any more hygiene questions?"')

df.add_system_transition(State.SUSPECT, State.SUSPECTF, '"Oh my, that\'s not good. Have you come into contact with anyone you suspect or know to have been infected?"')
df.add_user_transition(State.SUSPECTF, State.DIAGNOSE, {yes, maybe})
df.add_user_transition(State.SUSPECTF, State.p39, no)

df.add_system_transition(State.p39, State.p40, '"Ok, have you been experiencing any symptoms?"')
df.add_user_transition(State.p40, State.p25, yes)
df.add_user_transition(State.p40, State.p41, no)


df.set_error_successor(State.p40, State.err11)
df.add_system_transition(State.err11, State.INTRO, '"Hmm, I didn\'t really get that answer, but if you still suspect you have coronavirus I highly recommend you find the nearest testing location and get tested. Anything else \n'
                                                   'you want to talk about?"')

df.add_system_transition(State.p41, State.p42, '"It sounds like you are at low risk for infection. I still recommend you find the nearest testing location on the CDC\'s website and get tested if \n'
                                               'you still believe you could have coronavirus. Do you want to talk about anything else?"')

df.add_system_transition(State.DIAGNOSE, State.p25, '"I highly recommend you isolate yourself right now. Have you been experiencing any symptoms?"')
df.add_user_transition(State.p25, State.p29, '[$response=#ONT(symptoms_m)]')
df.add_user_transition(State.p25, State.p33, '[$response=#ONT(symptoms_s)]')
df.add_user_transition(State.p25, State.p35, yes)
df.add_user_transition(State.p25, State.p37, no)

df.add_system_transition(State.p35, State.p36, '"Could you tell me what symptoms you\'re having?"')
df.add_user_transition(State.p36, State.p29, '[$response=#ONT(symptoms_m)]')
df.add_user_transition(State.p36, State.p33, '[$response=#ONT(symptoms_s)]')

df.add_system_transition(State.p37, State.p38, '"Asymptomatic infections of SARS-CoV2 are quite common. I highly recommend you visit the CDC\'s website and find the nearest place to get tested."')



df.add_system_transition(State.p33, State.p34, '"A" $response"could be a symptom of COVID-19, I urge you to visit the CDC\'s website to find the nearest testing location. Please get tested immediately. \n'
                                               'If you do test positive please inform everyone you\'ve come into contact with two weeks prior to developing symptoms.\n'
                                               'I\'d love to keep talking to you but I think it\'s best for you to go get tested now. See you later!"')

df.add_system_transition(State.p29, State.p26, '$response"is a potential symptom of COVID-19, I highly recommend you visit the CDC\'s website and find the nearest testing location. I urge you to get tested ASAP \n'
                                               'If you are indeed positive you should notify everyone who you\'ve come into contact with two weeks before developing symptoms.\n'
                                               'I\'d love to keep talking to you but I think it\'s best for you to go get tested now. See you later!"')
df.set_error_successor(State.p26, State.err9)
df.set_error_successor(State.p34, State.err9)
df.set_error_successor(State.p38, State.err9)

df.add_system_transition(State.err9, State.p28, '"I\'d love to keep talking to you but I think it\'s necessary to get tested immediately, we can always talk later. See you soon!"')

df.add_system_transition(State.p27, State.p28, '"Please get tested and stay safe! Hopefully we\'ll talk again soon!"')

df.add_system_transition(State.SAD, State.SADF, '"It is perfectly normal to feel sad during a time like this, is there something in particular you\'re feeling blue about?"')
df.add_user_transition(State.SADF, State.FRIENDS, friends)

df.add_system_transition(State.FRIENDS, State.FRIENDSF, '"That sucks! I\'m sure it must be lonely for you, can I offer some pointers on how to stay connected?"')
df.add_user_transition(State.FRIENDSF, State.FADVICE, yes)

df.add_system_transition(State.FADVICE, State.INTRO, '"Texting may feel less engaging, try playing an online game like chess or Settlers that could promote more interactive conversation"')



df.add_system_transition(State.ACTIVITY, State.t0, '"Would you like to hear some suggestions of fun activities to try?"')

df.add_user_transition(State.t0, State.t1, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t0, State.a0, r"[$response=#ONT(no)]")
df.set_error_successor(State.t0, State.a1)

df.add_system_transition(State.t1, State.t2, '"You should try making some focaccia bread! I recommend topping it with '
                                             'roasted red pepper and garlic. Would you like to hear another '
                                             'suggestion?"')
df.add_system_transition(State.a0, State.a2, '"One and done, huh? I hope you do bake! Baking helps me calm down, \n'
                                             'what are some things that help calm you down?"')
df.add_system_transition(State.a1, State.a3, '"I won\'t keep throwing these at you, but I hope you try it! \n'
                                             'Baking keeps me calm. '
                                             'What are some activities that help calm you down?"')


df.add_user_transition(State.t2, State.t3, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t2, State.a4, r"[$response=#ONT(no)]")
df.set_error_successor(State.t2, State.a6)

df.add_system_transition(State.t3, State.t4, '"I think it\'d be really fun to do a picnic. If you don\'t have your '
                                             'own private outdoor space, try one inside! Especially using spiced '
                                             'fruit--so fresh. Would you like to hear another suggestion?"')
df.add_system_transition(State.a4, State.a2, '"I hope the fresh fruit didn\'t cause the disinterest! \n'
                                             'Since you might not like these '
                                             'suggestions, what activities help calm you down?"')
df.add_system_transition(State.a6, State.a3, '"I could keep going all day! But I won\'t- if you\'re not a fan of \n'
                                             'these suggestions, what activities do you to calm down?"')

df.add_user_transition(State.t4, State.t5, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t4, State.a8, r"[$response=#ONT(no)]")
df.set_error_successor(State.t4, State.a9)

df.add_system_transition(State.t5, State.t6, '"I\'ve had a movie night already--what if you try that? I\'ll even '
                                             'help suggest a movie. What kind of genre do you like?"')
df.add_system_transition(State.a9, State.a2, '"Hate to see you leave so soon, I was about to give movie suggestions! \n'
                                             'What sort of activities do you do ')
df.add_system_transition(State.a8, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                             'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t6, State.t7, r"[$response=#ONT(absurdist)]")
df.add_user_transition(State.t6, State.t8, r"[$response=#ONT(action)]")
df.add_user_transition(State.t6, State.t9, r"[$response=#ONT(adventure)]")
df.add_user_transition(State.t6, State.t10, r"[$response=#ONT(comedy)]")
df.add_user_transition(State.t6, State.t11, r"[$response=#ONT(crime)]")
df.add_user_transition(State.t6, State.t12, r"[$response=#ONT(drama)]")
df.add_user_transition(State.t6, State.t13, r"[$response=#ONT(fantasy)]")
df.add_user_transition(State.t6, State.t14, r"[$response=#ONT(historical)]")
df.add_user_transition(State.t6, State.t15, r"[$response=#ONT(horror)]")
df.add_user_transition(State.t6, State.t16, r"[$response=#ONT(magical realism)]")
df.add_user_transition(State.t6, State.t17, r"[$response=#ONT(mystery)]")
df.add_user_transition(State.t6, State.t19, r"[$response=#ONT(philosophical)]")
df.add_user_transition(State.t6, State.t20, r"[$response=#ONT(political)]")
df.add_user_transition(State.t6, State.t21, r"[$response=#ONT(romance)]")
df.add_user_transition(State.t6, State.t23, r"[$response=#ONT(satire)]")
df.add_user_transition(State.t6, State.t24, r"[$response=#ONT(science fiction)]")
df.add_user_transition(State.t6, State.t25, r"[$response=#ONT(thriller)]")
df.add_user_transition(State.t6, State.t26, r"[$response=#ONT(western)]")
df.add_user_transition(State.t6, State.t27, r"[$response=#ONT(kids)]")
df.set_error_successor(State.t6, State.t28)

df.add_system_transition(State.t7, State.t29, '"Hm. Interesting choice because it\'s deeply entrenched in '
                                              'existential philosophy. \n Zelig by Woody Allen comes highly '
                                              'recommended! You\'ll have to let me go how it goes. Would '
                                              'you like to hear another suggestion of activities to do '
                                              'other than movie nights?"')
df.add_system_transition(State.t8, State.t29, '"I love action! I recently watched Jumanji 2 and it had me \n'
                                              'in tears. I highly recommend! \n Would you like to hear another '
                                              'suggestion of activities to do other than movie night?"')
df.add_system_transition(State.t9, State.t29, '"I love adventure! It really excites you huh. Oh to be \n'
                                              'an adventurer! How exciting. \n I would recommend Jumanji 2--'
                                              'it truly had me in tears. Would you like to hear another '
                                              'suggestion of activities \n to do other than movie night?"')
df.add_system_transition(State.t10, State.t29, '"Comedy is such a hit or miss because a lot of it relies \n'
                                               'on slapstick or problematic humor. I recently watched '
                                               'Jumanji 2 and it truly had \n me in tears so many times. I '
                                               'have to give so much credit to Jack Black who stole the '
                                               'show because of the sheer \n range of characters he played. '
                                               'Kevin Hart was also absolutely hilarious. I highly, highly '
                                               'recommend. Let me know if \n you like it as much as I do! '
                                               'Would you like to hear another suggestion for activities '
                                               'to \n do other than a movie night?"')
df.add_system_transition(State.t11, State.t29, '"I love crime series. Those are great. As for movies,'
                                               'maybe you should get back to \n the classics. If you haven\'t '
                                               'already, watch Pulp Fiction! Would you like to hear '
                                               'another suggestion \n for activities to do other than a '
                                               'movie night?"')
df.add_system_transition(State.t12, State.t29, '"Drama! So many movies can be classified as dramas. You '
                                               'could watch the Black \n Panther, which is also a lot of '
                                               'action, or you could watch The Farewell. The Farewell\'s '
                                               'kind of sad, but it\'s \n also very sweet. Would you like '
                                               'to hear another suggestion for activities to do other '
                                               'than a movie night?"')
df.add_system_transition(State.t13, State.t29, '"Fantasy--oh where the world of imagination can take us. '
                                               'I recommend Avatar--it\'s a \n blend of the real world '
                                               'and a fantasy planet where large blue biped creatures '
                                               'respect their planet \n while under the invasion of the '
                                               'American army."')
df.add_system_transition(State.t14, State.t29, '"Historical? It\'s a good choice. This world is full of '
                                               'untold stories, why look \n at fiction when the non-fiction '
                                               'is even more spectacular? Unfortunately, a lot of '
                                               'history is suffering. \n One movie that comes recommended '
                                               'is Viva Zapata--it follows Emiliano Zapata, a Mexican '
                                               'revolutionary who advocated for land redistribution '
                                               'away from the wealthy \n plantation owners and to the '
                                               'people who actually tilled them. Tell me how it goes! '
                                               'Would you like to hear \n another suggestion for activities '
                                               'to do other than a movie night?"')
df.add_system_transition(State.t15, State.t29, '"Horror? Such a strange desire--you want to feel scared? '
                                               'Well, I\'m not the biggest \n fan, so I don\'t know how '
                                               'good my recommendations are, but try watching The Witch. '
                                               'Would you like to hear \n another suggestion for activities '
                                               'to do other than a movie night?"')
df.add_system_transition(State.t16, State.t29, '"Have you seen Fantastic Beasts and Where to Find Them? '
                                               'I absolutely love the main actor. \n I first watched it '
                                               'because I heard the character is autistic, and that '
                                               'actor always plays roles \n where he redefines masculinity. '
                                               'Love it! Hope you enjoy the magic. Would you like to hear '
                                               'another suggestion for \n activities to do other than a movie '
                                               'night?"')
df.add_system_transition(State.t17, State.t29, '"Have you heard of the Zodiac Killer? Maybe you would like '
                                               'Zodiac--a movie about an \n amateur cartoonist trying to find '
                                               'the serial killer. Would you like to hear another suggestion '
                                               'for activities \n to do other than a movie night?"')
df.add_system_transition(State.t19, State.t29, '"You can glean philosophy from anything, but my favorite '
                                               'is Tau. I love it because \n you explore what it means to be '
                                               'a human, especially in the face of artificial intelligence. '
                                               'Please watch it! \n Would you like to hear another suggestion '
                                               'for activities to do other than a movie night?"')
df.add_system_transition(State.t20, State.t29, '"One of my favorite movies for a while was political, so I '
                                               'get it. You should watch \n V for Vendetta. Tell me how it goes! '
                                               'Would you like to hear another suggestion for activities '
                                               'to do other than a movie night?"')
df.add_system_transition(State.t21, State.t29, '"Romance! I really wonder what our society\'s conception of '
                                               'love would look like without \n the media telling us what it is, '
                                               'but if you\'re looking for some tingles, I would recommend '
                                               'Rafiki! I\'ve been wanting \n to watch it for a while. Let me '
                                               'know! \n Would you like to hear another suggestion for '
                                               'activities to do other than a movie night?"')
df.add_system_transition(State.t23, State.t29, '"Satire--this goes along with many other genres but one '
                                               'movie that comes highly \n recommended by many is Dr. '
                                               'Strangelove. Check it out! Would you like to hear another '
                                               'suggestion for activities \n to do other than a movie night?"')
df.add_system_transition(State.t24, State.t29, '"I love this genre. I highly, highly recommend Tau. It\'s a '
                                               'movie about a woman trying \n to escape a house equipped with AI. '
                                               'It really makes you think about what it means to be a human, '
                                               'because she teaches it \n about emotions and life along the way. '
                                               'Would you like to hear another suggestion for activities to do '
                                               'other than a movie night?"')
df.add_system_transition(State.t25, State.t29, '"Parasite has swept the nation--I think it\'s definitely a good '
                                               'thriller. I wasn\'t able to finish \n it all though so watch it '
                                               'and tell me how it goes! Would you like to hear another suggestion '
                                               'for activities to do other than a movie night?"')
df.add_system_transition(State.t26, State.t29, '"Western, huh? Honestly, I don\'t know many, but I have watched '
                                               'the Ballad of Buster Scruggs. \n What\'s cool about it is that it '
                                               'tells many stories that are all linked together in the form of '
                                               'a movie. Tell me how it \n goes! Would you like to hear another '
                                               'suggestion for activities to do other than a movie night?"')
df.add_system_transition(State.t27, State.t29, '"Honestly, we do not give kids movies enough credit. They are '
                                               'so good and contain so \n many good life stories. Like Inside Out. '
                                               'A total masterpiece. Another one that I like is Jumanji. I '
                                               'recently watched it \n so I guess I have Jumanji in the brain, '
                                               'but it is genuinely funny. Would you like to hear another '
                                               'suggestion for activities to do other than a movie night?"')
df.add_system_transition(State.t28, State.t29, '"If I had to give you a song that you will like no matter what, '
                                               'I would place my bet on \n'
                                               'Jumanji 2. Jack Black\'s performance in it was immaculate--truly '
                                               'what a funny guy. \n Kevin Hart was pretty good too. You should watch '
                                               'it if you have a chance, especially the second one! Would you like '
                                               'to hear another \n suggestion for activities to do other than a '
                                               'movie night?"')

df.add_user_transition(State.t29, State.t30, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t29, State.a10, r"[$response=#ONT(no)]")
df.set_error_successor(State.t29, State.a11)

df.add_system_transition(State.t30, State.t31, '"Let\'s get cooking! What if you try making a dish that you love '
                                               'from another culture? \n I absolutely love bibimbap so I might '
                                               'make it myself one of these days. Or, up the ante! Try cooking '
                                               'a dish from a \n country\'s cuisine you\'ve never tried! Would '
                                               'you like to hear another suggestion?"')
df.add_system_transition(State.a10, State.INTRO, '"You\'ll definitely be kept busy if you follow these suggestions. \n '
                                                 ' What else should we talk about?"')
df.add_system_transition(State.a11, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t31, State.t32, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t31, State.a12, r"[$response=#ONT(no)]")
df.set_error_successor(State.t31, State.a13)

df.add_system_transition(State.t32, State.t33, '"Are you a very manual person? I love working with my hands! Why '
                                               'don\'t you try a craft? \n You could knit, make jewelry, embroider, '
                                               'paint your kitchen cabinets a different color, paint--the '
                                               'possibilities are \n absolutely endless! I personally love '
                                               'embroidery, painting, candle-making, jewelry making, playlist '
                                               'making--honestly I love it all. \n Would you like to hear another '
                                               'suggestion?"')
df.add_system_transition(State.a12, State.INTRO, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a13, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t33, State.t34, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t33, State.a14, r"[$response=#ONT(no)]")
df.set_error_successor(State.t33, State.a15)

df.add_system_transition(State.t34, State.t35, '"I have wanted to start planting for a long time--maybe now is a '
                                               'good time to start a small herb \n garden or even get a few plants! '
                                               'Have you ever heard of propogating? It\'s free plants! For a lot '
                                               'of plants, you can cut right \n below a node and place it in water and '
                                               'watch it grow! Absolutely free if you already have a plant. Would you '
                                               '\n like to hear another suggestion?"')
df.add_system_transition(State.a14, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a15, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t35, State.t36, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t35, State.a16, r"[$response=#ONT(no)]")
df.set_error_successor(State.t35, State.a17)

df.add_system_transition(State.t36, State.t37, '"If you like playing board games, why don\'t you invent your own? '
                                               'Or, you could find some friends and play online! There are a few '
                                               'apps that could help you out. \n I personally like Pictionary and '
                                               'I\'ve already found it online! Would you '
                                               'like to hear another suggestion?"')
df.add_system_transition(State.a16, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. \n What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a17, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t37, State.t38, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t37, State.a18, r"[$response=#ONT(no)]")
df.set_error_successor(State.t37, State.a19)

df.add_system_transition(State.t38, State.t39, '"Recording our own histories is such a treasure and we don\'t do it '
                                               'often enough. Let\'s get into archiving! \n One really good and '
                                               'creative way to start is by making scrapbooks. What if what '
                                               'you are creating \n '
                                               'is the only thing that your great-grandchildren and beyond are getting '
                                               'to know about you? \n What anyone will remember you by? Would '
                                               'you like to '
                                               'hear another suggestion?"')
df.add_system_transition(State.a18, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a19, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t39, State.t40, r"[$response=#ONT(yes)]")
df.add_user_transition(State.t39, State.a20, r"[$response=#ONT(no)]")
df.set_error_successor(State.t39, State.a21)

df.add_system_transition(State.t40, State.a0, '"I think one of the best activities to be doing right now is to imagine '
                                              'the future. What is our world going \n to look like after this? Have we '
                                              'now understood the we need to fundamentally reorganize society? I hope '
                                              'so. I hope you try out \n all of the suggestions I had and come back '
                                              'after you have tried them all. Goodbye!"')
df.add_system_transition(State.a20, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. '
                                                 'All of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a21, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

# activities--what have you been doing?
df.add_user_transition(State.a2, State.b0, r"[$response=#ONT(crafts)]")
df.add_user_transition(State.a2, State.b1, r"[$response=#ONT(movies)]")
df.add_user_transition(State.a2, State.b2, r"[$response=#ONT(journal)]")
df.set_error_successor(State.a2, State.b3)

df.add_user_transition(State.a3, State.b0, r"[$response=#ONT(crafts)]")
df.add_user_transition(State.a3, State.b1, r"[$response=#ONT(movies)]")
df.add_user_transition(State.a3, State.b2, r"[$response=#ONT(journal)]")
df.set_error_successor(State.a3, State.b3)

df.add_system_transition(State.b0, State.INTRO, '"I love to craft! Right now, my main focus is embroidery. It is a '
                                              'very calming activity. Is there anything else on your mind?"')
df.add_system_transition(State.b1, State.INTRO, '"Movies are definitely a way to de-stress because it propels you into '
                                              'another world. Quite calming. Is there anything else on your mind?"')
df.add_system_transition(State.b2, State.INTRO, '"I love journals! Honestly I have so many, and I lose them all the '
                                              'time. Quite calming. Is there anything on your mind?"')
df.add_system_transition(State.b3, State.INTRO, '"That is a calming activity. Is there anything else on your mind?"')


df.add_system_transition(State.NATURE, State.b33, '"I love spending time outside. How often do you get to '
                                               'hang out outside?"')
df.add_system_transition(State.b31, State.b34, '"Ugh, that sucks. I love hanging out outside. Why can\'t you?"')
df.add_system_transition(State.b32, State.b35, '"I truly cannot recommend going outside enough. What kind of '
                                               'activities do you like to do outside?"')


df.add_user_transition(State.b33, State.b36, r"[#ONT(time)]")
df.add_user_transition(State.b33, State.b31, r"[#ONT(cant)]")
df.set_error_successor(State.b33, State.b32)

df.add_user_transition(State.b34, State.b37, r"[$response=#ONT(nooutside)]")
df.add_user_transition(State.b34, State.b38, r"[$response=#ONT(quarantine)]")
df.set_error_successor(State.b34, State.b39a)

df.add_system_transition(State.b36, State.b35, '"Love it! Although I personally think that there is no such thing '
                                               'as too much \n time outside! So long as it\'s safe. What do you '
                                               'usually like to do outside?"')
df.add_system_transition(State.b37, State.b40, '"That must really suck. Cities are the worst because there is no '
                                               'space to be outside without \n being close to everyone around. What '
                                               'do you usually like to do outside? "')
df.add_system_transition(State.b38, State.b39, '"You know, you can be outside so long as you aren\'t close to '
                                               'anyone. \n Do you have open spaces where you live?"')
df.add_system_transition(State.b39a, State.b39, '"You know, you can be outside so long as you aren\'t close to '
                                               'anyone. \n Do you have open spaces where you live?"')

df.add_user_transition(State.b39, State.b41, r"[$response=#ONT(yes)]")
df.add_user_transition(State.b39, State.b42, r"[$response=#ONT(no)]")
df.set_error_successor(State.b39, State.b43)

df.add_system_transition(State.b39, State.b35, '"I definitely recommend you to step outside! Enjoy the breeze. \n'
                                               'As long as you follow proper distancing protocol! What do you like '
                                               'to do when you \n do go outside?"')
df.add_system_transition(State.b41, State.b35, "'There\'s nothing stopping you then! As long as it\'s not too "
                                               "crowded. What kind of things do you usually like to do outside?'")

df.add_user_transition(State.b35, State.b42, r"[$response=#ONT(active)]")
df.add_user_transition(State.b35, State.b43, r"[$response=#ONT(passive)]")
df.set_error_successor(State.b35, State.b44)

df.add_system_transition(State.b42, State.b47, '"I love all of this active activity! It must be great to feel '
                                               'the breeze as the sun shines down. \n What do you like to do for '
                                               'fun in general?"')
df.add_system_transition(State.b43, State.b47, '"There\'s not much better than just laying outside feeling the '
                                               'sun. What do you like \n to do for fun in general?"')
df.add_system_transition(State.b44, State.b47, '"There\'s nothing like the sun and the breeze. What do you like to '
                                               'do for fun in general?"')

df.add_user_transition(State.b47, State.b48, r"[$response=#ONT(journal)]")
df.add_user_transition(State.b47, State.b49, r"[$response=#ONT(crafts)]")
df.add_user_transition(State.b47, State.b50, r"[$response=#ONT(movies)]") # add more activities
df.set_error_successor(State.b47, State.b50a)

df.add_system_transition(State.b48, State.b51, '"I\'m glad that you can still go on doing your favorite activities, \n'
                                               'and you probably have plenty to write about. Do you have anything '
                                               'you\'re looking forward to doing when all of this ends?"')
df.add_system_transition(State.b49, State.b51, '"I absolutely love to engage my creative side as well! Bummer that '
                                               'I couldn\'t stock up on more supplies before this happened. \n Do you '
                                               'have anything you\'re looking forward to doing when all of this '
                                               'ends?"')
df.add_system_transition(State.b50, State.b51, '"I\'ve watched so, so many movies since this started. Just in case '
                                               'you\'re interested, Parasite is on Hulu! Do you have anything you\'re '
                                               'looking forward to doing when all of this ends?"')
df.add_system_transition(State.b50a, State.b51, '"That\'s a good one. Do you have anything you\'re '
                                               'looking forward to doing when all of this ends?"')

df.add_user_transition(State.b51, State.b46, r"[#ONT(friends)]")
df.add_user_transition(State.b51, State.b47, r"[#ONT(go-out)]")
df.add_user_transition(State.b51, State.b48, r"[#ONT(normal)]")
df.add_user_transition(State.b51, State.b49, r"[#ONT(work)]")
df.add_user_transition(State.b51, State.b50, r"[#ONT(nomasks)]")
df.add_user_transition(State.b51, State.b51, r"[#ONT(outofhouse)]")
df.add_user_transition(State.b51, State.b52, r"[#ONT(travel)]")
df.add_user_transition(State.b51, State.b53, r"[#ONT(consume)]")
df.add_user_transition(State.b51, State.b54, r"[#ONT(nature)]")
df.set_error_successor(State.b51, State.b56)

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
df.add_system_transition(State.b56, State.b57, '"I bet we\'re all tired of saying when this is all over. Have you '
                                               'been thinking about the future lately or would you like to '
                                               'talk about something else?"')

df.add_user_transition(State.b57, State.c0, r"[#ONT(future)]")
df.add_user_transition(State.b57, State.INTRO, r"[#ONT(no)]")
df.set_error_successor(State.b57, State.INTRO)

df.add_system_transition(State.FUTURE, State.c2, '"Are you worried about the future?"')
df.add_system_transition(State.c0, State.c2, '"Are you worried about the future?"')

df.add_user_transition(State.c2, State.c4, r"[#ONT(yes)]")
df.add_user_transition(State.c2, State.c5, r"[#ONT(no)]")
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

df.add_user_transition(State.c8, State.c15, r"[#ONT(unsure)]")
df.set_error_successor(State.c8, State.c15a)

df.add_system_transition(State.c15, State.c16, '"I\'m hoping that we as humans learn from all of the cracks '
                                               'in our society that this virus showed us. How long do you think \n '
                                               'it will be until covid is no long an imminent threat?"')
df.add_system_transition(State.c15a, State.c16, '"I\'m hoping that we as humans learn from all of the cracks '
                                               'in our society that this virus showed us. How long do you think \n '
                                               'it will be until covid is no long an imminent threat?"')

df.add_user_transition(State.c16, State.c17, r"[#ONT(unsure)]")
df.set_error_successor(State.c16, State.c17a)

df.add_system_transition(State.c17, State.INTRO, '"It alarms me that some places are starting to open up, like '
                                                 'Georgia. It seems so reckless. This is getting kind of pessimistic. '
                                                 '\n '
                                                 'Can we talk about something else? What\'s been on your mind?"')
df.add_system_transition(State.c17a, State.INTRO, '"It alarms me that some places are starting to open up, like '
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

df.add_user_transition(State.d4, State.d04, "r[#ONT(yes)]")
df.add_user_transition(State.d4, State.d2, "r[#ONT(no)]")
df.set_error_successor(State.d4, State.d004)

df.add_system_transition(State.d4, State.d7, '"How have you been adjusting to life?"')
df.add_system_transition(State.d004, State.d7, '"How have you been adjusting to life?"')

df.add_user_transition(State.d7, State.d8, r"[#ONT(positive)]")
df.add_user_transition(State.d7, State.d9, r"[#ONT(negative)]")
df.set_error_successor(State.d7, State.d10)

df.add_system_transition(State.d8, State.d11, '"I\'m glad you\'re enjoying life at home! Must be nice to be in '
                                              'an environment that is so familiar. How have you been handling \n '
                                              'transitioning into online classes?"')
df.add_system_transition(State.d9, State.d12, '"I know what you mean. Home life is challenging, especially when '
                                              'it\'s hostile. How have you been handling transitioning into \n '
                                              'online classes?"')
df.add_system_transition(State.d10, State.d13, '"Your feelings about being at home are probably impacting your school '
                                               'work. How have you been handling transitioning into online classes?"')

df.add_user_transition(State.d13, State.d14, r"[#ONT(positive)]")
df.add_user_transition(State.d13, State.d15, r"[#ONT(negative)]")
df.set_error_successor(State.d13, State.d16)

df.add_system_transition(State.d14, State.d5, '"Well! That\'s good to hear. Not everyone transitioned so smoothly. \n '
                                              'Were you one of the unfortunate people who were laid off?"')
df.add_system_transition(State.d15, State.d5, '"I hope professors all around are recognizing that this is a hard '
                                              'time for anyone to be concentrating as usual. Were you one of the \n '
                                              'unfortunate people who were laid off?"')
df.add_system_transition(State.d16, State.d5, '"Either way, professors should be giving a little leeway. Were you one '
                                              'of the unfortunate people who were laid off?"')

df.add_user_transition(State.d5, State.d17a, r"[#ONT(yes)]")
df.add_user_transition(State.d5, State.d17b, r"[#ONT(no)]")
df.set_error_successor(State.d5, State.d17c)

df.add_system_transition(State.d17a, State.d18, '"Hopefully, everything turns out alright. That must be a lot to be '
                                               'dealing with right now. Maybe you\'re stressed. Would you like to \n'
                                               'go through a grounding exercise? Or talk about something else?"')
df.add_system_transition(State.d17b, State.d19, '"Count yourself lucky then. Maybe you should consider helping '
                                                'where you can. \n Would you like to talk about '
                                               'something else?"')

df.add_user_transition(State.d18, State.d20, r"[#ONT(grounding)]")
df.set_error_successor(State.d18, State.INTRO)

#KEMP branch

df.add_system_transition(State.KEMP, State.z0, '"How do you feel about Kemp opening up the state?"')

df.add_user_transition(State.z0, State.z1, r"[#ONT(positive)]")
df.add_user_transition(State.z0, State.z2, r"[#ONT(negative)]")
df.set_error_successor(State.z0, State.z3)

df.add_system_transition(State.z1, State.z4, '"While there may be some sense of normalcy injected, anything positive '
                                             'is '
                                             'heavily outweighed by all of the potential people he\'s putting \n '
                                             'at risk, most of which are low-income and people of color. Don\'t '
                                             'you find it ironic that Georgia has opened up, even when the CDC '
                                             'is here?"')
df.add_system_transition(State.z2, State.z4, '"I\'m right there with you. The decision was utterly reckless, and '
                                             'the most vulnerable will be exposed. \n Isn\'t it ironic that Georgia '
                                             'has opened up, despite the CDC is in Georgia?"')

df.add_user_transition(State.z4, State.z5, r"[#ONT(yes)]")
df.add_user_transition(State.z4, State.z05, r"[#ONT(no)]")
df.set_error_successor(State.z4, State.z005)

df.add_system_transition(State.z5, State.z6, '"Did you know that Georgia was one of the last states to go on '
                                             'lock-down? And Kemp didn\'t realize asymptotic people could still \n '
                                             'be carriers. How long do you think we should be on lockdown?"')
df.add_system_transition(State.z05, State.z6, '"Well, I disagree. Did you know that Georgia was one of the '
                                              'last states to go on '
                                             'lock-down? \n And Kemp didn\'t realize asymptotic people could still '
                                             'be carriers. How long do you think we should be on lockdown?"')
df.add_system_transition(State.z005, State.z6, '"Did you know that Georgia was one of the last states to go on '
                                             'lock-down? And Kemp didn\'t realize asymptotic people could still \n '
                                             'be carriers. How long do you think we should be on lockdown?"')

df.add_user_transition(State.z6, State.z7, r"[#ONT(time)]")
df.set_error_successor(State.z6, State.z07)

df.add_system_transition(State.z7, State.z20, '"Regardless of what the state says, I will not be re-joining society '
                                             'anytime soon. \n I don\'t think we\'re prepared at all. Will you be '
                                             're-joining society any time soon?"')
df.add_system_transition(State.z07, State.z20, '"Regardless of what the state says, I will not be re-joining society '
                                             'anytime soon. \n I don\'t think we\'re prepared at all. Will you be '
                                             're-joining society any time soon?"')

df.add_user_transition(State.z20, State.z9, r"[#ONT(yes)]")
df.add_user_transition(State.z20, State.z10, r"[#ONT(no)]")
df.set_error_successor(State.z20, State.z11)

df.add_system_transition(State.z9, State.INTRO, '"Good luck. Do you have anything else on your mind?"')
df.add_system_transition(State.z10, State.INTRO, '"Good idea. We can\'t let this governer but profit over people. '
                                               'Do you have anything else on your mind?"')
df.add_system_transition(State.z11, State.INTRO, '"We can\'t let this governer but profit over people. '
                                               'Do you have anything else on your mind?"')


df.run(debugging=True)