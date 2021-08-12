from reportlab.platypus import *
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
#report.build([report_title])

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])
print(table_data)

#grid = [('GRID', (0,0), (-1,-1), 0.25, colors.black), ('ALIGN', (0,0), (1,-1), 'RIGHT')]
#report_table = Table(data=table_data, style = TableStyle(grid))

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

inch = 3
report_pie = Pie(width=10*inch, height=10*inch)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
print(report_pie.data)
print(report_pie.labels)
report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])
#report.build([report_title, report_table])