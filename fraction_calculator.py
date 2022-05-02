
import valar.morgulis.whole.fraction as fr
import valar.morgulis.whole.operations as frops
import re

hello = """
Hello!
That is simple interactive calculator for whole fractions.
This program can add, subtract, multiply and divide integer fractions.

Only for you, my daughter
Valar Morgulis, 2022  
"""

message_help = """
Please input whole fraction like as
1 1/2
or
3/4
If you want to exit that programm, please input word exit or quit.
"""

print(hello)
print(message_help)

number1 = "0"
print ("0")
current_operation = "="
while True:
    input_value = input('')
    message_fracts = fr.check(input_value)
    fract_number1 = fr.toNormalize(fr.makeList(number1))
    if input_value == "":
        print(number1)
        continue
    if input_value == 'exit' or number1 == 'quit':
        break
    if re.match('[+-/\*\:]',input_value):
        current_operation = input_value
        continue
    if message_fracts[0]:
        fract_number2 = fr.toNormalize(fr.makeList(input_value))
        answer = [0,0,0]
        if current_operation == "=":
            number1 = input_value
            continue
        if current_operation == "+":
            answer = frops.sum(fract_number1,fract_number2)
        if current_operation == "-":
            answer = frops.diff(fract_number1,fract_number2)
        if current_operation == ":" or current_operation == "/":
            answer = frops.division(fract_number1,fract_number2)
        if current_operation == "*":
            answer = frops.multiple(fract_number1,fract_number2)
        number1 = fr.toString(answer)
        print("=")
        current_operation = "="
    else:
        print("ERROR:")
        print(message_fracts[1])
        print(message_help)
    print(number1)