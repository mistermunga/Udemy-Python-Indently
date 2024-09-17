from collections import Counter
import re
import os
import pypdf as pdf
from docx_text_extracter import get_docx_text

raw_path = "raw"  # Removed leading slash for compatibility
txt_path = "plain-txt"  # Removed leading slash for compatibility


def get_raw_string(file_path):
    """Extracts text from a PDF or DOCX file and saves it as a plain text file."""
    text = ""

    # Process PDF files
    if file_path.endswith(".pdf"):
        reader = pdf.PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()

        # Save the extracted text as .txt
        filename = os.path.splitext(os.path.basename(file_path))[0]  # Get file name without extension
        output_path = os.path.join(txt_path, f"{filename}.txt")
        with open(output_path, "w") as text_file:
            text_file.write(text)

    # Process DOCX files
    elif file_path.endswith(".docx"):
        text = get_docx_text(file_path)

        filename = os.path.splitext(os.path.basename(file_path))[0]  # Get file name without extension
        output_path = os.path.join(txt_path, f"{filename}.txt")
        with open(output_path, "w") as text_file:
            text_file.write(text)

    return text


def get_frequencies(text: str):
    """Returns word frequencies in the given text."""
    words = re.findall(r"\b\w+\b", text.lower())  # Convert text to lowercase and find words
    word_counts = Counter(words)

    return word_counts.most_common()


def main():
    """Main function to handle user input and display word frequencies."""
    files = os.listdir(raw_path)  # Get a list of files in the raw directory
    index_dict = {i: files[i - 1] for i in range(1, len(files) + 1)}  # Create an index for file selection

    print("Choose a number from the list below:")
    for index, filename in index_dict.items():
        print(f"{index}: {filename}")

    while True:
        try:
            input_number = int(input("Enter your choice: "))  # Ask for user input
            if input_number not in index_dict:
                print("Invalid input: exiting.")
                return

            file_path = os.path.join(raw_path, index_dict[input_number])
            raw_text = get_raw_string(file_path)  # Extract the raw text from the selected file
            frequencies = get_frequencies(raw_text)  # Get word frequencies

            for word, count in frequencies:
                print(f"{word}: {count}")  # Print word frequency

        except ValueError:
            print("Invalid input: please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return


if __name__ == "__main__":
    main()
