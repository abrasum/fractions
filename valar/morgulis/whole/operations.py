
import valar.morgulis.whole.fraction as fraction
#import fraction


def sum(first = [1,0,0], second = [1,0,0] ):
    fun = fraction.unNormalize(first)
    sun = fraction.unNormalize(second)
    return fraction.toNormalize([ 0, fun[1]*sun[2] + sun[1]*fun[2], fun[2]*sun[2]])

def diff(first = [1,0,0], second = [1,0,0] ):
    first_unnormal = fraction.unNormalize(first)
    second_unnormal = fraction.unNormalize(second)
    return fraction.toNormalize([ 0, first_unnormal[1]*second_unnormal[2] - second_unnormal[1]*first_unnormal[2], first_unnormal[2]*second_unnormal[2]])

def multiple(first = [0,0,0], second = [0,0,0]):
    fun = fraction.unNormalize(first)
    sun = fraction.unNormalize(second)
    return fraction.toNormalize([ 0, fun[1]*sun[1], fun[2]*sun[2]])

def division (first = [2,0,0], second = [1,0,0]):
    fun = fraction.unNormalize(first)
    sun = fraction.unNormalize(second)
    return fraction.toNormalize([ 0, fun[1]*sun[2], fun[2]*sun[1]])