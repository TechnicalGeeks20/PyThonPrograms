# Python program to create
# a pdf file


from fpdf import FPDF


# save FPDF() class into a
# variable pdf
pdf = FPDF()

file = open("demo.txt",'r')
print(file)
# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# create a cell
pdf.cell(200, 10, txt = "Techinical Geeks",
		ln = 1, align = 'C')

# add another cell
for line in file.readlines():
    pdf.cell(200, 10, txt = line,
		ln = 2, align = 'C')


# save the pdf with name .pdf
pdf.output("demo.pdf")
print("Successfully converted   ")
