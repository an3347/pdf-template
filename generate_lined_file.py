from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

for k in range(2):
    pdf.add_page()
    i = 16
    while i <= 275:
        pdf.line(0, i, 216, i)
        i += 8
    i -= 10

    pdf.line(27, 0, 27, 280)

pdf.output("text_file_2.pdf")
