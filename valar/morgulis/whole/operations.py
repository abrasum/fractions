import fraction

def sum(first = [1,0,0], second = [1,0,0] ):
    return fraction.toNormalize([ first[0] + second[0], first[1]*second[2] + second[1]*first[2], first[2]*second[2]])

def diff(first = [1,0,0], second = [1,0,0] ):
    return fraction.toNormalize([ first[0] - second[0], first[1]*second[2] - second[1]*first[2], first[2]*second[2]])

def multiple(first = [0,0,0], second = [0,0,0]):
    return fraction.toNormalize([ first[0]*second[0], first[1]*second[1], first[2]*second[2]])

def division (first = [2,0,0], second = [1,0,0]):
    return fraction.toNormalize([ first[0]*second[0], first[1]*second[1], first[2]*second[2]])