
choice = "_"

while True:
    if choice == "0":
        print("Now you are Exit")
        break
    elif choice in "123456":
        print("your choice is {}".format(choice))
    else:
        (print("Please choose your option one of them.\n"
               "1 Akash\n"
               "2 Priya\n"
               "3 Suraj\n"
               "4 Pawn\n"
               "5 Ravi\n"
               "6 Shikhar\n"
               "0 EXit"))
        choice = input()

