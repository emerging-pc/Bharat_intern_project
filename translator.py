#Task-3
#Translator App
#It translates the English text to Spanish langauge.

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
