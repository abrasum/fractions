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
    
    if not re.match(r"(\d*\s)?\d+/\d+", fraction):
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
    fraction_list = fraction.split('/')
    fraction_list_whole_part = fraction_list[0].split(' ')
    if len(fraction_list_whole_part) == 2:
        answer = [fraction_list_whole_part[0], fraction_list_whole_part[1], fraction_list[1]]
    else:
        answer = ['0',fraction_list_whole_part[0],fraction_list[1]]
    return [ int(item) for item in answer ]

def toString( fract = [] ):
    """Get string view for fraction list 

    Args:
        fract (list, optional): list with 3 item. See function makeList. Defaults to [].

    Returns:
        String: String view for farction list
    """
    if fract[0] == 0 and fract[1] == 0 and fract[2] == 0:
        return "0"
    
    if not fract[1]:
        return "{0}".format(*fract)
    
    if fract[0]:
        return "{0} {1}/{2}".format(*fract)
    return "{1}/{2}".format(*fract)
    
def toNormalize(fract = []):
    answer = []
    return answer