import os
from genai_utils import configure_genai, generate_descriptions
from excel_utils import save_to_excel, adjust_excel_formatting
from colorama import init, Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as PTStyle

def colored_prompt(message, color):
    custom_style = PTStyle.from_dict({
        'prompt': color
    })
    return prompt([('class:prompt', message)], style=custom_style)

def main():
    init(autoreset=True)

    print(Fore.CYAN + "Welcome to the PDF to AI Description Generator!")

    api_key = colored_prompt("Please enter your GEMINI API key and press Enter: ", 'fg:yellow')
    model_name = colored_prompt("Please enter the model name and press Enter (default: 'gemini-1.5-flash'): ", 'fg:yellow') or "gemini-1.5-flash"
    max_requests = colored_prompt("Please enter the maximum number of requests and press Enter (default: 3): ", 'fg:yellow') or "3"

    try:
        max_requests = int(max_requests)
    except ValueError:
        print(Fore.RED + "Invalid input for maximum number of requests. Please enter a valid integer.")
        return

    print(colored_prompt("Please enter your system instruction (type 'END' on a new line to finish):", 'fg:yellow'))
    system_instruction = []
    while True:
        line = colored_prompt("", 'fg:green')
        if line == 'END':
            break
        system_instruction.append(line)
    system_instruction = "\n".join(system_instruction)

    pdf_directory = 'downloads'
    ai_descriptions_file = 'ai_descriptions.xlsx'

    try:
        os.environ['GEMINI_API_KEY'] = api_key
        model = configure_genai(api_key, system_instruction, model_name)
        descriptions = generate_descriptions(model, pdf_directory, max_requests)
        save_to_excel(descriptions, ai_descriptions_file)
        adjust_excel_formatting(ai_descriptions_file)
        print(Fore.GREEN + f"All AI descriptions have been saved to {ai_descriptions_file}")
    except Exception as e:
        print(Fore.RED + f"Error in main: {e}")

if __name__ == "__main__":
    main()
