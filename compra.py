def calculate_prices(car_price):
    discount_rate = 0.20
    increments = {
        6: 0.03,
        12: 0.06,
        18: 0.09,
        24: 0.12,
        30: 0.15,
        36: 0.18,
        42: 0.21,
        48: 0.24,
        54: 0.27,
        60: 0.30
    }

    cash_price = car_price * (1 - discount_rate)
    print(f"O preço final à vista com desconto de 20% é: R$ {cash_price:.2f}")

    for months, increment in increments.items():
        final_price = car_price * (1 + increment)
        installment_value = final_price / months
        print(f"O preço final parcelado em {months} X é de R$ {final_price:.2f} com parcelas de R$ {installment_value:.2f}")

car_price = float(input("Digite o preço do carro:"))
calculate_prices(car_price)
