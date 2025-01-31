# Description Generator with Gemini API

This is a simple description generator using the Gemini API. 
It uses the Gemini API to get the data and then generates a description based on the data. Which will be exported to an excel file.

## Pre-requisites

- [Python](https://www.python.org/downloads/) 3.x
- [Pip](https://pypi.org/project/pip/) (Python package manager)
- Gemini API key, which you could get it from [Gemini API](https://ai.google.dev/gemini-api/docs)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/KurodaKJ/pdf-to-ai-description-generator.git
   cd pdf-to-ai-description-generator
   ```
   
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   
3. Install the required packages
   ```sh
   pip install -r requirements.txt
   ```
   
## Usage

1. Put your PDF files in the `downloads` folder.

2. Run the script:
   ```sh
   python main.py
   ```

## Contributing

Contributions are welcome! Please open an [issue](https://github.com/KurodaKJ/pdf-to-ai-description-generator/issues) or submit a [pull request](https://github.com/KurodaKJ/pdf-to-ai-description-generator/pulls).
   
