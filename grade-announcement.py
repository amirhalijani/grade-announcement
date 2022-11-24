score = input("Enter Score: ")
point = float(score)

if point >= 0.0 and point <= 1.0:
    if point >= 0.9:
        print("A")
    elif point >= 0.8:
        print("B")
    elif point >= 0.7:
        print("C")
    elif point >= 0.6:
        print("D")
    elif point < 0.6:
        print("F")
