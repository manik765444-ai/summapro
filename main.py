# main.py

import sys
from textwrap import shorten

def summarize_text(input_text, max_length=100):
    """
    Summarizes the given text to the specified maximum length.

    Args:
        input_text (str): The text to summarize.
        max_length (int): The maximum length of the summary in characters. Default is 100.

    Returns:
        str: The summarized text.

    Raises:
        ValueError: If the input_text is empty or max_length is not positive.
    """
    if not input_text or not isinstance(input_text, str):
        raise ValueError("Input text must be a non-empty string.")
    if max_length <= 0:
        raise ValueError("Maximum length must be a positive integer.")

    # Use textwrap's shorten method to create the summary
    return shorten(input_text, width=max_length, placeholder="...")

def main():
    """
    Main function to handle user input and summarize the text.
    """
    try:
        # Prompt user for input
        input_text = input("Enter the text to summarize: ").strip()
        max_length = input("Enter the maximum summary length (default is 100): ").strip()

        # Default maximum length is 100 if user provides no input
        max_length = int(max_length) if max_length else 100

        # Generate and display summary
        summary = summarize_text(input_text, max_length)
        print("\nSummary:")
        print(summary)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Safeguard against script hanging
        print("\nProgram terminated.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        sys.exit(1)