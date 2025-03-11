def num():
    num = int(input("classify number: "))
    if num > 0:
        if num %2 == 0:
            print("Positive Even Number")
        else:
            print("Positive Odd Number")
    elif num == 0:
        print("Neutral number")
    else:
        if num %2 == 0:
            print("Negative Even Number")
        else:
            print("Negative Odd Number")

while True:
    num()