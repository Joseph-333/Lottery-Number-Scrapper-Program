import urllib.request
from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Site to download data
# https://www.lottomaxnumbers.com/numbers/2023
url = input('Website-')
pdf_title = input('File Title-')

with urllib.request.urlopen(url) as file:
    r_file = file.read()

    soup = BeautifulSoup(r_file, 'html.parser')

    arr = []

    for line in soup.find_all(class_='ball'):
        if 'bonus-ball' in line['class']:
            continue
        ball_numbers = int(line.text)

        # Put each one into an array
        arr.append(ball_numbers)

    sets_of_seven = [arr[i:i + 7] for i in range(0, len(arr), 7)]

# Create a PDF document object
doc = SimpleDocTemplate(f'{pdf_title}.pdf', pagesize=letter)

# Create a table with the data
table = Table(sets_of_seven)

# Apply the style to the table
style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])
table.setStyle(style)

# Add the table to the PDF document
doc.build([table])