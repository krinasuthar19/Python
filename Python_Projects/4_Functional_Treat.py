
dataset = []
dataset_summary = {}  

def data_summary():
    """Displays basic statistics of the dataset using built-in functions."""
    global dataset_summary

    if not dataset:
        print("Dataset is empty! Please input data first.")
        return

    total_elements = len(dataset)
    total_sum = sum(dataset)
    minimum = min(dataset)
    maximum = max(dataset)
    average = total_sum / total_elements

    dataset_summary = {"Total Elements": total_elements, "Mean": average}

    print("\nData Summary:")
    print(f"Total elements: {total_elements}")
    print(f"Minimum value: {minimum}")
    print(f"Maximum value: {maximum}")
    print(f"Sum of all values: {total_sum}")
    print(f"Average value: {average:.2f}")


def factorial(n):
    """Recursive function to calculate factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def filter_data(threshold):
    """Filter values greater than or equal to threshold using lambda."""
    filtered = list(filter(lambda x: x >= threshold, dataset))
    print(f"Filtered Data (values >= {threshold}): {filtered}")

def dataset_statistics():
    """Returns min, max, sum, and average of dataset."""
    if not dataset:
        return None, None, None, None
    total = sum(dataset)
    avg = total / len(dataset)
    return min(dataset), max(dataset), total, avg

def sort_data(order="asc"):
    """Sort dataset ascending or descending."""
    if order == "asc":
        sorted_data = sorted(dataset)
        print("Sorted Data (Ascending):", sorted_data)
    else:
        sorted_data = sorted(dataset, reverse=True)
        print("Sorted Data (Descending):", sorted_data)


def input_data():
    """Input 1D dataset manually."""
    global dataset
    raw = input("Enter data for a 1D array (separated by spaces): ")
    dataset = [int(x) for x in raw.split()]
    print("Data has been stored successfully!")


def main():
    while True:
        print("\n=== Data Analyzer and Transformer Program ===")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == "1":
            input_data()

        elif choice == "2":
            data_summary()

        elif choice == "3":
            n = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {n} is: {factorial(n)}")

        elif choice == "4":
            if not dataset:
                print("Dataset is empty! Please input data first.")
            else:
                threshold = int(input("Enter a threshold value: "))
                filter_data(threshold)

        elif choice == "5":
            if not dataset:
                print("Dataset is empty! Please input data first.")
            else:
                print("Choose sorting option:\n1. Ascending\n2. Descending")
                opt = input("Enter your choice: ")
                if opt == "1":
                    sort_data("asc")
                else:
                    sort_data("desc")

        elif choice == "6":
            min_val, max_val, total, avg = dataset_statistics()
            if min_val is None:
                print("Dataset is empty! Please input data first.")
            else:
                print("\nDataset Statistics:")
                print(f"Minimum value: {min_val}")
                print(f"Maximum value: {max_val}")
                print(f"Sum of all values: {total}")
                print(f"Average value: {avg:.2f}")

        elif choice == "7":
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
