# Bharat_intern_project

# Install googletrans in command prompt by: pip install googletrans

# Create python file for the project

# Write code as:

#PROJECT 01

from googletrans import Translator

def translate_text(text, target_language='es'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    source_text = input("Enter the text to translate (in English): ")
    translated_text = translate_text(source_text)
    print(f"Translated text (in Spanish): {translated_text}")

if __name__ == "__main__":
    main()
