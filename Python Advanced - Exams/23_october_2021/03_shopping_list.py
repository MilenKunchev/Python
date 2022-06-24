def shopping_list(money, **kwargs):
    in_basket_products = ''
    products_count = 0
    if money < 100:
        return f'You do not have enough budget.'

    for product, params in kwargs.items():
        product_price, product_quantity = params
        total_price = product_price * product_quantity
        if total_price <= money:
            in_basket_products += '\n' + f'You bought {product} for {total_price:.2f} leva.'
            products_count += 1
            money -= total_price
            if products_count == 5:
                break

    return in_basket_products


print(shopping_list(140,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
