#Manipulando alguns dados pera tranformar em porcentagem
#EM DAX PARA O POWER BI

PorcentagemConsultasPorHora = 
DIVIDE(
    CALCULATE(
        COUNT(DRG_GERENCIAL[ConsultaID]),
        FILTER(
            ALL(DRG_GERENCIAL),
            DRG_GERENCIAL[Hora] = MAX(DRG_GERENCIAL[Hora])
        )
    ),
    CALCULATE(
        COUNT(DRG_GERENCIAL[ConsultaID]),
        ALL(DRG_GERENCIAL)
    )
)

#EM PYTHON


import pandas as pd

# Supondo que você tenha um DataFrame chamado df contendo seus dados
# Vou criar um exemplo simplificado

# Exemplo de dados
data = {
    'ConsultaID': [1, 2, 3, 4, 5],
    'Hora': ['09:00', '09:00', '10:00', '11:00', '11:00']
}

# Criando DataFrame
df = pd.DataFrame(data)

# Convertendo a coluna 'Hora' para o tipo datetime
df['Hora'] = pd.to_datetime(df['Hora'])

# Calculando a porcentagem de consultas por hora
porcentagem_consultas_por_hora = (
    df.groupby('Hora')['ConsultaID'].count() / len(df) * 100
)

print(porcentagem_consultas_por_hora)
