import pypdf
import os
import sys
import time
import argparse
import tqdm
from process import process_text

import google.generativeai as genai

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process PDF and translate text.")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("-s", "--start", type=int, help="Starting page number")
    parser.add_argument("-l", "--last", type=int, help="Last page number")
    parser.add_argument("-m", "--model", help="Gemini model to use")
    return parser.parse_args()

def main():
    args = parse_arguments()

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    INITIAL_FILE = open("initial.txt", "r")
    FILE_PATH = "./pdfs/" + args.pdf_file
    RESULT_PATH = "./translate/" + args.output_file
    MODEL_NAME = 'gemini-1.0-pro' if args.model is None else args.model
    
    reader = pypdf.PdfReader(FILE_PATH)

    i = (args.start - 1) if args.start is not None and args.start > 0 else 0

    if args.last is not None and args.last > 0 and args.last <= len(reader.pages):
        page_last = args.last
    else:
        page_last = len(reader.pages)

    InitialPrompt = INITIAL_FILE.read()

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)

    InitialResponse = model.generate_content(InitialPrompt)

    print(f"[*] Translation started with : {InitialPrompt}")

    pbar = tqdm.tqdm(range(page_last - i), ncols=50, leave=False)
    with open(RESULT_PATH, "w+", encoding="utf-8") as f:
        while True:
            if i >= page_last:
                print("\n[*] Translation Done.")
                pbar.close()
                break
            
            processed = process_text(reader.pages[i].extract_text())

            try:
                translated = model.generate_content("Translate this to Korean:\n" + processed)
                # print(f"[*] translated Page {i+1} Successfully")
                f.write(translated.text + "\n")
                i += 1
                pbar.update()
            except IOError as F:
                print(f"[!] File I/O error occured: {F}")
                sys.exit(1)
            except Exception as e:
                print(f"[!] Error occurred: {e}")
                if "500 An internal error" in str(e):
                    time.sleep(10)
                else:
                    stop = input("[?] Unexpected error occurred. Would you like to continue? (y/n) :")
                    if "y" not in stop:
                        sys.exit(1)
            
if __name__ == "__main__":
    main()