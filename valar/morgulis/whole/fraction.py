"""

That is library for whole fraction math

"""

import re

#pattern = re.compile("^([A-Z][0-9]+)+$")
#pattern.match(string)


def check(fraction = ""):
    """Check input string to format \d \d/\d like as 1 1/2 or 3/4
     

    Args:
        fraction (str, optional): String in format. Defaults to "".

    Returns:
        list: List content two item. First item is check result, boolean. Second item is message about error
    """
    
    if re.match("-?\d+$", fraction):
        return [True, 'Good']
    
    if not re.match(r"-?(\d*\s)?\d+/\d+", fraction):
        return [False, 'Wrong format input string']
    
    
    fraction_list = fraction.split("/")
    
    if fraction_list[1] == '0':
        return [False,'Denominator cannot be 0!']
    
    fraction_list_with_whole = fraction_list[0].split(' ')
    
    if fraction_list_with_whole[0] == '0':
        return [False,'Numenator cannot be 0!']
    
    if len(fraction_list_with_whole) == 2 and fraction_list_with_whole[1] == '0':
        return [False,'Numenator cannot be 0!']
    
    return [True, 'Good']

def makeList(fraction = ""):
    """Make list fraction with three item. 

    Args:
        fraction (str, optional): Input string with format. See function check. Defaults to "".

    Returns:
        list: First item is whole part, second - Numerator, thrid - Denominator
    """
    answer = []
    if re.match(r"\d+$",fraction):
        return [int(fraction),0,0]
    fraction_list = fraction.split('/')
    fraction_list_whole_part = fraction_list[0].split(' ')
    if len(fraction_list_whole_part) == 2:
        answer = [fraction_list_whole_part[0], fraction_list_whole_part[1], fraction_list[1]]
    else:
        answer = ['0',fraction_list_whole_part[0],fraction_list[1]]
    return [ int(item) for item in answer ]

def toString( fract = [1,0,0] ):
    """Get string view for fraction list 

    Args:
        fract (list, optional): list with 3 item. See function makeList. Defaults to [0,0,0].

    Returns:
        String: String view for farction list
    """
    if not fract[0] and not fract[1] :
        return "0"
    
    if not fract[1]:
        return "{0}".format(*fract)
    
    if fract[0]:
        return "{0} {1}/{2}".format(*fract)
    return "{1}/{2}".format(*fract)
    
def toNormalize(fract = [1,0,0]):
    """Normalize fraction. f.e 2/2 = 1 or 4/3 = 1 1/3 etc.

    Args:
        fract (list, optional): _description_. Defaults to [0,0,0].

    Returns:
        _type_: _description_
    """
    if not fract[1] or not fract[2]:
        return [fract[0],0,0]
    if fract[2] > fract[1]:
        divider = respectByEvclid([fract[2],fract[1]])
        return [fract[0], fract[1] // divider, fract[2] // divider]
    whole = fract[1] // fract[2]
    remains = fract[1] % fract[2]
    if remains:
        divider = respectByEvclid([fract[2],remains])
        return [fract[0] + whole, remains // divider, fract[2] // divider]
    return [ fract[0] + whole, 0, 0]


def respectByEvclid(numbers = [0,0]):
    """Evclid is very cool man! 
    That is function for finding common divider for two numbers.
    See also: https://ru.wikipedia.org/wiki/Алгоритм_Евклида

    Args:
        numbers (list, optional): fisrt number must by bigger that second number. Defaults to [0,0].

    Returns:
        int: Common divider for two input numbers
    """
    if numbers[0] == numbers[1]:
        return numbers[0]
    remains = numbers[0] - numbers[1]
    if remains > numbers[1]:
        return respectByEvclid([remains,numbers[1]])
    return respectByEvclid([numbers[1], remains])
