#Reading pdf file 
import PyPDF2 
file = open('20. PROPERTY.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(file)
print (pdf_reader.numPages)
#Getting the page from a pdf file 
page1 = pdf_reader.getPage(0)
print (page1)
#Read the pages 
page1_read = page1.extractText()
print (page1_read)
file.close()
#Write to a file 
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page1)
pdf_output = open('test.pdf','wb')
pdf_writer.write(pdf_output)
file.close()
pdf_output.close()