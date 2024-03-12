import pypdf
import os
import sys
import time
import argparse

import google.generativeai as genai

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process PDF and translate text.")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("-p", "--param", type=int, help="Optional parameter")
    return parser.parse_args()

def main():
    args = parse_arguments()

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    FILE_PATH = "./pdfs/" + args.pdf_file + ".pdf"
    RESULT_PATH = "./translate/" + args.output_file + ".txt"
    i = (args.param - 1) if args.param is not None and args.param > 0 else 0

    InitialPrompt = """
            You are a translator for the manual of Avolites Titan consoles. The destination language is Korean.
            When I gave you some texts, you translate it.
            The texts that I give you may be unproperly line-broken and spaced.
            If so, you figure out the context of the texts and properly break the line and put spaces.
            Then Translate it to Korean. You ready?
        """

    genai.configure(api_key=GOOGLE_API_KEY)

    reader = pypdf.PdfReader(FILE_PATH)

    model = genai.GenerativeModel('gemini-1.0-pro')

    InitialResponse = model.generate_content(InitialPrompt)

    print(f"Start: {InitialResponse.text}")

    page_max = len(reader.pages)

    with open(RESULT_PATH, "w+", encoding="utf-8") as f:
        while True:
            if i == page_max:
                print("[*] Translation Done.")
                break
            
            contents = reader.pages[i].extract_text().split('\n')
            reformatted = "\n".join(contents[1:-2])

            try:
                translated = model.generate_content("Translate this to Korean:\n" + reformatted)
                print(f"[*] translated Page {i+1} Successfully")
                f.write(translated.text)
                i += 1
            except IOError as F:
                print("[!] File I/O error occured:" + F)
                sys.exit(1)
            except:
                print("[!] AI call error occured. Wait a moment...")
                time.sleep(10)
            
if __name__ == "__main__":
    main()