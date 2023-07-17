# solve for pressure, but using keyword parameter for R


def find_pressure(mol, temp, vol, R=0.082057):
    return mol * R * temp / vol
