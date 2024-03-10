import pypdf

lists = "a\nbcd\ne"

Split = lists.split("\n")

print(Split)
print("".join(lists[0]))

reader = pypdf.PdfReader("./Titan-17.pdf")

page = reader.pages[23]

print(page.extract_text())
#print(page.extract_text().split("\n"))