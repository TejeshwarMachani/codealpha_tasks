from googletrans import Translator

def translate_text(text, src_language='auto', dest_language='en'):
    translator = Translator()
    translated = translator.translate(text, src=src_language, dest=dest_language)
    return translated.text

# Example usage
if __name__ == "__main__":
    text_to_translate = input("Enter the text to translate: ")
    source_lang = input("Enter the source language (e.g., 'en' for English, 'es' for Spanish) or 'auto' for automatic detection: ")
    target_lang = input("Enter the target language (e.g., 'en' for English, 'es' for Spanish): ")

    translated_text = translate_text(text_to_translate, src_language=source_lang, dest_language=target_lang)
    print(f"Translated text: {translated_text}")
