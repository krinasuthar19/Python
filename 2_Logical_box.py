print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Invalid number of rows. Please enter a positive integer.")
        print("Pattern:")

        for i in range(1, rows + 2):
            print("*" * i)
    
    elif choice == "2":
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            if start > end:
                print("Invalid range. Start should be less than or equal to end.")
        
        total_sum = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total_sum += num
        
        print(f"Sum of all numbers from {start} to {end} is: {total_sum}")
    
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

