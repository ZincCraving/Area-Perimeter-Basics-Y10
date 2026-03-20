# Ask user for width amd loop until they
# enter a number that is more than zero
from enum import EnumCheck


def num_check(question):

    error = "Please enter a number that is more than 0 zero\n"
    while True:

        try:
            # ask the user for a number

            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine starts here
keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Cost: ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = perimeter * cost

    # Display output
    print()
    print(f"perimeter: {perimeter} m")
    print(f"Price: ${price: .2f}")

    # Ask the user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit")
    print()

print("Thank you for using the calculator")