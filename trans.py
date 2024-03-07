import pypdf
from googletrans import Translator

def remove_prefix_suffix(text):
    # Split text into lines
    lines = text.split("\n")
    
    # Remove the first and last lines
    removed = "\n".join(lines[1:-2])
    
    return removed

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def extract_text_from_pdf(pdf_path, target_language):
    result = ""
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            pure_text = remove_prefix_suffix(text)
            result += translate_text(pure_text, target_language)
    return result

def main(pdf_path, target_language, output_file):
    translated_text = ""

    # Step 0: Extranct the entire text from PDF
    reader = pypdf.PdfReader(pdf_path)
    
    for page in reader.pages:
        text = page.extract_text()
        remove_text = remove_prefix_suffix(text)
        translated_text += translate_text(remove_text, target_language)
    
    # Step 4: Save result to file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

if __name__ == "__main__":
    # Provide the path to the PDF file
    pdf_path = "./Titan-17.pdf"
    
    # Set the target language (default is Korean 'ko')
    target_language = 'ko'
    
    # Set the output file name (default is 'translated_output.txt')
    output_file = 'translated_output.txt'
    
    # Execute main function
    main(pdf_path, target_language, output_file)
