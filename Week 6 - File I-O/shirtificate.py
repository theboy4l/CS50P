from fpdf import FPDF


def main():
    name = input("Name: ")
    shirtify(name)


def shirtify(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=24)
    pdf.cell(0, 10, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", 55, 20, 100)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 60)
    pdf.cell(0, 10, name, align="C")
    return pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
