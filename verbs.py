def add_verb():
    verbs = open("korean_verbs.txt","a")
    english = input("Enter the verb in english")+ ";"
    korean1 = input("Enter the verb in korean (not conjugate)")+";"
    korean2 = input("Enter the verb in korean (conjugate)")

    verbs.write("\n"+english + korean1+korean2)

    verbs.close()