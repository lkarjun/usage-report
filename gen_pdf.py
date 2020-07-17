import datetime 
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

fileName = 'tem/report.pdf'
fileName_Alert = 'tem/Usage_alert.pdf'

doc = SimpleDocTemplate(fileName,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

doc2 = SimpleDocTemplate(fileName_Alert, padsize = letter,
                        rightMargin = 72, leftMargin = 72,
                        topMargin= 72, bottomMargin= 18)

def app_usage_pdf() -> int:
    Story = []
    mainTitle = 'APP USAGE REPORT'
    d = datetime.date.today()
    reportImage = 'tem/figure.png'
    subtitle = 'Daily Report'
    formatted_time = time.ctime()
    im = Image(reportImage,5.5*inch,4*inch)

    styles=getSampleStyleSheet()

    #Main Heading
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="25">%s</font>' % mainTitle
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(2,40))

    #sub heading
    ptext = '<font size="18">%s</font>' % subtitle
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 20))

    #Generating Time
    ptext = '<font size="10">%s</font>' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 20))

    #Matplotlib image display here
    Story.append(im)
    Story.append(Spacer(2,45))

    ptext = '<font size="12">Made with ❤ by LKA</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    doc.build(Story)

    return 0

def usage_alert() -> int:
    Story=[]
    mainTitle = 'USAGE ALERT'
    d = datetime.date.today()
    reportImage = 'tem/figure.png'
    subtitle = 'Apps using high memory and cpu usage.'
    formatted_time = time.ctime()
    im = Image(reportImage,5.5*inch,4*inch)

    styles=getSampleStyleSheet()

    #Main Heading
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size="25">%s</font>' % mainTitle
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(2,40))

    #sub heading
    ptext = '<font size="18">%s</font>' % subtitle
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 20))

    #Generating Time
    ptext = '<font size="10">%s</font>' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 20))

    #Matplotlib image display here
    Story.append(im)
    Story.append(Spacer(2,45))

    ptext = '<font size="12">Made with ❤ by LKA</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    doc2.build(Story)