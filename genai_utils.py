import google.generativeai as genai
from google.generativeai import GenerationConfig

# Function to configure the GenAI model
def configure_genai(api_key, system_instruction, model_name):
    try:
        # Configure the GenAI API with the provided API key
        genai.configure(api_key=api_key)

        # Set up the generation configuration
        generation_config = GenerationConfig(
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,
            response_mime_type='text/plain',
        )

        # Initialize the GenerativeModel with the provided parameters
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
            system_instruction=system_instruction,
        )
        return model
    except Exception as e:
        # Print an error message if configuration fails
        print(f"Error configuring GenAI: {e}")
        raise

# Function to generate descriptions for PDFs in a directory
def generate_descriptions(model, pdf_directory, max_requests):
    from pdf_utils import extract_text_from_pdf
    import os
    import time

    descriptions = []
    request_count = 0

    try:
        # Iterate through each file in the specified directory
        for i, filename in enumerate(os.listdir(pdf_directory)):
            if filename.endswith('.pdf'):
                if request_count >= max_requests:
                    print('Maximum number of requests reached.')
                    break

                pdf_path = os.path.join(pdf_directory, filename)
                content = extract_text_from_pdf(pdf_path)

                if content:
                    # Start a new chat session with the model
                    chat_session = model.start_chat(history=[])
                    # Send the extracted text to the model and get the response
                    response = chat_session.send_message(content)

                    description = response.text

                    # Append the filename and description to the list
                    descriptions.append({
                        'Filename': filename,
                        'Description': description
                    })

                    print(f'[{i}] Generated AI description for {filename}')
                    request_count += 1

                    # Pause after every 5 requests to avoid rate limiting
                    if (i + 1) % 5 == 0:
                        time.sleep(60)
    except Exception as e:
        # Print an error message if description generation fails
        print(f"Error generating descriptions: {e}")
        raise

    return descriptions