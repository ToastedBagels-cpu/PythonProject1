def main():
    name = input("What is your name:")
    numbersbetween = int(input("List a number between 1 and 10:"))
    projectstring = f"Welcome to Comp151 {name}\n" * numbersbetween
    print(projectstring)
main()