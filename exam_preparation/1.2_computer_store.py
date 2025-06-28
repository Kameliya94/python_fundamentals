DISCOUNT_FOR_SPECIAL = 0.1

prices = []
taxes = 0

while True:
    command = input()

    if command == "special":
        if sum(prices) == 0:
            print("Invalid order!")
            break
        else:
            print(f"Congratulations you've just bought a new computer!"
              f"\nPrice without taxes: {sum(prices):.2f}$"
              f"\nTaxes: {taxes:.2f}$\n-----------"
              f"\nTotal price: {((sum(prices) + taxes) - ((sum(prices) + taxes) * DISCOUNT_FOR_SPECIAL)):.2f}$")
        break

    elif command == "regular":
        if sum(prices) == 0:
            print("Invalid order!")
            break
        else:
            print(f"Congratulations you've just bought a new computer!"
              f"\nPrice without taxes: {sum(prices):.2f}$"
              f"\nTaxes: {taxes:.2f}$\n-----------"
              f"\nTotal price: {(sum(prices) + taxes):.2f}$")
        break

    else:
        if float(command) < 0:
            print("Invalid price!")
            continue
        else:
            taxes += (float(command) * 0.2)
            prices.append(float(command))