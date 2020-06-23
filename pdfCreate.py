from reportlab.pdfgen import canvas
from content import cont_obj

pdf = canvas.Canvas(cont_obj.file_name)
pdf.setTitle(cont_obj.doc_title)
pdf.setPageSize(cont_obj.page_size)


