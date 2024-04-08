def calculate_installments(debt_amount):
    interest_rates = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }
    
    print(f"{'Valor da dívida':<15} {'Juros':<10} {'Número de parcelas':<20} {'Valor da parcela':<20}")

    for installments, interest_rate in interest_rates.items():
        interest_value = debt_amount * (interest_rate / 100)
        total_debt = debt_amount + interest_value
        installment_value = total_debt / installments
        print(f"R$ {total_debt:<13,.2f} R$ {interest_value:<8,.2f} {installments:<18} R$ {installment_value:<18,.2f}")

debt_amount = float(input("Digite o valor da dívida:"))
calculate_installments(debt_amount)
