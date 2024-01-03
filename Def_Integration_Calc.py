from Integration_Calc import integrate

class Def_Integration_Calc:
    def __init__(self,expression,upper_limit,lower_limit):
        self.expression = expression
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
    
    def def_integral(self):
        integral = integrate(self.expression)
        integral = integral.replace(" + "," +")
        integral = integral.replace(" - "," -")
        integral = integral.split(" ")
        upper_answer = 0
        lower_answer = 0
        answer = 0
        for index in integral:
            if index[:2] == "+x" or index[:2] == "-x":
                index = index[0] + "1" + index[1:]
            if index[0] == "x":
                index = "1" + index
            if "^" not in index and "x" in index:
                index = index + "^1"
            index = index.split("x^")
            if "/" in index[0]:
                x = index[0].split("/")
                index[0] = str(int(x[0]) / int(x[1]))
            if "/" in index[1]:
                x = index[1].split("/")
                index[1] = str(int(x[0]) / int(x[1]))
            upper_answer += float(index[0]) * (self.upper_limit**(float(index[1])))
            lower_answer += float(index[0]) * (self.lower_limit**(float(index[1])))
            answer = (upper_answer - lower_answer)
        return(str(answer))