age = int(input('please enter your age'))
if age in range(18, 65):
    print("Welcome in travel")
else:
    print("Sorry you are not eligible to travel")

print("_" * 80)
if age > 18 or age < 65:
    print('Welcome in travel')
else:
    print("Sorry you are not eligible to travel")
