import os
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from turtle import width
from reportlab.lib.pagesizes import landscape,A4, letter
from reportlab.pdfgen import canvas

#-------------- VARIABLES --------------

# ---------------- MEDIDAS DE LOS CURSOS -------------------
# JESUCRISTO Y EL EVANGELIO SEMPITERNO
w_jesus = 170  # Este va primero como parametro
h_jesus = 290  # Este va segundo como parametro 

# LA FAMILIA ETERNA
w_fam = 274 # Este va primero como parametro
h_fam = 290 # Este va primero como parametro

# FUNDAMENTOS DE LA RESTAURACION ---- 30 Caracteres
w_fund = 206 # Este va primero como parametro
h_fund = 290 # Este va primero como parametro

# ENSEÑANZAS Y DOCTRINA DEL LIBRO DE MORMÓN ---- 41 Caracteres
w_teachings = 143 # Este va primero como parametro
h_teachings = 290 # Este va primero como parametro

# SIZES
width, height = letter




center = height / 2



herrera_axel = 260

# SIZE NAMES
w_name = 288 # Este va primero como parametro
h_name = 358 # Este va primero como parametro


#-------------- FUNCTIONS --------------

nombre = input("Coloque el nombre del estudiante: ")
curso = input("Coloque el nombre del curso: ")
fecha = input("Coloque la fecha: ")

nombre_caracters = 0
curso_caracters = 0

def registerFont():
    # SEARCH THE FOLDER FONT
    reportlab_directory = os.path.dirname(reportlab.__file__)
    font_folder = os.path.join(reportlab_directory, "fonts")
    custom_font_folder = os.path.join(font_folder, "PalaceS.ttf")

    # REGISTERING THE FONT
    custom_font = TTFont("palace_certificate", custom_font_folder)
    pdfmetrics.registerFont(custom_font)

    return custom_font


# WORKING WITH THE FILE 
def workPDF(nombre, curso_caracters, nombre_caracters):
    
    # THIS CREATES A NEW FILE
    pdf = canvas.Canvas(f'{nombre}.pdf')
    
    # THIS SETS THE PAGE SIZE
    canvas.Canvas.setPageSize(pdf, (landscape(letter)))

    # PASTE THE CERTIFICATE TEMPLATE
    pdf.drawImage("certificado_a.jpg", 0, 0, height  ,width  )

    # WRITES THE COURSE NAME
    for courses in curso:
        curso_caracters += 1
    if curso_caracters == 41:
        pdf.setFont('Times-Roman', 30)
        pdf.drawString(w_teachings , 290 , curso)
    elif curso_caracters == 30:
        pdf.setFont('Times-Roman', 30)
        pdf.drawString(w_fund , 290 , curso)
    elif curso_caracters == 36:
        pdf.setFont('Times-Roman', 30)
        pdf.drawString(w_jesus , 290 , curso)
    else:
        pdf.setFont('Times-Roman', 30)
        pdf.drawString(w_fam , 290 , curso)
     
    # WRITES THE DATE 
    pdf.setFont('Times-Roman', 16)
    pdf.drawString(348, 265, fecha)

    # WRITES THE STUDENT NAME

    for name in nombre:
        nombre_caracters += 1
    
    pixels = nombre_caracters * 10
    correct_position = center - pixels

    if nombre_caracters >= 20:
        pixels = nombre_caracters * 10.1
    elif nombre_caracters > 12:
        pixels = nombre_caracters * 10.05

    pdf.setFont('palace_certificate', 68)
    pdf.drawString(correct_position, 358, nombre)

    pdf.save()
    
#def main():

registerFont()
workPDF(nombre, curso_caracters, nombre_caracters)


#main()















