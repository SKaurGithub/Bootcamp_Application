"""
-------------- Welcome to TechDustry!--------------
This project was built with the goal of validating the input 
an user provides for a bootcamp application according 
the application's criteria.


"""


def separator(symbol="-", length=65):
    """
    This function creates a separator which helps with readability.
    """
    print(symbol * length)


def is_alpha(prompt):
    """
    This function will check if the input is alphabetic -
    if so, it will continue with the program otherwise
    the user will be prompt to enter a alphabetic value.
    :param prompt: different questions being asked to the user
    :return: return each input value
    """
    while True:
        input_value = input(prompt)
        input_value = input_value.replace(" ", "")
        if input_value.isalpha():
            return input_value
        else:
            while True:
                input_value = input(f"Invalid. Your entry should only "
                                    f"contain alphabetical characters. "
                                    + prompt)
                input_value = input_value.replace(" ", "")
                if input_value.isalpha():
                    return input_value


def language(choice):
    """
    This function will prompt user to ask,
    which programming language they would like to learn,
    providing the user with 4 options.
    :param choice: the choice of user
    :return: programming language choosen
    """
    while True:
        choice = input("Please select which programming language "
                       "you would like to enrol for (1-4):\n"
                       "1. Python\n"
                       "2. Java\n"
                       "3. JavaScript\n"
                       "4. SQL:\n")

        if choice == "1":
            return "Python"

        elif choice == "2":
            return "Java"

        elif choice == "3":
            return "JavaScript"

        elif choice == "4":
            return "SQL"

        else:
            print("Invalid entry.")


# Main code
# Collecting personal information from the user for a bootcamp application

print("\n\t\t\t\tWelcome to TechDustry!\n")
separator()
print("In order to enrol for the Software Engineer Bootcamp,\n"
      "please provide us with the requested information below.")
separator()

# Asking the user for information
first_name = is_alpha("Please enter your first name: ")

surname = is_alpha("Please enter your surname: ")

while True:
    try:
        age = input("Please enter your age: ")
        if age >= "0":
            age = int(age)
            break
        else:
            print("The age can not be a negative value.")
    except ValueError:
        print("Your age contains invalid characters.")


phone_number = input("Please enter your best contact number: ")
number = phone_number.replace(" ", "")
while True:
    if number.isnumeric() and len(phone_number) == 11 \
            and phone_number[0] == "0" and phone_number[1] == "7":
        break
    else:
        phone_number = input("Your contact number should only "
                             "contain numeric values and "
                             "should be 11 digit long (starting with 07).\n"
                             "Please re-enter your best contact number: ")
        number = phone_number.replace(" ", "")


email_address = input("Please enter your email address: ")
while True:
    if "@" in email_address and "." in email_address:
        break
    else:
        email_address = input("Your email address is invalid. "
                              "Please re-enter your email address: ")

location = is_alpha("Please enter your location (city): ")

work = input("Are you eligible to work in the UK? (yes/no): ")
while True:
    if work.lower() == "yes" or work.lower() == "no":
        break

    else:
        work = input("Please enter yes or no. "
                     "Are you eligible to work in the UK?: ")


programming_language = language("Please select which programming language "
                                "you would like to enrol for (1-4):\n"
                                "1. Python\n"
                                "2. Java\n"
                                "3. JavaScript\n"
                                "4. SQL:\n")


# Providing the user the option to review details provided and
# to make changes if needed.
separator()
separator()
print("Thank you for providing us with the above.\n"
      "Please review the information you have entered below.")

user = {"First name": first_name.title(),
        "Surname": surname.title(),
        "Age": age,
        "Contact number": phone_number,
        "Email address": email_address.lower(),
        "Location": location.title(),
        "Eligible to work": work.title(),
        "Programming language": programming_language.title(),
        }

while True:
    separator()
    # Display collected data in dict to the user
    for keys, values in user.items():
        print(keys, ":", values)

    separator()
    review = input("\nAre you happy with the above? (yes)\n"
                   "If you would like to make some changes, "
                   "please select (1-8):\n"
                   "1. First name\n"
                   "2. Surname\n"
                   "3. Age\n"
                   "4. Contact number\n"
                   "5. Email address\n"
                   "6. Location\n"
                   "7. Eligible to work\n"
                   "8. Programming language:\n")

    if review == "1":
        first_name = is_alpha("Please enter your first name: ")
        user["First name"] = first_name.title()

    elif review == "2":
        surname = is_alpha("Please enter your surname: ")
        user["Surname"] = surname.title()

    elif review == "3":
        while True:
            try:
                age = input("Please enter your age: ")
                if age >= "0":
                    age = int(age)
                    user["Age"] = age
                    break
                else:
                    print("The age can not be a negative value.")
            except ValueError:
                print("Your age contains invalid characters.")

    elif review == "4":
        phone_number = input("Please enter your best contact number: ")
        number = phone_number.replace(" ", "")
        while True:
            if number.isnumeric() and len(phone_number) == 11 \
                    and phone_number[0] == "0" and phone_number[1] == "7":
                user["Contact number"] = phone_number
                break
            else:
                phone_number = input("Your contact number should "
                                     "only contain numeric values "
                                     "and should be 11 digit long "
                                     "(starting with 07).\n"
                                     "Please re-enter your "
                                     "best contact number: ")
                number = phone_number.replace(" ", "")

    elif review == "5":
        email_address = input("Please enter your email address: ")
        while True:
            if "@" in email_address and "." in email_address:
                user["Email address"] = email_address.lower()
                break
            else:
                email_address = input("Your email address is invalid. "
                                      "Please re-enter your email address: ")

    elif review == "6":
        location = is_alpha("Please enter your location (city): ")
        user["Location"] = location.title()

    elif review == "7":
        work = input("Are you eligible to work in the UK? (yes/no): ")
        while True:
            if work.lower() == "yes" or work.lower() == "no":
                user["Eligible to work"] = work.title()
                break

            else:
                work = input("Please enter yes or no. "
                             "Are you eligible to work in the UK?: ")

    elif review == "8":
        programming_language = language(programming_language)

        user["Programming language"] = programming_language


    elif review.lower() == "yes":
        separator()
        separator()
        print("Thank you for your time.\n"
              "We will contact you shortly via email.")
        break

    else:
        print("Invalid entry.")