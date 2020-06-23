from pdfCreate import pdf
from help import register_font
from content import cont_obj
from text_obj import textObj
from reportlab.platypus import Frame, SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import PageBreak
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
import stylez
from reportlab.pdfgen.canvas import Canvas


register_font(cont_obj.fonts['title'])
register_font(cont_obj.fonts['regular'])
register_font(cont_obj.fonts['light'])
register_font(cont_obj.fonts['else'])
canv = Canvas('folderLex1.pdf')
stylesheet = stylez.stylesheet()


def first_page(canvas, doc):
    canvas.saveState()
    draw_background(cont_obj.frontpage_img)
    pdf.setFont(cont_obj.fonts['regular'], 48)
    add_paragraph(cont_obj.frontpage_edit, (cont_obj.page_size[0] / 2), (cont_obj.page_size[1] / 2 + 200), (500, 500))
    pdf.setFont(cont_obj.fonts['light'], 64)
    add_paragraph(cont_obj.frontpage_whom, (cont_obj.page_size[0] / 2), (cont_obj.page_size[1] / 2), (500, 500))
    canvas.restoreState()


def nxt_page(canvas, doc):
    canvas.saveState()
    canvas.restoreState()
    draw_background(cont_obj.background_img)


def go():
    doc = SimpleDocTemplate(cont_obj.doc_title)
    Story = [Spacer(1, 2 * inch)]
    Story.append(PageBreak())
    styles = stylez.stylesheet()
    p = Paragraph(cont_obj.p4_text, styles['Heading'])
    Story.append(p)
    Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story, onFirstPage=first_page, onLaterPages=nxt_page)
    pdf.save()


def add_paragraph(text, x, y, size, style='Lejzi'):
    text = Paragraph(text, stylesheet[style])
    w, h = text.wrap(size[0], size[1])
    if w <= size[0] and h <= size[1]:
        text.drawOn(pdf, x, y)
        height = size[1] - h

    else:
        raise ValueError


def draw_background(image):
    pdf.drawImage(image, 0, 0)


def add_frame(story, x, y, size):
    frame = Frame(x, y, size[0], size[1], showBoundary=1)
    frame.addFromList(story, pdf)



go()