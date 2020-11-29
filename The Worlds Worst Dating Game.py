###The World Worst Dating Game###


def introduction():  # Function will make the player introduce themselves and create name and age variable
    global name
    name = input("Welcome, what is your name?")
    if name != "":
        print("Hello {}".format(name))
        global age
        age = int(input("How old are you?"))
        if age < 18:
            print("You are too young to be playing this game")
            introduction()
        else:
            global conf
            conf = (input("So you are {} and are {} years old? Is that correct (Please say yes or no))?".format(name, str(age))).lower())
            if conf == "yes":
                print("Excellent, let's get started!")
                return True
            else:
                print("Let's restart!")
                introduction()
                return False


def routes():  # Character is getting introduced to the available routes of men and girls

    print("We will now introduce to you 1 woman and 1 man")
   
    print("The first person we want to introduce to you is Katja, she loves her naps more than her love life")
    print("She is 22 years old")
    print("The second person we introduce to you is Lucas, he a photographer and he has sweet tooth")
    print("He is 26 years old.")
    print("Lastly, the second person we want to introduce to you is Martin, he works in finance and is a football fan")
    print("He is 23 years old")
    print()
    print()
    print("You have 2 options")
    
    print("1.KATJA      2.Martin       3.Lucas")
    print("Please type a number between 1 and 3")
    print("DISCLAMER: We do not assume your sexual orientation and gender, none of these people are real people.")
    global r_choice
    r_choice = int(input("Your choice?"))
    # r_choice is the route choice variable
   
    if r_choice == 1:
        print("You have chosen Katja")
        return r_choice
    elif r_choice == 2:
        print("You have chosen Martin")
        return r_choice
    elif r_choice == 3:
        print("You have chosen Lucas")
        return r_choice
    else:
        print("Please type a valid number")
        print()
        print()
        print()
        routes()


def failed_approach():
    print("What are you doing? You should have appraoched them... that was a big mistake")
    while True:
        global try_again
        try_again = input("Would you like to try again and start from the beginning? (yes or no)").lower()
        if try_again == "yes":
            return True
        elif try_again == "no":
            return False
        else:
            print("Please select a valid answer")
            continue


def basic_fail():
    print("Now that was a good attempt, but you were just unlucky. I'm sorry buddy")
    global try_again
    while True:
        try_again = input("Would you like to try again and start from the beginning? (yes or no)").lower()
        if try_again == "yes":
            return True
        elif try_again == "no":
            return False



def big_fail():
    print("Wow, that was a big mistake. You have failed this route.")
    print("Now you can either wallow in sadness and quit the game, or try again and start from the beginning")
    global try_again
    while True:
        try_again = input("Would you like to try again and start from the beginning? (yes or no)").lower()
        if try_again == "yes":
            return True
        elif try_again == "no":
            return False
        else:
            print("Please select a valid answer")
            continue


def congratulations():
    print("Congratulations, you absolute mad lad, you did it.")
    print("Capturing a woman's heart is no easy task.")
    global play_again
    play_again = input("Would you like to play again").lower()
    if play_again == "yes".lower():
        return True
    elif play_again == "no":
        return False



#KATJA Route

def katja_meet():

    print("You go to the library and see a person that interests you. She is studying and trying not to fall asleep.")
    print("Your getting nervous wondering whether you should approach her or not.")
    print("You build up the courage and go to her")
    print("What is your opening line?")
    print("1.Hey, are you alright? You seem kind of tired       2.Hey baby gurl, I'm trynna get yo numba")
    print("3. *Sit down next to her*")
    global k_choice1
    k_choice1=int(input("Choose a number between 1 and 3"))
    if k_choice1 == 1:
        print("Girl: Huh? Haha, yea... my finals are coming up so I'm a bit stressd. Could you please leave me alone?")
        return k_choice1
    elif k_choice1 == 2:
        print("Girl: *Leaves and calls the librarian on you*")
        return k_choice1
    elif k_choice1 == 3:
        print("Girl: Hi")
        print("{}: Hi, what are you doing?".format(name))
        print("Girl: I'm sorry, but I'm studying for my finals")


# MARTIN ROUTE

def martin_meet():  # Path 1
    print("Your friends have convinced you to go to the club, and you see this guy dancing alone.")
    print("You are given a choice")
    print("1.Approach him        2.Not approach him")
    while True:
        global m_choice1
        m_choice1 = int(input("Would you like to approach him or not? (Choose number 1 or 2)"))
        if m_choice1 == 1:
            return m_choice1
        elif m_choice1 == 2:  # FAIL ROUTE if m_choice1 = 2
            return m_choice1
        else:
            print("Please type in a valid number")
            continue


def martin_ask_out():  # Path 2
    print("You head on over to the guy and ask him for his name")
    print("He smiles and tells you 'My name is Martin'")
    print("You dance with him and you find out about how interesting he is and want to ask him out on a date")
    print("You can choose what you want to do")
    print("1.Do nothing                             2.Ask him out to a restaurant")
    print("3.Ask him out to your place right now   ")
    global m_choice2
    m_choice2 = int(input("Which option would you like to choose?"))
    if m_choice2 == 1:  # FAIL ROUTE if m_choice2 = 1
        print("{}: Okay bye".format(name))
        return m_choice2
    elif m_choice2 == 2:
        print("{}: How about we go on a date at a restaurant?".format(name))
        print("Martin: Yea that sounds lovely, how does Friday sound?")
        print("{}: sure".format(name))
        return m_choice2
    elif m_choice2 == 3:  # FAIL ROUTE if m_choice2 = 3
        print("{}: How about we go to my place right now")
        print("Martin: Oh I don't know about that, I'm not that kind of guy sorry.")



def martin_restaurant():
    print("Days have passed, and you have been preparing for your date, not knowing what to expect")
    print("You are nervous and arrive 30 minutes early")
    print("Martin: Hey there, have you been here for a long time?")
    print("{}: 1. No I just arrived here as well        2.Took you long enough".format(name))
    global m_choice3_1
    m_choice3_1= int(input("Choose an appropriate answer:"))
    if m_choice3_1 == 1:
        print("{}: No I just arrived here as well")
        print("Martin: Thank god, don't wanna leave my first date hanging. I got divorced 3 weeks ago")
        return m_choice3_1
    elif m_choice3_1 == 2: #FAIL ROUTE
        print("{}: Took you long enough")
        print("Martin: Alright then, I guess you can wait a bit longer for someone to return")
        return m_choice3_1

def sass():
    print("That was excessively sassy")
    print("how dare you?")
    global try_again
    while True:
        try_again = input("Would you like to try again and start from the beginning? (yes or no)").lower()
        if try_again == "yes":
            return True
        elif try_again == "no":
            return False
        else:
            print("Please select a valid answer")
            continue


def martin_psycho():
    print("{}: Divorce?".format(name))
    print("Martin: Yea... It's hard on me...")
    print("{}: Why did you get divorced? *you start to feel a bit awkward and I don't blame you*".format(name))
    print("Martin: Murdering our dog")
    print("You are given new options")
    print("1. Go to the 'bathroom'          2. Settle for him")
    global m_choice3_2
    m_choice3_2 = int(input("Choose option 1 or 2"))
    if m_choice3_2 == 1:
        print("{}: I gotta use the bathroom for a second, it won't be long".format(name))
        print("Martin: Don't worry that is fine")
        print("{}: Thank you".format(name))
        print("You approach the bathroom and you leave like there is no tomorrow")
        return m_choice3_2
    if m_choice3_2 == 2:
        print("{}: Wow, your ex is overacting much?".format(name))
        print("Martin: Thanks for understanding")
        print("*3 Hours pass and you are walking Martin home")
        print("{}: Today was amazing, want to do it again?".format(name))
        print("Martin: Yea sure, how about we have dinner at my place next time?")
        print("{}Sound amazing".format(name))
        return m_choice3_2

def martin_run():
    print("Whew, you avoided a big red flag, congratulations")
    print("Dating isn't about getting with someone, it's to know fo who and when to get with someone")
    print("in this case, running was the right decision, who knows what could've happened")
    while True:
        global try_again
        try_again = input("Would you like to play again and start from the beginning? (yes or no)").lower()
        if try_again == "yes":
            return True
        elif try_again == "no":
            return False
        else:
            print("Please select a valid answer")
            continue


def martin_settle():
    print("Years have passed and you managed to marry him and died after 9 years of wonderful marriage")
    print("you turned {}".format(age+5))
    print("You died from bleeding out due to stabbing wounds induced by your husband")
    print("Why did you not run when you got saw the red flag? Idiot")
    while True:
        global try_again
        try_again = input("Would you like to try again and start from the beginning? (yes or no)").lower()
        if try_again == "yes":
            return True
        elif try_again == "no":
            return False
        else:
            print("Please select a valid answer")
            continue

# LUCAS ROUTE

def lucas_meet():
    print("You decided to prepare a christmas dinner with your friends and your friend decided to invite Lucas who catched your attention")
    print("At first he doesn't seem like a catch but then you realise you got no other chance for a long long time. You are given a choice.")
    print()
    print("How would you try to get his attention?")
    print("1.Try to express him with your fortnite dances    2.Yeet him off the roof    3.Get on with your day")
    while True:
        global m_choice1
        m_choice1 = int(input("(Choose an answer from 1 to 3): "))
        if m_choice1 == 1:
            return m_choice1
        elif m_choice1 == 2: # m_choice1 == 2 Fail 
            print("Uhh... I honestly don't know what you expected to happen... try not to drop the soap")
            return m_choice1 # m_choice1 == 3 Fail 
        elif m_choice1 == 3: 
            print("You deserve way more better than that pathetic potato sack anyway.... smh...")
            return m_choice1
        else:
            print("Please type in a valid number")
            continue

def lucas_fortnitedance(): 
    print("After witnessing your stunning floss and after getting the attention of the whole room, you lock eyes with him and it really seems like it worked for ya huh... strange...  ")
    print("He approaches you and compliments your sick a** dancing skills as an opener and he says: ")
    print("Lucas: Whoa that was stunning! I really need you to teach me how to floss broouuh")
    print("You get a little surprised by the way he talks considering his age but keep the conversation going")
    print("{}: Yeah I know, I used to play fortnite profesionally so it really is nothing for me")
    print("Lucas: Aren't you a bit old to play fortnite?")
    print("{}: What!? I'm just" + format(age) + "what's wrong with it?")
    print("Lucas: I mean... You're right I'm 26 and I play Robloxon Pro League all day long")
    print("After a short conversation he asked you to watch Avatar The Last Airbender one day")
    print()
    print("What would be your response?")
    print("1.Accept it and call him flameo hotman from now on    2.You rather destroy a cart of cabbages...")
    while True:
        global m_choice2
        m_choice2 = int(input("(Choose an answer. 1 or 2): "))
        if m_choice2 == 1:
            return m_choice2
        elif m_choice2 == 2: # m_choice2 == 2 Fail
            print("You can always watch ATLA by yourself! ps. Multiple times a year!")
            return m_choice2
        else:
            print("Please type in a valid number")
            continue
        
def lucas_atla():
    print("You meet up with him infront of your house, hop into his car and realise darude sandstorm playing continously on his radio but you play it cool ")
    print("You arrive to his place and turn on the TV to watch some good quality Avatar The Last Airbender")
    print("However, as he sets the TV up you realise he starts to open the ATLA Live Action Movie... Your blood instantly freezes and your PTSDs start showing back up")
    print()
    print("You can either 1.'start running away' or 'try to get through that torture to achieve your ultimate goal' ")
    while True:
        global m_choice3
        m_choice3 = int(input("(Choose an answer. 1 or 2): "))
        if m_choice3 == 1:
            return m_choice2
        elif m_choice3 == 2: # m_choice3 == 2 Fail
            print("Not a single experience in this WORLD IS WORTH SEEING THE LIVE ACTION AGAIN")
            return m_choice2
        else:
            print("Please type in a valid number")
            continue
        
def lucas_runaway():
    print("You start to run to the door while trying to pack away your stuff and he asks you what's wrong")
    print("You shout: I RATHER GO TO BRAZIL")
    print("{}: What's wrong with me?! NO! What the hell is wrong with you? How can you put the live action without feeling pain, you masochist?!")
    print("After you flee his house you learn a valuable lesson not to date anyone who plays roblox.")
    while True:
        global try_again
        try_again = input("Would you like to try again and start from the beginning? (yes or no)").lower()
        if try_again == "yes":
            return True
        elif try_again == "no":
            return False
        else:
            print("Please select a valid answer")
            continue

while True:
    introduction()
    routes()
    if r_choice == 1:
        katja_meet()
        if k_choice1 == 1:
            basic_fail()
            if try_again == "no":
                break
        elif k_choice1 == 2:
            big_fail()
            if try_again == "no":
                break
        elif k_choice1 == 3:
            basic_fail()
            if try_again == "no":
                break
    elif r_choice == 2:
        martin_meet()
        if m_choice1 == 1:
            martin_ask_out()
            if m_choice2 == 1:
                big_fail()
                if try_again == "no":
                    break
            elif m_choice2 == 2:
                martin_restaurant()
                if m_choice3_1 == 1:
                    martin_psycho()
                    if m_choice3_2 == 1:
                        martin_run()
                        if try_again == "no":
                            break
                    elif m_choice3_2 == 2:
                        martin_settle()
                        if try_again == "no":
                            break
                if m_choice3_1 == 2:
                    sass()
                    if try_again == "no":
                        break
            elif m_choice2 == 3:
                basic_fail()
                if try_again == "no":
                    break
        elif m_choice1 == 2:
            failed_approach()
            if try_again == "no":
                break
    if r_choice == 3:
        martin_meet()
        if m_choice1 == 1:
            martin_ask_out()
            if m_choice2 == 1:
                big_fail()
                if try_again == "no":
                    break
            elif m_choice2 == 2:
                martin_restaurant()
                if m_choice3_1 == 1:
                    martin_psycho()
                    if m_choice3_2 == 1:
                        martin_run()
                        if try_again == "no":
                            break            















