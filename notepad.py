def save_text_to_file(text, filename="output.txt"):
    """
    Saves the given text to a file with the specified filename.
    
    Args:
    - text (str): The text to be saved.
    - filename (str): The name of the file where the text will be saved.
    """
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Text has been saved to {filename}")

def main():
    print("Enter your text (press Enter to finish):")
    user_text = input()
    save_text_to_file(user_text)

if __name__ == "__main__":
    main()

