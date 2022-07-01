def get_number_from_string(price):
    return price.split(' ')[0]

def get_price_from_string(price):
    return float(get_number_from_string(price).replace('.', '').replace(',', '.'))

def get_normal_number_from_string(price):
    return price.split(' ')[0]

def get_normal_price_from_string(price):
    try:
        return float(get_normal_number_from_string(price).replace('.', '').replace(',', '.'))
    except:
        return 0