import PyPDF2

with open('dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    with open('rotate.pdf','wb') as new_file:
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        writer.write(new_file)