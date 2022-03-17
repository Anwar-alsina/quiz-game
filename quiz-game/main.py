# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments  
quiz = {
    1 : {
        "question" : "Who was able to pick up Thor’s hammer in Endgame?",
        "answer" : "Captain America",
         "choices" : ['1. Captain America', '2. Thor', '3. Iron man', '4. Hulk']
    },
    2 : {
        "question" : "In which movie did Spider-Man make his first appearance in the MCU?",
        "answer" : "Captain America:Civil War",
        "choices" : ['1. Captain America:Civil War', '2. Thor', '3. Iron man', '4. Hulk']
    },
    3 : {
        "question" : "Wanda and her brother Pietro are from where?",
        "answer" : "Sokovia",
        "choices" : ['1. Wakanda', '2. Brooklyn', '3. Sokovia', '4. Germany']
    },
    4 : {
        "question" : "Whose power exceeds that of the Sorcerer Supreme?",
        "answer" : "Scarlet Witch",
        "choices" : ['1. Wandavision', '2. Thor', '3. Scarlet Witch', '4. Hulk']
    },
    5 : {
        "question" : "Who does Loki accidentally kill when directing the Dark Elves to the staircase on the left?",
        "answer" : "Frigga",
        "choices" : ['1. Captain America', '2. Frigga', '3. Iron man', '4. Hulk']
    },
    6 : {
        "question" : "Black Panther is set in which fictional country?",
        "answer" : "Wakanda", 
        "choices" : ['1. Uganda', '2. Atlantis', '3. Wakanda', '4. Bermuda Triangle']
    },
    7 : {
        "question" : "What’s the name of the amulet Doctor Strange wears around his neck?",
        "answer" : "The Eye of Agamoto.",
        "choices" : ['1. The Eye of Agamoto', '2. Infinity Gauntlet', '3. Pym Particle', '4. None of the Above']
    },
    8 : {
        "question" : "What does TVA stand for?",
        "answer" : "Time Variance Authority",
        "choices" : ['1. Tennessee Valley Authority', '2. Time Variance Authority', '3. Tax on Value Added', '4. Hulk']
    },
    9 : {
        "question" : "Who said, “What is grief, if not love persevering?”",
        "answer" : "Vision",
        "choices" : ['1. Hulk', '2. He Who Remains', '3. Vision', '4. Nana']
        
    },
    10 : {
        "question" : "What song is playing in Wong's earbuds in the library?",
        "answer" : "Single Ladies",
        "choices" : ['1. Smoking Out The window', '2. Staying Alive', '3. Single Ladies', '4. Loyal']
    }
}

def check_ans(question,ans, attempts, score):

    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_answers():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    
    print("Welcome to this Marvel Cinematic Universe quiz! \nAre you ready to test your knowledge about Superheros?")
    input("Press any key to start the fun ;) \n")
    return True





intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            print(quiz[question]['choices'])
            answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                print("")
                break
            attempts -= 1
            print("")

    break

print(f"Your final score is {score}!\n\n")
print("Want to know the correct answers? Please see them below! ;)\n")
print_answers()
print("Thanks for playing!")
