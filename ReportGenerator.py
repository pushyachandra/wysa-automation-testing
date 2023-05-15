from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.validators import Auto
from reportlab.graphics.charts.legends import Legend

def generate_pie_chart(pdf,pass_count,fail_count):
    data=[pass_count,fail_count]
    labels = ['Pass Count','Fail Count']
    pie_colors=[colors.green, colors.red]
    drawing = Drawing(400, 200)

    pie = Pie()
    pie.x = 150
    pie.y = 50
    pie.width = 200
    pie.height = 200
    pie.data = data
    pie.labels = labels
    pie.slices.strokeWidth = 0.5

    for i, color in enumerate(pie_colors):
        pie.slices[i].fillColor = color

    drawing.add(pie)
    
    legend = Legend()
    legend.alignment = 'left'
    legend.x = 10
    legend.y = 70
    legend.colorNamePairs = Auto(obj=pie)
    drawing.add(legend)

    drawing.wrapOn(pdf, 50, 400)
    drawing.drawOn(pdf, 50, 400)
    
    return pdf
    

def generate_report(pass_count, fail_count, report_file):
    try:
        total_test_cases = pass_count + fail_count

        pdf = canvas.Canvas(report_file, pagesize=letter)

        data = [
            ['Number of Test Cases', 'Passed Cases Count', 'Failed Cases Count', 'Pass Rate', 'Fail Rate'],
            [total_test_cases, pass_count, fail_count, f'{pass_count/total_test_cases:.2%}', f'{fail_count/total_test_cases:.2%}']
        ]

        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        table = Table(data)
        table.setStyle(table_style)

        table.wrapOn(pdf, 50, 700)
        table.drawOn(pdf, 50, 700)

        title_text = "Automation Test Report"
        pdf.setFont('Helvetica-Bold', 16)
        pdf.drawCentredString(300, 750, title_text)
        
        pdf=generate_pie_chart(pdf,pass_count,fail_count)

        pdf.save()
    except Exception as error:
        print("Oops from Report Generation")
        print("The Error is",error)