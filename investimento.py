def calculate_tax(investment_type, amount, days_invested):
    tax_rates = {
        'cdb': {
            180: 0.225,
            360: 0.20,
            720: 0.175,
            'more': 0.15
        }
    }

    if investment_type == 'cdb':
        if days_invested <= 180:
            rate = tax_rates['cdb'][180]
        elif days_invested <= 360:
            rate = tax_rates['cdb'][360]
        elif days_invested <= 720:
            rate = tax_rates['cdb'][720]
        else:
            rate = tax_rates['cdb']['more']

    return amount * rate

def main():
    print("Tipo de investimento:\n1 - CDB\n2 - LCI\n3 - LCA")
    investment = input("Entre o tipo de investimento (1, 2, ou 3): ")

    if investment not in ['1', '2', '3']:
        print("Valor inválido")
        return

    amount = float(input("Entre o montante a ser investido: "))
    days_invested = int(input("Entre o tempo que o dinheiro se manterá investido, em dias"))

    if investment == '1': 
        tax = calculate_tax('cdb', amount, days_invested)
        print(f"Volume de taxa: R$ {tax:.2f}")
    else:
        print("LCI e LCA são isentos de taxa. Nenhuma taxa foi aplicada")

main()
