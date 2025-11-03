#task 1
#"report.pdf"
#using Python dictionary to store my business data and then generate a PDF report using the reportlab library
# britafri_report.py
# ------------------
# Task: Use a dictionary to generate a PDF report

# 1️⃣ Import tools from the reportlab box
from reportlab.lib.pagesizes import A4     # brings in paper size
from reportlab.pdfgen import canvas        # gives us the pen + paper
import os                                  # helps us open the PDF automatically

# 2️⃣ Create a dictionary with your report data
sales_report = {
    "Business Name": "BritAfri",
    "Month": "October 2025",
    "Total Sales (KSh)": "145,000",
    "Top Product": "Shea Butter Cream",
    "New Clients": 27,
    "Repeat Clients": 15,
    "Customer Feedback": "Positive — many liked the new packaging!",
    "Prepared By": "Antony Karanja"
}

# 3️⃣ Create a new PDF file (your blank paper)
pdf_name = "report.pdf"
pdf = canvas.Canvas(pdf_name, pagesize=A4)

# 4️⃣ Add a heading
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(100, 800, "BRITAFRI MONTHLY SALES REPORT")

# 5️⃣ Add dictionary data line by line
pdf.setFont("Helvetica", 12)
y = 770  # vertical position (starts below heading)
for key, value in sales_report.items():
    pdf.drawString(100, y, f"{key}: {value}")
    y -= 20  # move down for next line

# 6️⃣ Save the PDF
pdf.save()

# 7️⃣ Tell the user it’s done
print("✅ report.pdf created successfully!")

# 8️⃣ Automatically open the PDF after it’s created
try:
    os.startfile(pdf_name)  # works for Windows
except AttributeError:
    # for Mac/Linux systems
    os.system(f"open {pdf_name}" if os.name == "posix" else f"xdg-open {pdf_name}")

