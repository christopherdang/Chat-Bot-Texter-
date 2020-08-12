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


class Category(object):
    name = ""
    triggers = []
    responses = []

    def __init__(self, name, triggers, responses):
        self.name = name
        self.triggers = triggers
        self.responses = responses


def chat():
    global categoryList
    categoryList = []
    global mode
    global backup_responses
    global backup_questions
    backup_responses = ["what?", "I don't understand", "huh", "hmmm"]
    backup_questions = ["what do you mean?", "can you explain?", "are you okay?", "???"]
    # ^ to control the conversation

    # Backup responses
    backup_responses_check = input("Are these back up responses ok, y for yes and n for no")
    if backup_responses_check == "y":
        pass
    elif backup_responses_check == "n":
        new_backup_responses = input("what back up response do you want?: ")
        backup_responses = str(new_backups_responses)
        backup_responses = backup_responses.split(", ")
        print(backup_responses)

    # Backup questions
    backup_questions_check = input("Are these back up questions ok, y for yes and n for no")
    if backup_questions_check == "y":
        pass
    elif backup_questions_check == "n":
        new_backup_questions = input("what back up questions do you want?: ")
        backup_questions = str(new_backup_questions)
        backup_questions = backup_questions.split(", ")
        print(backup_questions)

    greeting = input("Choose a greeting: ")

    where_triggers = input("Input trigger words for 'where' questions: ")
    where_triggers = where_triggers.split(",")
    where = input("What should I say if they ask a where question: ")

    when_triggers = input("Input trigger words for 'when' questions: ")
    when_triggers = when_triggers.split(",")
    when = input("What should I say if they ask a when question: ")

    want_triggers = input("Input trigger words for 'want' questions: ")
    want_triggers = want_triggers.split(",")
    want = input("what should I say if they ask a want question: ")

    how_triggers = input("Input trigger words for 'how' questions: ")
    how_triggers = how_triggers.split(",")
    how = input("what should I say if they ask a how question: ")

    what_triggers = input("Input trigger words for 'what' questions: ")
    what_triggers = what_triggers.split(",")
    what = input("what should I say if they ask a what question: ")

    why_triggers = input("Input trigger words for 'why' questions: ")
    why_triggers = why_triggers.split(",")
    why = input("what should I say if they ask a why question: ")

    who_triggers = input("Input trigger words for 'who' questions: ")
    who_triggers = who_triggers.split(",")
    who = input("what should I say if they ask a who question:  ")

    #################################################################################################
    mode = input("'Do Not Disturb' Mode: y for yes OR n for no: ")

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

                customName = input("What is the name of the category: ")

                listSize = len(categoryList)

                if listSize == 0:
                    customTriggers = input("What are the trigger words: ")
                    customTriggers = customTriggers.split(",")

                    customResponses = input("What are the responses: ")
                    customResponses = customResponses.split(",")

                    customCategory = Category(customName, customTriggers, customResponses)

                    categoryList.append(customCategory)

                    print("CATEGORY ADDED")

                    index = 0
                    for i in categoryList:
                        print("Category Name:" + categoryList[index].name)
                        print("     Triggers:" + categoryList[index].triggers[0])
                        print("     Responses:" + categoryList[index].responses[0])
                        index = index + 1

                else:
                    categoryExist = False

                    for i in categoryList:
                        if customName == i.name:
                            categoryExist = True
                            break

                    if categoryExist == True:
                        print("Category Already Exists")

                    elif categoryExist == False:
                        customTriggers = input("What are the trigger words: ")
                        customTriggers = customTriggers.split(",")

                        customResponses = input("What are the responses: ")
                        customResponses = customResponses.split(",")

                        customCategory = Category(customName, customTriggers, customResponses)

                        categoryList.append(customCategory)

                        print("CATEGORY ADDED")

                        index = 0
                        for i in categoryList:
                            print("Category Name:" + categoryList[index].name)
                            print("     Triggers:" + categoryList[index].triggers[0])
                            print("     Responses:" + categoryList[index].responses[0])
                            index = index + 1

            # Print categoryList
            elif inp == "*LIST*":
                listSize = len(categoryList)

                if listSize == 0:
                    print("List does not contain any categories")

                else:
                    index = 0
                    for i in categoryList:
                        print("Category Name:" + categoryList[index].name)
                        print("     Triggers:" + categoryList[index].triggers[0])
                        print("     Responses:" + categoryList[index].responses[0])
                        index = index + 1

            # Remove categories from the list
            elif inp == "*REM*":

                index = 0
                for i in categoryList:
                    print("Category Name:" + categoryList[index].name)
                    print("     Triggers:" + categoryList[index].triggers[0])
                    print("     Responses:" + categoryList[index].responses[0])
                    index = index + 1

                remCategory = input("What category would you like to remove: ")

                categoryExist = False

                for i in categoryList:
                    if remCategory == i.name:
                        categoryList.remove(i)
                        categoryExist = True
                        print("Category removed successfully")

                        index = 0
                        for i in categoryList:
                            print("Category Name:" + categoryList[index].name)
                            print("     Triggers:" + categoryList[index].triggers[0])
                            print("     Responses:" + categoryList[index].responses[0])
                            index = index + 1

                        break

                if categoryList == False:
                    print("Category does not exist")

            # Edit categories
            elif inp == "*EDIT*":
                index = 0
            for i in categoryList:
                print("Category Name:" + categoryList[index].name)
                print("     Triggers:" + categoryList[index].triggers[0])
                print("     Responses:" + categoryList[index].responses[0])
                index = index + 1

                editCategory = input("What category would you like to edit: ")

                categoryExist = False

                for i in categoryList:
                    if editCategory == i.name:
                        categoryExist = True
                        break

                if categoryExist == False:
                    print("Category does not exist")

                elif categoryExist == True:
                    for i in categoryList:
                        if editCategory == i.name:
                            categoryList.remove(i)
                            break

                    newTriggers = input("What are the new trigger words: ")
                    newTriggers = newTriggers.split(",")

                    newResponses = input("What are the new responses: ")
                    newResponses = newResponses.split(",")

                    newCategory = Category(editCategory, newTriggers, newResponses)

                    categoryList.append(newCategory)

                    print("CATEGORY ADDED")

                    index = 0
                    for i in categoryList:
                        print("Category Name:" + categoryList[index].name)
                        print("     Triggers:" + categoryList[index].triggers[0])
                        print("     Responses:" + categoryList[index].responses[0])
                        index = index + 1

            # Bot responses, not actual commands
            else:
                results = model.predict([bag_of_words(inp, words)])[0]
                results_index = numpy.argmax(results)
                tag = labels[results_index]

                if results[results_index] > 0.8:
                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']

                    print(random.choice(responses))

                else:
                    list_identified = False

                    where_identified = False
                    when_identified = False
                    why_identified = False
                    what_identified = False
                    who_identified = False
                    want_identified = False
                    how_identified = False

                    ##### needs to make the loops run when a sentence containing the trigger words are present, just like the functional defaults
                    for i in categoryList:
                        # print("First loop run")
                        pass
                        for j in i.triggers:
                            # print("Second loop run")
                            pass
                            if j in inp:
                                # print("Customizable trigger found")
                                list_identified = True

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

                    if list_identified == True:
                        for i in categoryList:
                            # print("First loop run")
                            for j in i.triggers:
                                # print("Second loop run")
                                if j in inp:
                                    print("Customizable trigger found")
                                    print(i.responses[0])

                    elif where_identified == True:
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
                        time.sleep(2)
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