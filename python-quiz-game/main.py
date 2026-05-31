def python_quiz():
    questions={
        "Who created Python?":"Guido van Rossum",
        "Which function is used to take input from the user?":"input",
        "Which function is used to display output?":"Print",
        "What symbol is used for comments in Python?":"#",
        "How do you define a function in Python?":"def",
        "Which statement is used to import a module?":"import",
        "What is OOP?":"Object-Oriented Programming",
        "What is the output of print(min(5, 2, 9))?":"2",
        "What is the output of print(abs(-10))?":"10",
        "What is the output of print(2 ** 3)":"8",
    }
    score=0
    for question,answer in questions.items():
        user_answer=input(f"\n{question}\nYour answer:").strip().lower()
        
        if user_answer==answer.strip().lower():
            print("Correct")
            score+=1
        else:
            print(f"wrong \ncorrect answer:{answer}")
    total=len(questions)
    print(f"\nyour score:{score}/{total}")

    if score >=5:
        print("Good Job")
    else:
        print("Keep Practicing")


python_quiz()

