#


def escape_velocity(escape_velocity, in_kilometers=True, in_seconds=True):
    if not in_kilometers:
        escape_velocity *= 0.62
    if not in_seconds:
        escape_velocity *= 3600

    return round(escape_velocity, 2)
