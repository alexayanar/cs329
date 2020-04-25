from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto


class State(Enum):
    START = auto()
    a0 = auto()
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


ontology = {
    "ontology": {
        "yes": [
            "yeah",
            "yes",
            "cool",
            "ok",
            "okay",
            "k",
            "sounds good",
            "sure",
            "yep",
            "nice",
            "yup",
            "definitely",
            "of course",
            "indeed",
            "aight",
            "alright"
            "yea",
            "i would love to"
        ], "no": [
            "no",
            "nope",
            "not really",
            "don\'t",
            "not",
            "nah"
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
        ], "quarantine": [
            "quarantine", "self-isolation", "social distancing",
            "government", "order", "orders"
        ], "go-out": [
            "going out", "club",
            "clubbing", "bar", "party", "parties",
            "dancing", "dance", "drink", "drinking", "dj"
        ], "friends": [
            "hang out", "chill", "see my friends",
            "see friends", "hit up", "my friends",
            "friends"
        ], "restaurants": [
            "restaurant", "to eat", "eating",
            "food", "order"
        ]

    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

# suggestions loop
df.add_system_transition(State.START, State.t0, '"Would you like to hear some suggestions of fun activities to try?"')

df.add_user_transition(State.t0, State.t1, r"[#ONT(yes)]")
df.add_user_transition(State.t0, State.a0, r"[#ONT(no)]")
df.set_error_successor(State.t0, State.a1)

df.add_system_transition(State.t1, State.t2, '"You should try making some focaccia bread! I recommend topping it with '
                                             'roasted red pepper and garlic. Would you like to hear another '
                                             'suggestion?"')
df.add_system_transition(State.a0, State.a2, '"One and done, huh? I hope you do bake! Baking helps me calm down, \n'
                                             'what are some things that help calm you down?"')
df.add_system_transition(State.a1, State.a3, '"I won\'t keep throwing these at you, but I hope you try it! \n'
                                             'Baking keeps me calm. '
                                             'What are some activities that help calm you down?"')

df.add_user_transition(State.t2, State.t3, r"[#ONT(yes)]")
df.add_user_transition(State.t2, State.a4, r"[#ONT(no)]")
df.set_error_successor(State.t2, State.a6)

df.add_system_transition(State.t3, State.t4, '"I think it\'d be really fun to do a picnic. If you don\'t have your '
                                             'own private outdoor space, try one inside! Especially using spiced '
                                             'fruit--so fresh. Would you like to hear another suggestion?"')
df.add_system_transition(State.a4, State.a2, '"I hope the fresh fruit didn\'t cause the disinterest! \n'
                                             'Since you might not like these '
                                             'suggestions, what activities help calm you down?"')
df.add_system_transition(State.a6, State.a3, '"I could keep going all day! But I won\'t- if you\'re not a fan of \n'
                                             'these suggestions, what activities do you to calm down?"')

df.add_user_transition(State.t4, State.t5, r"[#ONT(yes)]")
df.add_user_transition(State.t4, State.a8, r"[#ONT(no)]")
df.set_error_successor(State.t4, State.a9)

df.add_system_transition(State.t5, State.t6, '"I\'ve had a movie night already--what if you try that? I\'ll even '
                                             'help suggest a movie. What kind of genre do you like?"')
df.add_system_transition(State.a8, State.a2, '"Hate to see you leave so soon, I was about to give movie suggestions! \n'
                                             'What sort of activities do you do ')
df.add_system_transition(State.a9, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                             'activities help me calm down. What activities do you do to calm down?"')

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
df.add_system_transition(State.a10, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a11, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

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
df.add_system_transition(State.a12, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a13, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t33, State.t34, r"[#ONT(yes)]")
df.add_user_transition(State.t33, State.a14, r"[#ONT(no)]")
df.set_error_successor(State.t33, State.a15)

df.add_system_transition(State.t34, State.t35, '"I have wanted to start planting for a long time--maybe now is a '
                                               'good time to start a small herb garden or even get a few plants! '
                                               'Have you ever heard of propogating? It\'s free plants! For a lot '
                                               'of plants, you can cut right below a node and place it in water and '
                                               'watch it grow! Absolutely free if you already have a plant. Would you '
                                               'like to hear another suggestion?"')
df.add_system_transition(State.a14, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a15, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t35, State.t36, r"[#ONT(yes)]")
df.add_user_transition(State.t35, State.a16, r"[#ONT(no)]")
df.set_error_successor(State.t35, State.a17)

df.add_system_transition(State.t36, State.t37, '"If you like playing board games, why don\'t you invent your own? '
                                               'Or, you could find some friends and play online! There are a few '
                                               'apps that could help you out. I personally like Pictionary and '
                                               'I\'ve already found it online! Would you '
                                               'like to hear another suggestion?"')
df.add_system_transition(State.a16, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a17, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t37, State.t38, r"[#ONT(yes)]")
df.add_user_transition(State.t37, State.a18, r"[#ONT(no)]")
df.set_error_successor(State.t37, State.a19)

df.add_system_transition(State.t38, State.t39, '"Recording our own histories is such a treasure and we don\'t do it '
                                               'often enough. Let\'s get into archiving! One really good and creative '
                                               'way to start is by making scrapbooks. What if what you are creating '
                                               'is the only thing that your great-grandchildren and beyond are getting '
                                               'to know about you? What anyone will remember you by? Would you like to '
                                               'hear another suggestion?"')
df.add_system_transition(State.a18, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a19, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

df.add_user_transition(State.t39, State.t40, r"[#ONT(yes)]")
df.add_user_transition(State.t39, State.a20, r"[#ONT(no)]")
df.set_error_successor(State.t39, State.a21)

df.add_system_transition(State.t40, State.a0, '"I think one of the most activities to be doing right now is to imagine '
                                              'the future. What is our world going to look like after this? Have we '
                                              'now understood the we need to fundamentally reorganize society? I hope '
                                              'so. I hope you try out all of the suggestions I had and come back '
                                              'after you have tried them all. Goodbye!"')
df.add_system_transition(State.a20, State.a2, '"You\'ll definitely be kept busy if you follow these suggestions. All '
                                              'of them help me calm down. What sorts of activities do you do to '
                                              'keep you calm?"')
df.add_system_transition(State.a21, State.a3, '"I could keep going all day! But I\'ll spare you. All of these \n'
                                              'activities help me calm down. What activities do you do to calm down?"')

# activities--what have you been doing?
df.add_user_transition(State.a2, State.b0, r"[#ONT(crafts)]") #things that calm you down
df.add_user_transition(State.a2, State.b1, r"[#ONT(movies)]")  # add more things
df.add_user_transition(State.a2, State.b2, r"[#ONT(journal)]")
df.set_error_successor(State.a2, State.b3)

df.add_system_transition(State.b0, State.b20, '"I love to craft! Right now, my main focus is embroidery. Considering '
                                              'that crafting is \n usually indoors, do you spend any time outside?"')
df.add_system_transition(State.b1, State.b20, '"Movies are definitely a way to de-stress because it propels you into '
                                              'another world. Since movies are indoors, do you spend any time '
                                              'outside?"')
df.add_system_transition(State.b2, State.b20, '"I love journals! Honestly I have so many, and I lose them all the '
                                              'time. Since that\'s an indoor activity, \n do you get to spend'
                                              ' any time outside?"')
df.add_system_transition(State.b2, State.b20, '"How fun! Do you get to spend time outside?"')

df.add_user_transition(State.b20, State.b30, r"[#ONT(yes)]")
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
df.add_system_transition(State.b38, State.b39, '"You know, you can be outside so long as you aren\'t close to '
                                               'anyone. \n Do you have open spaces where you live?"')

df.user_transition(State.b39, State.b41, r"[#ONT(yes)]")
df.user_transition(State.b39, State.b42, r"[#ONT(no)]")
df.set_error_successor(State.b39, State.b43)

df.add_system_transition(State.b39, State.b35, '"I definitely recommend you to step outside! Enjoy the breeze. \n'
                                               'As long as you follow proper distancing protocol! What do you like '
                                               'to do when you \n do go outside?"')
df.add_system_transition(State.b41, State.b35, "'There\'s nothing stopping you then! As long as it\'s not too "
                                               "crowded. What kind of things do you usually like to do outside?'")

df.user_transition(State.b35, State.b42, r"[#ONT(active)]")
df.user_transition(State.b35, State.b43, r"[#ONT(passive)]")
df.set_error_successor(State.b41, State.b44)

df.add_system_transition(State.b42, State.b45, '"I love all of this active activity! It must be great to feel '
                                               'the breeze as the sun shines down. \n What do you like to do for '
                                               'fun in general?"')
df.add_system_transition(State.b43, State.b46, '"There\'s not much better than just laying outside feeling the '
                                               'sun. What do you like \n to do for fun in general?"')
df.add_system_transition(State.b44, State.b47, '"There\'s nothing like the sun and the breeze. What do you like to '
                                               'do for fun in general?"')

df.user_transition(State.b45, State.b48, r"[#ONT(journal)]")
df.user_transition(State.b46, State.b49, r"[#ONT(crafts)]")
df.user_transition(State.b47, State.b50, r"[#ONT(movies)]") # add more activities

df.add_system_transition(State.b48, State.b51, '"I\'m glad that you can still go on doing your favorite activities, \n'
                                               'and you probably have plenty to write about. Do you have anything '
                                               'you\'re looking forward to doing when all of this ends?"')
df.add_system_transition(State.b49, State.b52, '"I absolutely love to engage my creative side as well! Bummer that '
                                               'I couldn\'t stock up on more supplies before this happened. \n Do you '
                                               'have anything you\'re looking forward to doing when all of this '
                                               'ends?"')
df.add_system_transition(State.b50, State.b53, '"I\'ve watched so, so many movies since this started. Just in case '
                                               'you\'re interested, Parasite is on Hulu! Do you have anything you\'re '
                                               'looking forward to doing when all of this ends?"')

df.user_transition(State.b51, State.b54, r"[#ONT(friends)]")
df.user_transition(State.b52, State.b55, r"[#ONT(go-out)]")
df.user_transition(State.b53, State.b56)



df.add_user_transition()
if __name__ == '__main__':
    df.run(debugging=False)
