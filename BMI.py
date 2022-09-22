sex = input("請輸入性別（男／女）")
heigh = eval(input("請輸入身高（cm）"))
weigh = eval(input("請輸入體重（kg）"))

bmi = weigh/(heigh/100)**2

if sex=='男':
    if bmi > 25:
        print("體重過重")
    elif bmi < 20:
        print("體重過輕")
    else:
        print("體重適中")
else:
    if bmi > 22:
        print("體重過重")
    elif bmi < 18:
        print("體重過輕")
    else:
        print("體重適中")