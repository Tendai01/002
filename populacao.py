populacao_por_ano = {
    2015: 27.12,
    2016: 28.83,
    2017: 29.67,
    2018: 30.37,
    2019: 31.26,
    2020: 32.30,
    2021: 33.25,
    2022: 34.12,
    2023: 35.07,
    2024: 36.04,
}

def contar_populacao(ano):
    try:
        populacao = populacao_por_ano[ano]
        return f"A população de Moçambique em {ano} foi de aproximadamente {populacao} milhões."
    except KeyError:
        return "Ano não encontrado nos dados disponíveis."

x = int (input ("Digite o ano de 2015 ate 2024"))        
        
print (contar_populacao(x))
print ("Luís Pedro Tendai")
print ("RA 204585")
