import pandas as pd

notas_alunos_dataframe = pd.DataFrame({
    "Nome": ["Luan", "Nadinho", "Pedroka"],
    "nota 1": [7,10,9],
    "nota 2": [6,9,8],
    "nota 3": [7,5,10],
    "nota 4": [10,10,5],
})

notas_alunos_dataframe["media"] = (notas_alunos_dataframe["nota 1"] + notas_alunos_dataframe["nota 2"] + notas_alunos_dataframe["nota 3"] + notas_alunos_dataframe["nota 4"]) / 4

nova_coluna_faltas = [2, 5, 3]

notas_alunos_dataframe["Faltas"] = nova_coluna_faltas

notas_alunos_dataframe.loc[1, "nota 2"] = 6

print(notas_alunos_dataframe)