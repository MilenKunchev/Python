

def stock_availability(boxes, *args):
    command = args[0]

    if command == 'delivery':
        [boxes.append(x) for x in args[1:]]
        return boxes
    # sell
    else:
        if len(args) > 1 and isinstance(args[1], int):
            count = int(args[1])
            return boxes[count:]
        if len(args) > 1 and isinstance(args[1], str):
            return [x for x in boxes if x not in args]
        return boxes[1:]


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
