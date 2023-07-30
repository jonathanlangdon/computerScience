# validate a credit card


def validate_card(number, cvv, expiration_month, expiration_year, provider="Visa"):
    try:
        int(number) and int(cvv)
    except:
        return False
    if expiration_month not in range(1, 13):
        return False
    if expiration_year not in range(22, 29):
        return False
    if provider not in ["Visa", "MasterCard", "Discover", "American Express"]:
        return False
    if provider == "American Express":
        if len(number) != 15:
            return False
        if len(cvv) != 4:
            return False
    else:
        if len(number) != 16:
            return False
        if len(cvv) != 3:
            return False
    return True
