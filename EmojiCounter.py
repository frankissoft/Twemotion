import csv
import os.path
from os import path
import os
import sched
from datetime import datetime
import time
from datetime import timedelta
import emoji
import regex
from time import sleep

state_ID = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
    }


# emoji_ID = {
#     "U+1F602": "FACE WITH TEARS OF JOY",
#     "2764": "HEAVY BLACK HEART",
#     "267B": "BLACK UNIVERSAL RECYCLING SYMBOL",
#     "U+1F60D": "SMILING FACE WITH HEART-SHAPED EYES",
#     "U+1F62D": "LOUDLY CRYING FACE",
#     "2665": "BLACK HEART SUIT",
#     "U+1F60A": "SMILING FACE WITH SMILING EYES",
#     "U+1F612": "UNAMUSED FACE",
#     "U+1F495": "TWO HEARTS",
#     "U+1F618": "FACE THROWING A KISS",
#     "U+1F629": "WEARY FACE",
#     "263A": "WHITE SMILING FACE",
#     "U+1F614": "PENSIVE FACE",
#     "U+1F601": "GRINNING FACE WITH SMILING EYES",
#     "U+1F44C": "OK HAND SIGN",
#     "U+1F60F": "SMIRKING FACE",
#     "U+1F609": "WINKING FACE",
#     "U+1F44D": "THUMBS UP SIGN",
#     "U+1F605": "SMILING FACE WITH OPEN MOUTH AND COLD SWEAT",
#     "U+1F64F": "PERSON WITH FOLDED HANDS",
#     "U+1F440": "EYES",
#     "U+1F60C": "RELIEVED FACE",
#     "U+1F622": "CRYING FACE",
#     "U+1F494": "BROKEN HEART",
#     "2B05": "LEFTWARDS BLACK ARROW",
#     "U+1F60E": "SMILING FACE WITH SUNGLASSES",
#     "U+1F3B6": "MULTIPLE MUSICAL NOTES",
#     "U+1F499": "BLUE HEART",
#     "U+1F49C": "PURPLE HEART",
#     "2728": "SPARKLES",
#     "U+1F633": "FLUSHED FACE",
#     "U+1F64C": "PERSON RAISING BOTH HANDS IN CELEBRATION",
#     "U+1F525": "FIRE",
#     "U+1F496": "SPARKLING HEART",
#     "U+1F4AF": "HUNDRED POINTS SYMBOL",
#     "U+1F648": "SEE-NO-EVIL MONKEY",
#     "270C": "VICTORY HAND",
#     "U+1F604": "SMILING FACE WITH OPEN MOUTH AND SMILING EYES",
#     "U+1F634": "SLEEPING FACE",
#     "U+1F611": "EXPRESSIONLESS FACE",
#     "U+1F60B": "FACE SAVOURING DELICIOUS FOOD",
#     "U+1F61C": "FACE WITH STUCK-OUT TONGUE AND WINKING EYE",
#     "U+1F62A": "SLEEPY FACE",
#     "U+1F61E": "DISAPPOINTED FACE",
#     "U+1F615": "CONFUSED FACE",
#     "U+1F497": "GROWING HEART",
#     "U+1F44F": "CLAPPING HANDS SIGN",
#     "U+1F610": "NEUTRAL FACE",
#     "U+1F449": "WHITE RIGHT POINTING BACKHAND INDEX",
#     "U+1F49E": "REVOLVING HEARTS"
# }

# emoji_EX = {
#     "U+1F602": 0,
#     "2764": 0,
#     "267B": 0,
#     "U+1F60D": 0,
#     "U+1F62D": 0,
#     "2665": 0,
#     "U+1F60A": 0,
#     "U+1F612": 0,
#     "U+1F495": 0,
#     "U+1F618": 0,
#     "U+1F629": 0,
#     "263A": 0,
#     "U+1F614": 0,
#     "U+1F601": 0,
#     "U+1F44C": 0,
#     "U+1F60F": 0,
#     "U+1F609": 0,
#     "U+1F44D": 0,
#     "U+1F605": 0,
#     "U+1F64F": 0,
#     "U+1F440": 0,
#     "U+1F60C": 0,
#     "U+1F622": 0,
#     "U+1F494": 0,
#     "2B05": 0,
#     "U+1F60E": 0,
#     "U+1F3B6": 0,
#     "U+1F499": 0,
#     "U+1F49C": 0,
#     "2728": 0,
#     "U+1F633": 0,
#     "U+1F64C": 0,
#     "U+1F525": 0,
#     "U+1F496": 0,
#     "U+1F4AF": 0,
#     "U+1F648": 0,
#     "270C": 0,
#     "U+1F604": 0,
#     "U+1F634": 0,
#     "U+1F611": 0,
#     "U+1F60B": 0,
#     "U+1F61C": 0,
#     "U+1F62A": 0,
#     "U+1F61E": 0,
#     "U+1F615": 0,
#     "U+1F497": 0,
#     "U+1F44F": 0,
#     "U+1F610": 0,
#     "U+1F449": 0,
#     "U+1F49E": 0
# }

# emoji_set2 = [
#     "U+1F602",
#     "2764",
#     "267B",
#     "U+1F60D",
#     "U+1F62D",
#     "2665",
#     "U+1F60A",
#     "U+1F612",
#     "U+1F495",
#     "U+1F618",
#     "U+1F629",
#     "263A",
#     "U+1F614",
#     "U+1F601",
#     "U+1F44C",
#     "U+1F60F",
#     "U+1F609",
#     "U+1F44D",
#     "U+1F605",
#     "U+1F64F",
#     "U+1F440",
#     "U+1F60C",
#     "U+1F622",
#     "U+1F494",
#     "2B05",
#     "U+1F60E",
#     "U+1F3B6",
#     "U+1F499",
#     "U+1F49C",
#     "2728",
#     "U+1F633",
#     "U+1F64C",
#     "U+1F525",
#     "U+1F496",
#     "U+1F4AF",
#     "U+1F648",
#     "270C",
#     "U+1F604",
#     "U+1F634",
#     "U+1F611",
#     "U+1F60B",
#     "U+1F61C",
#     "U+1F62A",
#     "U+1F61E",
#     "U+1F615",
#     "U+1F497",
#     "U+1F44F",
#     "U+1F610",
#     "U+1F449",
#     "U+1F49E"
# ]

# emoji_set3 = [
#     "1F602",
#     "2764",
#     "267B",
#     "1F60D",
#     "1F62D",
#     "2665",
#     "1F60A",
#     "1F612",
#     "1F495",
#     "1F618",
#     "1F629",
#     "263A",
#     "1F614",
#     "1F601",
#     "1F44C",
#     "1F60F",
#     "1F609",
#     "1F44D",
#     "1F605",
#     "1F64F",
#     "1F440",
#     "1F60C",
#     "1F622",
#     "1F494",
#     "2B05",
#     "1F60E",
#     "1F3B6",
#     "1F499",
#     "1F49C",
#     "2728",
#     "1F633",
#     "1F64C",
#     "1F525",
#     "1F496",
#     "1F4AF",
#     "1F648",
#     "270C",
#     "1F604",
#     "1F634",
#     "1F611",
#     "1F60B",
#     "1F61C",
#     "1F62A",
#     "1F61E",
#     "1F615",
#     "1F497",
#     "1F44F",
#     "1F610",
#     "1F449",
#     "1F49E"
# ]
emoji_set1 = [
    "\\U0001F602",
    "\\U00002764",
    "\\U0000267B",
    "\\U0001F60D",
    "\\U0001F62D",
    "\\U00002665",
    "\\U0001F60A",
    "\\U0001F612",
    "\\U0001F495",
    "\\U0001F618",
    "\\U0001F629",
    "\\U0000263A",
    "\\U0001F614",
    "\\U0001F601",
    "\\U0001F44C",
    "\\U0001F60F",
    "\\U0001F609",
    "\\U0001F44D",
    "\\U0001F605",
    "\\U0001F64F",
    "\\U0001F440",
    "\\U0001F60C",
    "\\U0001F622",
    "\\U0001F494",
    "\\U00002B05",
    "\\U0001F60E",
    "\\U0001F3B6",
    "\\U0001F499",
    "\\U0001F49C",
    "\\U00002728",
    "\\U0001F633",
    "\\U0001F64C",
    "\\U0001F525",
    "\\U0001F496",
    "\\U0001F4AF",
    "\\U0001F648",
    "\\U0000270C",
    "\\U0001F604",
    "\\U0001F634",
    "\\U0001F611",
    "\\U0001F60B",
    "\\U0001F61C",
    "\\U0001F62A",
    "\\U0001F61E",
    "\\U0001F615",
    "\\U0001F497",
    "\\U0001F44F",
    "\\U0001F610",
    "\\U0001F449",
    "\\U0001F49E"
]

# emoji_set = [
#     "\u1F602",
#     "\u2764",
#     "\u267B",
#     "\u1F60D",
#     "\u1F62D",
#     "\u2665",
#     "\u1F60A",
#     "\u1F612",
#     "\u1F495",
#     "\u1F618",
#     "\u1F629",
#     "\u263A",
#     "\u1F614",
#     "\u1F601",
#     "\u1F44C",
#     "\u1F60F",
#     "\u1F609",
#     "\u1F44D",
#     "\u1F605",
#     "\u1F64F",
#     "\u1F440",
#     "\u1F60C",
#     "\u1F622",
#     "\u1F494",
#     "\u2B05",
#     "\\U0001F60E",
#     "\u1F3B6",
#     "\u1F499",
#     "\u1F49C",
#     "\u2728",
#     "\u0001F633",
#     "\u1F64C",
#     "\u1F525",
#     "\u1F496",
#     "\u1F4AF",
#     "\u1F648",
#     "\u270C",
#     "\u1F604",
#     "\u1F634",
#     "\u1F611",
#     "\u1F60B",
#     "\u1F61C",
#     "\u1F62A",
#     "\u1F61E",
#     "\u1F615",
#     "\u1F497",
#     "\u1F44F",
#     "\u1F610",
#     "\u1F449",
#     "\U0001F49E"
# ]
good_cols = [0, 1, 2, 3, 10, 11, 13, 15]

def text2emoji(text):
    emoji_50 = [0] * 50
    emoji_list = []
    data = regex.findall(r'\X', text)
    if len(data) == 0:
        return False, data
    # print(data)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)
    # print("emoji_list: ", emoji_list)
    # print("emoji_50: ", emoji_50)
    if (len(emoji_list) == 0):
        return False, emoji_list
    for em in emoji_list:
        # print(em.encode('utf-8'))
        # print(em.encode('utf-8').decode('unicode-escape'))
        # x = em.encode('utf-8').decode('unicode-escape')
        # print(em, emoji_set2[0])
        if em in emoji_set2:
            emoji_50[emoji_set2.index(em)] = 1
    if emoji_50 == [0] * 50:
        return False, emoji_list
    print(emoji_50, emoji_list)
    return True, emoji_50

def count(time):

    try:
        with open('GetTweet' + time + '.csv', newline='', encoding='utf-8') as csv_file:
            with open('GetTweet' + time + 'emoji.csv', 'w') as csv_out:
                writer = csv.writer(csv_out)
                for row in csv.reader(csv_file):
                    new_row = []
                    for item in row:
                        # print("Here!")
                        if row.index(item) in good_cols:
                            # print(new_row)
                            new_row.append(item)
                        # print(row[0], row[1])
                        # print("row_size: ", len(row))
                    state = new_row[5]
                    # print("State: ", state)
                    if (state[-3: ] != "USA"):
                        state = state[-2: ]
                    else:
                        state = state_ID[state[:(state.find(','))]]
                    new_row.insert(6, state)


                    TorF, emojilist = text2emoji(new_row[2])
                    if (TorF == False):
                        # print("Here")
                        continue
                    else:
                        print("Here")
                        writer.writerow(new_row + [emojilist])
                        print(emojilist)
    except BaseException as e:
        print("Error on_data: %s" % str(e))

    # with open('some.csv', newline='') as f:
    # reader = csv.reader(f, delimiter="\t")
    # for i, line in enumerate(reader):
    #     print 'line[{}] = {}'.format(i, line)
    #     for row in reader:
    #         print(row)

# def sniff():
#     now = datetime.now()
#     before = now - timedelta(minutes=2)
#     timestr = before.strftime("%Y%m%d%H%M")
#
#     counter = 0
#     working = True
#     while counter < 5 and working:
#         if os.path.isfile('GetTweet' + timestr + '.csv'):
#             count(timestr)
#             working = False
#         else:
#             counter += 1
#             sleep(8)

emoji_set2 = []
for x in emoji_set1:
    a = x.encode('utf-8')
    x = a.decode('unicode-escape')
    emoji_set2.append(x)

for r, d, f in os.walk("."):
    for file in f:
        if file.endswith(".csv"):

            count(file[8: -4])
            # print(file[8: -4])

# while (1):
#     sniff()
#     sleep(10)
#     print(datetime.now())
