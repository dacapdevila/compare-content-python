import pandas as pd


def read_excel_file(path):
    try:
        df = pd.read_excel(path)

        print(df)

        return df

    except FileNotFoundError:
        print(f"El archivo '{path}' no fue encontrado.")
        return None
    except Exception as error:
        print(f"Error al leer el archivo: {error}")
        return None


path_1 = 'FinancialSample.xlsx'
read_excel_file(path_1)

def compare_content(file1, file2):
    try:
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)

        changes = {}
        for column in df1.columns:
            if (df1[column] != df2[column]).any():
                changes[column] = {
                    'file1': df1[column].values.tolist(),
                    'file2': df2[column].values.tolist(),
                }

        if changes:
            print("Changes found:")
            for column, values in changes.items():
                print(f"Columna: {column}")
                print(f"Archivo 1: {values['file1']}")
                print(f"Archivo 2: {values['file2']}")
                print(f"--------------------")
        else:
            print("No se encontraron cambios en las columnas.")

    except FileNotFoundError as error:
        print(f"Error: {error}. Revisa la ruta de los archivos")
    except Exception as error:
        print(f"Error al comparar los archivos: {error}")


file_1 = 'FinancialSample.xlsx'
file_2 = 'FinancialSample.xlsx'
compare_content(file_1, file_2)
