def scoresAndGrades():
    import random
    print "Scores and Grades"
    for x in range(1, 11):
        random_num = random.random()*40+60
        if random_num >= 90:
            print "Score: " + str(random_num) + "; Your grade is A"
        elif random_num >= 80:
            print "Score: " + str(random_num) + "; Your grade is B"
        elif random_num >= 70:
            print "Score: " + str(random_num) + "; Your grade is C"
        elif random_num >= 60:
            print "Score: " + str(random_num) + "; Your grade is D"
        else:
            print "Score: " + str(random_num) + "; Your grade is F"
    print "End of the program. Bye!"
scoresAndGrades()
