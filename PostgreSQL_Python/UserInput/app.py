from database import add_entry, get_entry


menu = """Please select one of the following options: 
1) Add new entry for today.
2) View Entries.
3) Exit.

Your Selection: """

welcome = "Welcome to the programming diary."

print(welcome)

# user_input = input(menu)
while (user_input := input(menu)) != "3":
    if user_input == "1":
        entry_content = input("What have you learned today?")
        entry_date = input("Enter the date:")

        add_entry(entry_content,entry_date)

    elif user_input == "2":
        enteries = get_entry()

        for entry in enteries:
            print(f"{entry['date']}\n{entry['content']}\n\n")
            
    else:
        print('Invalid Input.')



