import os
import argparse
from colorama import init, Fore
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as PTStyle

from excel_utils import save_to_excel, adjust_excel_formatting
from genai_utils import configure_genai, generate_descriptions


# Function to create a colored prompt (no longer used for input)
def colored_prompt(message, color):
    custom_style = PTStyle.from_dict({
        'prompt': color
    })
    return prompt([('class:prompt', message)], style=custom_style)

def main():
    # Initialize colorama for colored output
    init(autoreset=True)

    print(Fore.CYAN + "Welcome to the PDF to AI Description Generator!")

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate AI descriptions from PDFs.")
    parser.add_argument("-system_instruction", type=str, required=True, help="System instruction for the AI")
    parser.add_argument("-apiKey", type=str, required=True, help="GEMINI API key")
    parser.add_argument("-model", type=str, default="gemini-1.5-flash", help="Model name (default: gemini-1.5-flash)")
    parser.add_argument("-max_requests", type=int, default=3, help="Maximum number of requests (default: 3)")

    args = parser.parse_args()

    # Retrieve values from arguments
    api_key = args.apiKey
    model_name = args.model
    max_requests = args.max_requests
    system_instruction = args.system_instruction


    # Define directories and output file
    pdf_directory = 'downloads'
    ai_descriptions_file = 'ai_descriptions.xlsx'

    try:
        # Set GEMINI API key environment variable
        os.environ['GEMINI_API_KEY'] = api_key

        # Configure the model with the provided parameters
        model = configure_genai(api_key, system_instruction, model_name)

        # Generate descriptions for PDFs in the specified directory
        descriptions = generate_descriptions(model, pdf_directory, max_requests)

        # Save the generated descriptions to an Excel file
        save_to_excel(descriptions, ai_descriptions_file)

        # Adjust the formatting of the Excel file
        adjust_excel_formatting(ai_descriptions_file)

        print(Fore.GREEN + f"All AI descriptions have been saved to {ai_descriptions_file}")
    except Exception as e:
        print(Fore.RED + f"Error in main: {e}")

if __name__ == "__main__":
    main()