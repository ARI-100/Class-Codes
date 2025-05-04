import random

def generate_username(full_name):
    name_parts = full_name.split()
    if len(name_parts) < 2:
        return "Please enter a valid full name (e.g., John Doe)"
    
    first_name = name_parts[0].lower()
    last_name = name_parts[-1].lower()
    
    # More random number ranges
    short_num = random.randint(10, 99)
    med_num = random.randint(100, 999)
    long_num = random.randint(1000, 9999)
    
    username1 = first_name + last_name
    username2 = first_name[:3] + last_name[-3:] + str(short_num)
    username3 = first_name[:3] + last_name[-2:] + str(med_num)
    username4 = first_name + str(short_num)
    username5 = last_name + str(med_num)
    username6 = first_name[1:3] + last_name[::-1] + str(short_num)  # Using full reversed lastname
    username7 = first_name[-2:] + last_name[:2] + str(long_num)     # Mix of end and start
    username8 = first_name[0] + last_name[-1] + str(med_num)        # First and last letters
    username9 = first_name[-1] + last_name[0] + str(long_num)       # Last and first letters
    username10 = first_name[::2] + last_name[::2] + str(short_num)  # Every other letter

    usernames = [username1, username2, username3, username4, username5, username6, username7, username8, username9, username10]
    choice = random.randint(0, 9)
    return f"{usernames[choice]} (Option {choice + 1})"

while True:
    full_name = input("Enter your full name or type exit to quit: ")
    if full_name.lower() == "exit":
        print("Exiting the program...")
        break
    username = generate_username(full_name)
    print(f"Generated username: {username}")
    print("-" * 40)