score = 0
start = input('Are you ready to play(yes/no): ')
if start.lower() == 'yes':
    print('   ______ ')
    print('  /      |')
    print(' /       |')
    print('/________|')
    print('Welcome to the Cricket Quiz!')
    one = input("1.Who is the vice captain of India in 20/21 ODI: ")
    if one.lower() == 'k.l.rahul':
        print("correct!")
        score += 1
    else:
        print('Incorrect!')
        print("The correct answer is K.L.Rahul")
    two = input("2.How many balls are bowled in an over: ")
    if two.lower() == '6':
        print("Correct!")
        score += 1
    if two.lower() == 'six':
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is 6")
    three = input("3.Which Country first started 'Cricket': ")
    if three.lower() == 'england':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is England")
    four = input("4.What is the Nick Name of Mahendra Singh Dhoni: ")
    if four.lower() == 'captain cool':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Captain Cool")
    five = input("5.Who is named as the nickname 'Haryana Hurricane': ")
    if five.lower() == 'kapil dev':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Kapil Dev")
    six = input("6.Shane warne is the coach of which team in IPL: ")
    if six.lower() == 'rr':
        print("Correct!")
        score += 1
    if six.lower()=='rajastan royals':
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is RR or Rajastan Royals")
    seven = input("7.Does R.C.B  win the IPL trophy since 2020: ")
    if seven.lower() == 'no':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is No")
    eight = input("8.How many times does Rohit Sharma Captained and won the IPL trophy since 2020: ")
    if eight.lower() == '4':
        print("Correct!")
        score += 1
    if eight.lower() == 'four':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is four")
    nine = input("9.Who is the Chairman of IPL now: ")
    if nine.lower() == 'sourav ganguly':
        print("Correct!")
        score += 1
    if nine.lower()=='dada':
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Sourav Ganguly")
    ten = input("Who has been awarded the 'SPIRIT OF CRICKET OF THE DECADE' award in the year 2021: ")
    if ten.lower() == 'm.s.dhoni':
        print("Correct!")
        score += 1
    if ten.lower()=='dhoni':
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is M.S.Dhoni")
    print('')
    print('Your score is '+str(score)+' out of 10')
    print('')
    print("See you later in another Quiz")
    print('')
    print('Update will be soon!!')
if start.lower() == 'no':
    print('')
    print('Get ready for the Quiz soon!,See you later in another Quiz!')
print('     "SYSTEM CLOSED"')
