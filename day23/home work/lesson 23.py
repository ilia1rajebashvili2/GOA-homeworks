
def get_user_info():
    print("Please provide the following information:")

    # 1. First Name
    first_name = input("1. First Name: ")

    # 2. Last Name
    last_name = input("2. Last Name: ")

    # 3. Age
    age = input("3. Age: ")

    # 4. Email Address
    email = input("4. Email Address: ")

    # 5. Phone Number
    phone_number = input("5. Phone Number: ")

    # 6. Favorite Color
    favorite_color = input("6. Favorite Color: ")

    # 7. Hobbies
    hobbies = input("7. Hobbies (comma separated): ")

    # 8. Country of Residence
    country = input("8. Country of Residence: ")

    # 9. Occupation
    occupation = input("9. Occupation: ")

    # 10. Preferred Programming Language
    preferred_language = input("10. Preferred Programming Language: ")

    # Display collected information
    print("\nThank you for providing the information. Here is what you entered:")
    print(f"1. First Name: {first_name}")
    print(f"2. Last Name: {last_name}")
    print(f"3. Age: {age}")
    print(f"4. Email Address: {email}")
    print(f"5. Phone Number: {phone_number}")
    print(f"6. Favorite Color: {favorite_color}")
    print(f"7. Hobbies: {hobbies}")
    print(f"8. Country of Residence: {country}")
    print(f"9. Occupation: {occupation}")
    print(f"10. Preferred Programming Language: {preferred_language}")
