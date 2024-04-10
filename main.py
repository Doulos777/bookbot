def main():
    # Define the path to your file
    path_to_file = 'books/frankenstein.txt'
    
    # Open the file and read its contents
    with open(path_to_file, 'r') as file:
        file_contents = file.read()
        
        # Print the contents to the console
        print(file_contents)

        # Counting words
        print(len(file_contents.split()))

        # Counting Letters
    with open(path_to_file, 'r') as file:
        file_contents = file.read().lower()
        letter_count = {}
        for char in file_contents:
            if char.isalpha():
                letter_count[char] = letter_count.get(char, 0) +1

        print(letter_count)
        print(" ")

    # aggregate report
    file_name = str(path_to_file)
    print("--- Begin report of ",file_name," ---")
    print(len(file_contents.split()),"words found in the document")
    list_of_chars = []
    for char, count in letter_count.items():
        list_of_chars.append({"chars": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    list_of_chars.sort(reverse=True, key=sort_on)

    for k, v in list_of_chars:
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")



# Calling the main function
if __name__ == '__main__':
    main()
