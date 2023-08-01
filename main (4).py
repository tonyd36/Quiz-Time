# Fun Title ASCI Art
print(r"""
 #####                     #######                 ### 
#     # #    # # ######       #    # #    # ###### ### 
#     # #    # #     #        #    # ##  ## #      ### 
#     # #    # #    #         #    # # ## # #####   #  
#   # # #    # #   #          #    # #    # #          
#    #  #    # #  #           #    # #    # #      ### 
 #### #  ####  # ######       #    # #    # ###### ### 
                                                                                  """)

print()
print()

#Introduction to the quiz and instructions
print("Welcome to Quiz Time! You will answer a few True or False questions.")
print("Please ONLY enter the letter T or F when it's your turn to answer. Have fun!")

print()
print()
#Storing questions and answers in a tuple
questions = ("1. Is a kangaroo a marsupial?","2. 12 in. = 1 ft.","3. Grass is red")
answers = ("T","T","F")


#Calculate the number of questions
number_of_questions = len(questions)

#Set the number of correct answers to zero to keep count of the correct answers
#Also setting my userguess input with an empty string to read and store the user's input
correct_answers = 0
user_guess = ""
index = ""

#Create the for loop with each question:
for index in range(1):

  #print function to display the question from the questions tuple from the index
  #Question 1
  print(questions[0])
  user_guess = input("Enter answer: ")
  #While loop to detect if the user entered valid syntax
while user_guess != "T" and user_guess != "F":
      #print(questions[0])
      user_guess = input("Enter answer: ")
  
   #If statement to run when the user enters the correct input to continue with the quiz
if user_guess == answers[0]:
      correct_answers += 1
        
for index in range(1):
    #Print function to display the question from the questions tuple from the index
    #Question 2
      print()
      print(questions[1])
      user_guess = input("Enter answer: ")
  #While loop to detect if the user entered valid syntax
  #while user_guess != "T" and user_guess != "F":
while user_guess != "T" and user_guess != "F":
      user_guess = input("Enter answer: ")
if user_guess == answers[1]:
      correct_answers += 1
      #else:
  #If statement to run when the user enters the correct input to continue with the quiz
    
for index in range(1):
    #Print function to display the question from the questions tuple from the index
    #Question 3
      print()
      print(questions[2])
      user_guess = input("Enter answer: ")
  #While loop to detect if the user entered valid syntax
while user_guess != "T" and user_guess != "F":
      user_guess = input("Enter answer: ")

  #If statement to run when the user enters the correct input to continue with the quiz
if user_guess == answers[2]:
      correct_answers += 1
      print()
  
print()
#Print function to display the number of correct answers
print(f"You got {correct_answers} of 3 correct!")


    
      
  

  
