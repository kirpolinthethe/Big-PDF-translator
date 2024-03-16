# BPT - Big PDF Translator
BPT is designed for translation of pdf files with huge size that translation services cannot deal with.  

# Why?
Generally, if you try to translate pdf through deepl or google translate, the maximum size is limited to around 10MB.  
The GPT-4 may handle a larger pdf file, but the performance was not satisfactory according to personal experience.  
In addition, since translating text in pdf files daily is a very cumbersome task, there is a need for a program that automatically extracts and translates text.  

# Requirement
BPT uses Gemini from Google. So the users need to prepare their own Gemini API key. See the Python [Gemini API Guide document.](https://ai.google.dev/tutorials/python_quickstart) to get API key and specify the key as an environment variable.   
In order to use this program, the following packages should be installed:  
- pypdf
- tqdm
- google-generativeai

# How to Use
1. Clone this repository.
2. Put the pdf file you want to translate in the "pdfs" folder.
3. Save the initial prompt customized for the pdf file you want to translate to "initial.txt".
4. Put the text processing logic in process.py for the pdf you want to translate. If no text processing is needed, you can just use the code below.
```py
def process_text(text):
    return text
```
5. Run the run.py according to the format below.
```shell
python run.py [pdf name].pdf [output file name] [options]
```
6. The translated text will be generated in the "translate" folder.

# Options
- -s, --start : Page number to start translation. The default value is 1.
- -l, --last : The last page number you want to translate. The default value is the last page number in the pdf file.
- -m, --model : The Gemini modeld to use. Default model is Gemini 1.0 Pro.