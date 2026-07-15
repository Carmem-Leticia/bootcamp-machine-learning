coluna = df['nome_da_coluna']

filtrado = df[df['idade'] > 30]

filtrado2 = df[(df['idade'] > 30) & (df['cidade'] == 'Fortaleza')]