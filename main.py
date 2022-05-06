from KarnaughMapper import KarnaughMapper

#Main program
if __name__ == "__main__":
    userInput = 'y'
    while userInput == 'y':
        print("\tKarnaugh Mapper and Solver for 2 variables")
        for _ in range(50):
            print("-", end='')
        print()

        print("A B lineNumber")
        print("0 0     0")
        print("0 1     1")
        print("1 0     2")
        print("1 1     3")
        print("Enter the lineNumber with the truth value:")

        tValue = list(map(int, input().split()))
        KarnaughMapper.construct_and_display_k_map(tValue, 1)

        userInput = input("Enter 'y' for another K-Map or anything else to exit : ").lower()

        for i in range(25):
            print("--", end='')
        print()

    print("\n\tProgram ended")