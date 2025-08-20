import pandas as pd
import glob, os

# Caminho da pasta onde estão os CSVs
path = './processed'  # se rodar o script dentro de dataset_ia_llm

# Busca todos os arquivos CSV
all_files = glob.glob(os.path.join(path, "*.csv"))
print("Arquivos encontrados:", all_files)

if not all_files:
    print("Nenhum arquivo CSV encontrado no caminho:", path)
else:
    # Lê cada arquivo CSV e junta
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)

    # Salva no arquivo final
    output_file = 'combined.csv'
    concatenated_df.to_csv(output_file, encoding='utf-8-sig', index=False)
    print("Arquivo combinado salvo em:", output_file)
