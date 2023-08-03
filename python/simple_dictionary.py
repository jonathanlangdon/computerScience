# lookup a key to see if is in a dictionary


def safe_lookup(adict, akey):
    if akey in adict:
        return adict[akey]
    else:
        return None
