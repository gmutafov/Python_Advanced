def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []

    for product, qty in products:
        result.append(f"{product}: {qty}")

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
