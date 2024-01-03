from simplify import simplify

def multiply_fractions(frac1,frac2):
    fraction1 = frac1.partition("/")
    numerator1 = int(fraction1[0])
    denominator1 = int(fraction1[2])
    fraction2 = frac2.partition("/")
    numerator2 = int(fraction2[0])
    denominator2 = int(fraction2[2])
    new_fraction = str(numerator1 * numerator2) + "/" + str(denominator1 * denominator2)
    return new_fraction

def numerator(fract):
    if "/" in str(fract):
        fraction = fract.partition("/")
        numerator = int(fraction[0])
    elif "/" not in str(fract):
        numerator = int(fract)
    return numerator

def power(expression):
    new = expression.partition("x^")
    if "/" not in new[2]:
        power = int(new[2]) + 1
    if "/" in new[2]:
        power_frac = new[2].partition("/")
        numerator = power_frac[0]
        denominator = power_frac[2]
        power = f"{(int(numerator) + int(denominator))}/{denominator}"
    return power

def coefficient(expression):
    new = expression.partition("x^")
    if power(expression) == 0:
        return new[0]
    elif "/" not in expression and power(expression) != 0:
        remainder = int(new[0]) % power(expression)
        if remainder == 0:
            new_coefficient = int(int(new[0]) / power(expression))
        else:
            new_coefficient = f"{new[0]}/{power(expression)}"
            new_coefficient = simplify(new_coefficient)
    elif "/" in new[0] and "/" not in new[2]:
        new_coefficient = multiply_fractions(new[0],f"1/{power(expression)}")
    elif "/" in new[0] and "/" in new[2]:
        co_frac = new[0].partition("/")
        co_num = int(co_frac[0])
        co_den = int(co_frac[2])
        po_frac = power(expression).partition("/")
        po_num = int(po_frac[0])
        po_den = int(po_frac[2])
        new_coefficient = f"{co_num*po_den}/{co_den*po_num}"
        new_coefficient = simplify(new_coefficient)
    elif "/" not in new[0] and "/" in new[2]:
        po_frac = power(expression).partition("/")
        po_num = int(po_frac[0])
        po_den = int(po_frac[2])
        new_coefficient = f"{(int(new[0])*po_den)}/{po_num}"
        new_coefficient = simplify(new_coefficient)
    return new_coefficient

def main():
    expression = input("Enter the expression :")
    expression = expression.replace(" - "," -")
    expression = expression.replace(" + "," +")
    x = expression.split(" ")
    new_expressions = ""
    no_power = ""
    for index in x:
        if index[:2] == "+x" or index[:2] == "-x":
            index = index[0] + "1" + index[1:]
        if index[0] == "x":
            index = "1" + index
        if "^" not in index and "x" in index:
            index = index + "^1"
        if "x" not in index:
            no_power = index + "x"
            if int(index) > 0 and "+" not in index:
                no_power = "+" + no_power
            continue
        if power(index) == 0:
            new_expression = str(coefficient(index)) + "ln(x)"
        elif power(index) == 1:
            new_expression = str(coefficient(index)) + "x"
        elif coefficient(index) == 1:
            new_expression = "x^" + str(power(index))
        elif coefficient(index) == -1:
            new_expression = "-x^" + str(power(index))
        else:
            new_expression = str(coefficient(index)) + "x^" + str(power(index))
        c = coefficient(index)
        if numerator(c) > 0 and new_expressions != "":
            new_expressions += " + " + new_expression
        if numerator(c) > 0 and new_expressions == "":
            new_expressions += new_expression
        if numerator(c) < 0 and new_expressions != "":
            new_expressions += " - " + new_expression[1:]
        if numerator(c) < 0 and new_expressions == "":
            new_expressions += new_expression
    if no_power != "" and new_expressions != "":
        if "+" in no_power:
            no_power = " + " + no_power[1:]
        if "-" in no_power:
            no_power = " - " + no_power[1:]
    print(new_expressions + no_power)
    menu()

def menu():
    main()
#menu()

def integrate(expression):
    expression = expression.replace(" - "," -")
    expression = expression.replace(" + "," +")
    x = expression.split(" ")
    new_expressions = ""
    no_power = ""
    for index in x:
        if index[:2] == "+x" or index[:2] == "-x":
            index = index[0] + "1" + index[1:]
        if index[0] == "x":
            index = "1" + index
        if "^" not in index and "x" in index:
            index = index + "^1"
        if "x" not in index:
            no_power = index + "x"
            if int(index) > 0 and "+" not in index:
                no_power = "+" + no_power
            continue
        if power(index) == 0:
            new_expression = str(coefficient(index)) + "ln(x)"
        elif power(index) == 1:
            new_expression = str(coefficient(index)) + "x"
        elif coefficient(index) == 1:
            new_expression = "x^" + str(power(index))
        elif coefficient(index) == -1:
            new_expression = "-x^" + str(power(index))
        else:
            new_expression = str(coefficient(index)) + "x^" + str(power(index))
        c = coefficient(index)
        if numerator(c) > 0 and new_expressions != "":
            new_expressions += " + " + new_expression
        if numerator(c) > 0 and new_expressions == "":
            new_expressions += new_expression
        if numerator(c) < 0 and new_expressions != "":
            new_expressions += " - " + new_expression[1:]
        if numerator(c) < 0 and new_expressions == "":
            new_expressions += new_expression
    if no_power != "" and new_expressions != "":
        if "+" in no_power:
            no_power = " + " + no_power[1:]
        if "-" in no_power:
            no_power = " - " + no_power[1:]
    answer = (new_expressions + no_power)
    return answer