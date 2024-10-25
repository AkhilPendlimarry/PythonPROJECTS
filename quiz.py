import random
import operator 

# Defining the operators
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod
}

def question():
    # generates random questions 
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operatorSymbol = random.choice(list(operators.keys()))  # Randomly picks up an operator


    # Creating the question string
    question_text = f"{num1} {operatorSymbol} {num2}"
    
    # Calculating the answer using the selected operator
    answer = operators[operatorSymbol](num1, num2)
    
    # If it's a division question, round the answer to 2 decimal places
    if operatorSymbol == '/':
        answer = round(answer, 2)
    
    return question_text, answer

def save_results(name, score):
    #Saving the user's name and score into a text file.
    with open("quiz_results.txt", "a") as file:
        file.write(f"Name: {name}, Score: {score}\n")

def quiz():
    name = input("Enter your name: ")  # Get the user's name
    total_questions = 10  # initial number of questions taken to 10
    
    while True:
        score = 0
        print(f"Hello {name}, Welcome to the math quiz!!! Answer the following questions:\n")

        for i in range(total_questions):
            question_text, correct_answer = question()
            print(f"Question {i+1}: {question_text} = ?")
            
            try:
                user_answer = float(input("Your answer: "))
                
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect! The correct answer is {correct_answer}")
            except ValueError:
                print(f"Invalid input! The correct answer was {correct_answer}")
            
            print()

        # Display final score
        print(f"Quiz finished! Your score: {score}/{total_questions}")
        
        # Save the results in a text file
        save_results(name, score)
        print(f"Your score has been saved, {name}!\n")

        # Ask the user if they want to continue the quiz
        continue_quiz = input("Do you want to continue? (Y/N): ").strip().upper()
        
        if continue_quiz == 'N':
            print("Thank you for playing! Exiting the quiz.")
            break  # Exit the quiz if the user selects 'N'
        elif continue_quiz == 'Y':
            print("Starting a new quiz...\n")
        else:
            print("Invalid input! Exiting the quiz.")
            break  # Exit if the input is neither 'Y' nor 'N'

quiz()
