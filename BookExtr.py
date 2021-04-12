import PyPDF2


PDFfile = r'C:\Users\lucas\Documents\Python\NLP\On_the_Road.pdf'
text_file = r"C:\Users\lucas\Documents\Python\NLP\ontheroad.txt"

#Função para extrair texto de PDF
def TextExtract(start, pdfFile):
   pdfFileObject = open(pdfFile, 'rb')
   pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
   numberOfPages = pdfReader.numPages

   with open(text_file,"w") as tempFile:
       for p in range(start, numberOfPages):
          pagesObject = pdfReader.getPage(p)
          text = pagesObject.extractText()
          #Correções específicas deste PDF. Dois caracteres unicodes com espaço.
          text = text.replace('\ufb01', "fi")
          text = text.replace("fi ", "fi")
          text = text.replace('\ufb02', "fl")
          text = text.replace("fl ", "fl")
          tempFile.write(text)
   tempFile.close()

TextExtract(117, PDFfile)

#open and read the file after the appending to check if ok:
#f = open(text_file, "r")
#print(f.read())
