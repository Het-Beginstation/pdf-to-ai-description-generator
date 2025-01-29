import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment

def save_to_excel(descriptions, ai_descriptions_file):
    try:
        df = pd.DataFrame(descriptions)
        df.to_excel(ai_descriptions_file, index=False)
    except Exception as e:
        print(f"Error saving to Excel: {e}")
        raise

def adjust_excel_formatting(ai_descriptions_file, max_column_width=50):
    try:
        wb = load_workbook(ai_descriptions_file)
        ws = wb.active

        for col in ws.columns:
            column = col[0].column_letter
            ws.column_dimensions[column].width = max_column_width
            for cell in col:
                cell.alignment = Alignment(wrap_text=True, vertical='top')

        ws.row_dimensions[1].height = None

        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical='top')
            ws.row_dimensions[row[0].row].height = 200

        wb.save(ai_descriptions_file)
        print(f'Saved all AI descriptions to {ai_descriptions_file}')
    except Exception as e:
        print(f"Error adjusting Excel formatting: {e}")
        raise