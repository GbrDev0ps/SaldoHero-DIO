def calcula_nivel(vitorias, derrotas):
    saldo = vitorias - derrotas    
    
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = 'Imortal'    
        
    return f"O herói tem saldo de {saldo} e esta no nivel de {nivel}"

vitorias = int(input('Digite o numero de vitórias: '))
derrotas = int(input('Digite o numero de derrotas: '))

mensagem = calcula_nivel(vitorias, derrotas)
print(mensagem)
