import pypdf
from googletrans import Translator

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        for page_num in range(reader.numPages):
            page = reader.Page[page_num]
            text += page.extract_text()
    return text

def remove_prefix_suffix(text):
    # Assuming prefix and suffix are known patterns, you can replace them with empty string
    # Adjust this function according to your specific needs
    prefix = "Prefix_to_remove"
    suffix = "Suffix_to_remove"
    return text.replace(prefix, "").replace(suffix, "")

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main(pdf_path, target_language='ko', output_file='translated_output.txt'):
    # Step 1: Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Remove prefix and suffix
    processed_text = remove_prefix_suffix(extracted_text)
    
    # Step 3: Translate text
    translated_text = translate_text(processed_text, target_language)
    
    # Step 4: Save result to file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

if __name__ == "__main__":
    # Provide the path to the PDF file
    pdf_path = "path/to/your/pdf/file.pdf"
    
    # Set the target language (default is Korean 'ko')
    target_language = 'ko'
    
    # Set the output file name (default is 'translated_output.txt')
    output_file = 'translated_output.txt'
    
    # Execute main function
    main(pdf_path, target_language, output_file)
