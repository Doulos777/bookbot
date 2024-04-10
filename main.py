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
        print(len(file_contents.split()))

        # git commit -m "saving changes"


# Calling the main function
if __name__ == '__main__':
    main()
