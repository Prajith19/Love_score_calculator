print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_lower = name1.lower()
name2_lower = name2.lower()
check = name1_lower + name2_lower

ty = check.count("t")
ry = check.count("r")
uy = check.count("u")
ey = check.count("e")

first_total = ty + ry + uy + ey
first_total_string = str(first_total)

ly = check.count("l")
oy = check.count("o")
vy = check.count("v")

second_total = ly + oy + vy + ey
second_total_string = str(second_total)

love_score = first_total_string + second_total_string
love_score_int = int(love_score)

if love_score_int < 10 or love_score_int > 90:
    print(f"Your score is {love_score_int}, you go together like coke and mentos.")
elif love_score_int >= 40 and love_score_int <= 50:
    print(f"Your score is {love_score_int}, you are alright together.")
else:
    print(f"Your score is {love_score_int}.")
