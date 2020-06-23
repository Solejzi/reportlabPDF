from pdfCreate import pdf
from help import register_font
from content import cont_obj

import stylez
from reportlab.pdfgen.canvas import Canvas



canv = Canvas('pdfpdf.pdf')
stylesheet = stylez.stylesheet()
def draw_background(image):
    pdf.drawImage(image, 0, 0)

def first_page(canvas, doc, img):
    canvas.saveState()
    draw_background(img)
    canvas.restoreState()
