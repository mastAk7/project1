print("WELCOME TO THE MASTERAK CAFE APP")
print()
print()
x=input("Please press enter to proceed.")
print()
print("Enter 1 for consumer")
print("Enter 2 for admin")
c=int(input("Enter Choice: "))
if c==1:
    with open("consumer.py","r") as f:
        code=f.read()
        exec(code)
    f.close()
