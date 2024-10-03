import pandas as pd
import numpy as np

#dataFrame_Meses = pd.date_range("20221231", periods=12, freq="M")

#print(dataFrame_Meses)

#numeros_aleatorios = pd.DataFrame(np.random.rand(15,10)*100)

#print(numeros_aleatorios)

notas_alunos = pd.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao"],
    "Media": ["9", "7", "10"]
})

print(notas_alunos)