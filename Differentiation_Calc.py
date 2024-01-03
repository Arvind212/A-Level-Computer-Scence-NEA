def numerator(fract):
    if "/" in str(fract):
        fraction = fract.partition("/")
        numerator = int(fraction[0])
    elif "/" not in str(fract):
        numerator = int(fract)
    return numerator

# Takes 1 away from the fraction by taking away the denominator from the numerator
def fract_minus_one(fract):
    fraction = fract.partition("/")
    numerator = int(fraction[0])
    denominator = int(fraction[2])
    new_fraction = str(numerator - denominator) + "/" + str(denominator)
    return new_fraction

# Multiplies two fractions together
def multiply_fractions(frac1,frac2):
    fraction1 = frac1.partition("/")
    numerator1 = int(fraction1[0])
    denominator1 = int(fraction1[2])
    fraction2 = frac2.partition("/")
    numerator2 = int(fraction2[0])
    denominator2 = int(fraction2[2])
    new_fraction = str(numerator1 * numerator2) + "/" + str(denominator1 * denominator2)
    return new_fraction

# Finds the new coefficient by multiplying the power to the old coefficient
# if power and old coefficient is a fraction then it will use the multiply fractions function
def coefficient(expression):
    new = expression.partition("x^")
    coefficient = 0
    if "/" in new[0] and "/" in new[2]:
        coefficient = multiply_fractions(new[0],new[2])
    if "/" in new[0] and "/" not in new[2]:
        power = new[2] + "/1"
        coefficient = multiply_fractions(new[0],power)
    if "/" not in new[0] and "/" in new[2]:
        coefficient_fract = new[0] +"/1"
        coefficient = multiply_fractions(coefficient_fract,new[2])
    if "/" not in new[0] and "/" not in new[2] and new[0] != "":
        coefficient = int(new[0]) * int(new[2])
    return coefficient

# Finds the new power by taking away 1 from the old power
# if the power is a fraction then it uses the fract_minus_one function
def power(expression):
    new = expression.partition("x^")
    power = 0
    if "/" in new[2]:
        power = fract_minus_one(new[2])
    if "/" not in new[2]:
        power = int(new[2])
        power -= 1
    return power

def differentiate(expression):
        expression = expression.replace(" - "," -")
        expression = expression.replace(" + "," +")
        x = expression.split(" ")
        new_expressions = ""
        no_power = ""
        for index in x:
            if index[:2] == "+x" or index[:2] == "-x":
                index = index[0] + "1" + index[1:]
            elif index[0] == "x":
                index = "1" + index
            if "^" not in index and "x" in index:
                no_power = index[:-1]
                if int(no_power) > 0 and "+" not in no_power:
                    no_power = "+" + no_power
                continue
            if "x" not in index:
                continue
            new_expression = str(coefficient(index)) + "x^" + str(power(index))
            if power(index) == 1:
                new_expression = str(coefficient(index)) + "x"
            # if the coefficient is an integer
            c = coefficient(index)
            if numerator(c) > 0 and new_expressions != "":
                new_expressions += " + " + new_expression
            if numerator(c) > 0 and new_expressions == "":
                new_expressions += new_expression
            if numerator(c) < 0 and new_expressions != "":
                new_expressions += " - " + new_expression[1:]
            if numerator(c) < 0 and new_expressions == "":
                new_expressions += new_expression
        # checks if the numerator is a negative or positive number
        # then a "+" or "-" is added before the number
        if no_power != "":
            s = int(numerator(no_power))
            if s > 0 and new_expressions != "":
                no_power = " + " + no_power[1:]
            if s < 0 and new_expressions != "":
                no_power = " - " + no_power[1:]
        answer = (new_expressions + no_power)
        return answer

def main():
    expression = input("Enter the expression you would like to differentiate :")
    expression = expression.replace(" - "," -")
    expression = expression.replace(" + "," +")
    x = expression.split(" ")
    new_expressions = ""
    no_power = ""
    for index in x:
        if index[:2] == "+x" or index[:2] == "-x":
            index = index[0] + "1" + index[1:]
        elif index[0] == "x":
            index = "1" + index
        if "^" not in index and "x" in index:
            no_power = index[:-1]
            if int(no_power) > 0 and "+" not in no_power:
                no_power = "+" + no_power
            continue
        if "x" not in index:
            continue
        new_expression = str(coefficient(index)) + "x^" + str(power(index))
        if power(index) == 1:
            new_expression = str(coefficient(index)) + "x"
        # if the coefficient is an integer
        c = coefficient(index)
        if numerator(c) > 0 and new_expressions != "":
            new_expressions += " + " + new_expression
        if numerator(c) > 0 and new_expressions == "":
            new_expressions += new_expression
        if numerator(c) < 0 and new_expressions != "":
            new_expressions += " - " + new_expression[1:]
        if numerator(c) < 0 and new_expressions == "":
            new_expressions += new_expression
    # checks if the numerator is a negative or positive number
    # then a "+" or "-" is added before the number
    if no_power != "":
        s = int(numerator(no_power))
        if s > 0 and new_expressions != "":
            no_power = " + " + no_power[1:]
        if s < 0 and new_expressions != "":
            no_power = " - " + no_power[1:]
    print(new_expressions + no_power)
    menu()

def menu():
    main()
#menu()