# adding a catch for zero division to PV = nRT


def find_pressure(mol, temp, vol, R=0.082057):
    try:
        return mol * R * temp / vol
    except ZeroDivisionError:
        return "Volume must be greater than 0."
