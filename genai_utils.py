import google.generativeai as genai
from google.generativeai import GenerationConfig

def configure_genai(api_key, system_instruction, model_name):
    try:
        genai.configure(api_key=api_key)
        generation_config = GenerationConfig(
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,
            response_mime_type='text/plain',
        )
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
            system_instruction=system_instruction,
        )
        return model
    except Exception as e:
        print(f"Error configuring GenAI: {e}")
        raise

def generate_descriptions(model, pdf_directory, max_requests):
    from pdf_utils import extract_text_from_pdf
    import os
    import time

    descriptions = []
    request_count = 0

    try:
        for i, filename in enumerate(os.listdir(pdf_directory)):
            if filename.endswith('.pdf'):
                if request_count >= max_requests:
                    print('Maximum number of requests reached.')
                    break

                pdf_path = os.path.join(pdf_directory, filename)
                content = extract_text_from_pdf(pdf_path)

                if content:
                    chat_session = model.start_chat(history=[])
                    response = chat_session.send_message(content)

                    description = response.text

                    descriptions.append({
                        'Filename': filename,
                        'Description': description
                    })

                    print(f'[{i}] Generated AI description for {filename}')
                    request_count += 1

                    if (i + 1) % 5 == 0:
                        time.sleep(60)
    except Exception as e:
        print(f"Error generating descriptions: {e}")
        raise

    return descriptions