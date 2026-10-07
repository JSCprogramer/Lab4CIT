score1 = float(input("Enter the score for test 1:"))
score2 = float(input("Enter the score for test 2:"))
score3 = float(input("Enter the score for test 3:"))

scoreavg= (score1+score2+score3)/3

print(f'The average score is {scoreavg}')

if scoreavg > 95:
    print('Amzaing score Comgratulations!')
