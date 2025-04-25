import pandas as pd
from fpdf import FPDF


df = pd.read_csv("topics.csv")

print(df.head())

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
counter = 0
for index, row in df.iterrows():
    print(row["Topic"])

    topic = row["Topic"]
    pages = int(row["Pages"])

    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{topic}", align="L",
             ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    pdf.ln(260)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    counter += 1
    pdf.cell(w=0, h=10, txt=f"Page Topic: {topic} - Page: {str(counter)}", align="R",
             ln=1)

    for page in range(pages - 1):
        pdf.add_page()
        pdf.ln(272)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        counter += 1
        pdf.cell(w=0, h=10, txt=f"Page Topic: {topic}, Page - {str(counter)}", align="R",
                 ln=1)

pdf.output("output.pdf")
