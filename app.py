def calculate_total(price, quantity):
    total = price * quantity
    return total


def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False


def process_data(data):
    result = []
    for item in data:
        result.append(item * 2)

    return result
