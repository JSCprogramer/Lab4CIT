score= int(input('Enter your test score'))

if score >= 90:
    print('Grade is A')
else:
    if score >= 80:
        print('Grade is B')
    else:
        if score >= 70:
            print('Grade is C')
        else:
            if score >= 60:
                print('Grade is D')
            else:
                print('Grade is F')
