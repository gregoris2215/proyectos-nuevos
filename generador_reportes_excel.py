# generador_reportes_excel.py

import pandas as pd

def generar_reporte():
    datos = {
        'Nombre': ['Ana', 'Luis', 'Pedro', 'María'],
        'Ventas': [1500, 2400, 1200, 1800],
        'Objetivo': [2000, 2500, 1500, 2000]
    }
    
    df = pd.DataFrame(datos)
    df['Diferencia'] = df['Ventas'] - df['Objetivo']
    df.to_excel('reporte_ventas.xlsx', index=False)

def main():
    generar_reporte()
    print("Reporte generado exitosamente como 'reporte_ventas.xlsx'")

if __name__ == "__main__":
    main()
