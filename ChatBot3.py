def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


print("these are the back up responses:")


class Category:
    def __init__(self, name, triggers, responses):
        self.name = name
        self.triggers = []
        self.responses = []


def chat():
    global categoryList
    categoryList = []
    global mode
    global backup_responses
    global backup_questions
    backup_responses = ["what?", "I don't understand", "huh", "hmmm"]
    backup_questions = ["what do you mean?", "can you explain?", "are you okay?", "???"]
    # ^ to control the conversation
    backup_check = input("Are these back up responses ok, y for yes and n for no")
    if backup_check == "y":
        pass
    elif backup_check == "n":
        new_backups = input("what back up response do you want?")
        backup_responses = str(new_backups)
        backup_responses = backup_responses.split(", ")
        print(backup_responses)

    greeting = input("Choose a greeting")

    where_triggers = input("Input trigger words for 'where' questions")
    where_triggers = where_triggers.split(",")
    where = input("What should I say if they ask a where question")

    when_triggers = input("Input trigger words for 'when' questions")
    when_triggers = when_triggers.split(",")
    when = input("What should I say if they ask a when question")

    want_triggers = input("Input trigger words for 'want' questions")
    want_triggers = want_triggers.split(",")
    want = input("what should I say if they ask a want question")

    how_triggers = input("Input trigger words for 'how' questions")
    how_triggers = how_triggers.split(",")
    how = input("what should I say if they ask a how question")

    what_triggers = input("Input trigger words for 'what' questions")
    what_triggers = what_triggers.split(",")
    what = input("what should I say if they ask a what question")

    why_triggers = input("Input trigger words for 'why' questions")
    why_triggers = why_triggers.split(",")
    why = input("what should I say if they ask a why question")

    who_triggers = input("Input trigger words for 'who' questions")
    who_triggers = who_triggers.split(",")
    who = input("what should I say if they ask a who question")

    #################################################################################################
    mode = input("'Do Not Disturb' Mode: y for yes OR n for no:    ")

    inp = input("Initiate or Wait for Text? Press y then enter for initiate OR n then enter for wait")
    inp = str(inp)
    if inp == "y":
        print(greeting)
    elif inp == "n":
        print("waiting for message! (type quit to stop)!")
    else:
        print("waiting for text, type quit to stop")

    if mode == "y":
        print("DO NOT DISTURB ON")
        while True:
            inp = input("You: ")
            if inp.lower() == "quit":
                break

            msgtimestamp = datetime.datetime.now()
            # print(msgtimestamp.strftime('%H'))

            # for the test phase of the user experience
            if inp == "*ADD*":
                customName = input("What is the name of the category")

                customTriggers = input("What are the trigger words")
                customTriggers = customTriggers.split(",")

                customResponses = input("What are the responses")
                customResponses = customResponses.split(",")

                customCategory = Category(customName, customTriggers, customResponses)

                categoryList.append(customCategory)

                print("CATEGORY ADDED")

            # For testing purposes to print categoryList
            if inp == "*DISPLAY LIST*":
                index = 0
                for i in categoryList:
                    print(categoryList[index].name)
                    index = index + 1

            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]

            if results[results_index] > 0.8:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']

                print(random.choice(responses))

            else:
                where_identified = False
                when_identified = False
                why_identified = False
                what_identified = False
                who_identified = False
                want_identified = False
                how_identified = False

                for i in where_triggers:
                    if i in inp:
                        # print("where found")
                        where_identified = True

                for i in when_triggers:
                    if i in inp:
                        # print("when found")
                        when_identified = True

                for i in why_triggers:
                    if i in inp:
                        # print("why found")
                        why_identified = True

                for i in what_triggers:
                    if i in inp:
                        # print("what found")
                        what_identified = True

                for i in who_triggers:
                    if i in inp:
                        # print("who found")
                        who_identified = True

                for i in want_triggers:
                    if i in inp:
                        # print("want found")
                        want_identified = True

                for i in how_triggers:
                    if i in inp:
                        # print("how found")
                        how_identified = True

                if where_identified == True:
                    print(where)

                elif when_identified == True:
                    print(when)

                elif why_identified == True:
                    print(why)

                elif what_identified == True:
                    print(what)

                elif who_identified == True:
                    print(who)

                elif want_identified == True:
                    print(want)

                elif how_identified == True:
                    print(how)

                else:
                    print(random.choice(backup_responses))
                    time.sleep(3)
                    print(random.choice(backup_questions))

    elif mode == "n":
        print("DO NOT DISTURB OFF")
        while True:
            inp = input("You: ")
            if inp.lower() == "quit":
                break

            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]

            if results[results_index] > 0.8:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']

                print(random.choice(responses))


            else:
                where_identified = False
                when_identified = False

                for i in where_triggers:
                    if i in inp:
                        # print("where found")
                        where_identified = True

                for i in when_triggers:
                    if i in inp:
                        # print("when found")
                        when_identified = True

                if where_identified == True:
                    print(inp)
                    interveneInp = input("\n")

                elif when_identified == True:
                    print(inp)
                    interveneInp = input("\n")