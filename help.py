from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def register_font(font):
    ttf = font + '.ttf'
    pdfmetrics.registerFont(TTFont(font, ttf))

def fonts(pdf):
    for font in pdf.getAvailableFonts():
        print(font)
