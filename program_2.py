#Brason Orrey - Age Classifier Program

age = float(input("Please Enter a Person's Age: "))

if age <= 1:
    print("This person is an infant.")
elif age > 1 and age < 13:
    print("This person is a child.")
elif age >= 13 and age < 20:
    print("This person is a teenager.")
else:
    print("This person is an adult.")
