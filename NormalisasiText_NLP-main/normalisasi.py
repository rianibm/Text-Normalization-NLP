import os

# for filename in os.listdir("tesfile"):
#    with open(os.path.join("tesfile", filename), 'r') as f:
#        text = f.read()
#        print(text)
import PyPDF2

#ambil path setiap file pdf
listPathFile = []
for filename in os.listdir("tesfile"):
   listPathFile.append('tesfile/'+filename)

#simpan judul doc dan isinya
dictDoc = {}

for file_path in listPathFile:
    with open(file_path, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        a = file_path[8::]
        isikonten = ""
        for page in reader.pages:
            text = page.extractText()
            striptext = text.strip()
            delNewLine = striptext.replace('\n','')
            textLower = delNewLine.lower()
            isikonten +=textLower
        dictDoc[a] = isikonten

print(dictDoc["coba.pdf"])

            