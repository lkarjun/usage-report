from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


def genPdf() -> int:
    '''
    generates pdf
    '''
    report = SimpleDocTemplate("tem/report.pdf")
    styles =  getSampleStyleSheet()
    report_title = Paragraph("Daily Usage Report", styles["h1"])
    report.build([report_title])

