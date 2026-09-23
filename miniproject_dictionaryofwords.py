#Dictionary of words
"""Create a program that manages a dictionary of word meanings. The program
should allow users to perform the following actions:
1. Add a Word: Allow users to add new words along with their meanings to the
dictionary.
2. Search for Meaning: Enable users to search for the meaning of a word in the
dictionary.
3. Display All Words: Provide an option to display all words and their meanings
currently stored in the dictionary.
4. Update Meaning: Implement a feature to update the meaning of an existing
word in the dictionary. After updating, display the updated meaning.
5. Delete Word: Implement a feature to delete a word and its meaning from the
dictionary. Confirm the deletion and handle cases where the word doesn't exist.

Ensure the program handles invalid inputs gracefully. Use a while loop to keep the
program running until the user chooses to exit"""

dictionary = {}

while True:
    print("\nDictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        word = input("Enter the word: ").lower()
        meaning = input("Enter the meaning: ")
        dictionary[word] = meaning
        print("Word added successfully!")

    elif choice == 2:
        word = input("Enter the word to search: ").lower()
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found in the dictionary.")

    elif choice == 3:
        if dictionary:
            print("Words and their meanings:")
            for word, meaning in dictionary.items():
                print(f"{word}: {meaning}")
        else:
            print("Dictionary is empty.")
 
    elif choice == 4:
        word = input("Enter the word to update meaning: ").lower()
        if word in dictionary:
            new_meaning = input("Enter the new meaning: ")
            dictionary[word] = new_meaning
            print("Meaning updated successfully!")
            print("Updated Meaning:", dictionary[word])
        else:
            print("Word not found in the dictionary.")

    elif choice == 5:
        word = input("Enter the word to delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print("Word deleted successfully!")
        else:
            print("Word not found in the dictionary.")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("invalid choice. Enter a valid choice: ") 