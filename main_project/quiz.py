questions = ("1. When was the first iPod released? ",
             "2. Which continent covers all four hemispheres of the earth? ",
             "3. Who was the youngest U.S. president? ",
             "4. What are California’s state colors? ",
             "5. What is the currency of Poland? ")
options = (("A) 2001", "B) 2007", "C) 2009"),
           ("A) Asia", "B) Europe", "C) Africa"),
           ("A) Theodore Roosevelt", "B) Joe Biden", "C) George Washington"),
           ("A) Black and Red", "B) White and Gold", "C) Blue and Gold"),
           ("A) Zloty", "B) Dollar", "C) Rubles"))

correct = ("A", "C", "A", "C", "A")
answers = []

a_limit = 3
a_count = 0

score = 0
question_nmb = 0

for question in questions:
    print("-------------------")
    print(question)
    
    for option in options[question_nmb]:
        print(option)
    
    answer = input("Enter ur variants here (A, B, C): ").upper()
    answers.append(answer)

    if answer == correct[question_nmb]:
        score += 1
        print("Good job!")
    
    elif answer == "":
        print("Plaese enter a normal answer.")
        answer = input("Enter ur variants here (A, B, C, D): ").upper()


    elif answer != correct[question_nmb]:
        a_count += 1
        print(f"Incorrect. Answer: {correct[question_nmb]}. UR answer is: {answer}")

    elif a_count > a_limit:
        print("Ur failed!")
        break

    question_nmb += 1

print("-------")
print("RESULTS")
print("-------")

print("answers:", end=" ")
for cor in correct:
    print(cor, end=" ")
print()

print("ur answers:", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

score = int(score / len(questions) * 100)

if cor == ans:
    print(f"Perfect! Your score: {score}%")
else:
    print(f"Good! Your score: {score}%")
