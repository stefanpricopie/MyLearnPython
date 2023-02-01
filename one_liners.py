### Min-Max: ensure value is bounded by min and max
def min_max_long(x, xu, xl):
    if x > xu:
        return xu
    elif x < xl:
        return xl
    else:
        return x

def min_max_short(x, xu, xl):
    return min(xu, max(xl, x))