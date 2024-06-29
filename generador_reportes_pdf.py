# generador_reportes_pdf.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_reporte():
    c = canvas.Canvas("reporte_ventas.pdf", pagesize=letter)
    c.drawString(100, 750, "Reporte de Ventas")
    c.drawString(100, 730, "Nombre del Producto: Producto 1")
    c.drawString(100, 710, "Ventas: $1500")
    c.drawString(100, 690, "Objetivo: $2000")
    c.drawString(100, 670, "Diferencia: -$500")

    c.save()

def main():
    generar_reporte()
    print("Reporte generado exitosamente como 'reporte_ventas.pdf'")

if __name__ == "__main__":
    main()
