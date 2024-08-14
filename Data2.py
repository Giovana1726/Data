import re
from datetime import datetime

# Lista com todos os meses por extenso
meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]


def numero_por_extenso(numero):
    """Converte números em palavras (de 0 a 9999)."""
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    centenas = ["cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
                "oitocentos", "novecentos"]
    milhares = ["", "mil", "dois mil", "três mil", "quatro mil", "cinco mil", "seis mil", "sete mil", "oito mil",
                "nove mil"]

    def _numero_por_extenso(num):
        if 0 <= num < 10:
            return unidades[num]
        elif 10 <= num < 20:
            return especiais[num - 10]
        elif 20 <= num < 100:
            dezena = num // 10
            unidade = num % 10
            return dezenas[dezena] + (" e " + unidades[unidade] if unidade else "")
        elif 100 <= num < 1000:
            centena = num // 100
            resto = num % 100
            if num == 100:
                return "cem"
            return centenas[centena] + (" e " + _numero_por_extenso(resto) if resto else "")
        elif 1000 <= num < 10000:
            milhar = num // 1000
            resto = num % 1000
            if milhar == 1:
                return "mil" + (" e " + _numero_por_extenso(resto) if resto else "")
            return milhares[milhar] + (" e " + _numero_por_extenso(resto) if resto else "")

    return _numero_por_extenso(numero)


# Lista para armazenar as datas convertidas
datas_convertidas = []


def validar_data(data):
    """Valida se a data está no formato DD/MM/AAAA e é uma data válida."""
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def formatar_data(data):
    """Converte a data no formato DD/MM/AAAA para o formato por extenso, incluindo o ano por extenso."""
    dia, mes, ano = map(int, data.split('/'))
    return f"{numero_por_extenso(dia)} de {meses[mes - 1]} de {numero_por_extenso(ano)}"


def obter_data():
    """Pede ao usuário uma data e valida a entrada."""
    while True:
        data = input('Digite a data no formato DD/MM/AAAA: ')
        if validar_data(data):
            return data
        else:
            print("Formato inválido. Digite a data no formato correto.")


def salvar_datas():
    """Salva as datas convertidas em um arquivo."""
    with open('datas_convertidas.txt', 'w') as f:
        for data in datas_convertidas:
            f.write(data + '\n')
    print("Datas salvas no arquivo 'datas_convertidas.txt'.")


def menu():
    """Exibe o menu e processa as escolhas do usuário."""
    while True:
        print("""
1 – Converter Data
2 – Listar Datas
3 – Sair
""")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            data = obter_data()
            data_extenso = formatar_data(data)
            datas_convertidas.append(data_extenso)
            print("Data por extenso:", data_extenso)
        elif escolha == '2':
            if datas_convertidas:
                print("\nDatas por extenso:")
                for data in datas_convertidas:
                    print(data)
            else:
                print("Nenhuma data convertida ainda.")
        elif escolha == '3':
            salvar_datas()
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
