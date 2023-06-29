class Monomial:
    def __init__(self, a, k: list) -> None:
        self.a = a
        self.k = k

    def is_monomial(self) -> bool:
        for exponent in self.k:
            if not (exponent // 1 == exponent and exponent >= 0):
                return False
        return True

    def find_max_exponent(self):
        return max(self.k)

    def is_constant(self) -> bool:
        # if self.k == [0]:
        #     return True
        # else:
        #     return False
        # return self.k == [0]
        return sum(self.k) == 0

    def find_number_of_vars(self) -> int:
        if self.is_constant():
            return 0
        return len(self.k)

    def __str__(self) -> str:
        result = ""
        # ต้องการบวก a เข้าไปใน string
        result += str(self.a)
        for i, exponent in enumerate(self.k):
            # [2, 1, 6] -> i=0, e=2 -> i=1, e=1 -> i=2, e=6
            if exponent == 1:
                result += f"x_{i}"
            elif exponent == 0:
                continue
            else:
                result += f"x_{i}^{exponent}"

        return result


def is_addable(m1: Monomial, m2: Monomial) -> bool:
    # if m1.k == m2.k:
    #     return True
    # else:
    #     return False
    return m1.k == m2.k


def add_two_monomial(m1: Monomial, m2: Monomial) -> Monomial:
    if not is_addable(m1, m2):
        return None

    result_coefficient = m1.a + m2.a

    return Monomial(a=result_coefficient, k=m1.k)

def multiply_two_monomial(m1: Monomial, m2: Monomial) -> Monomial:
    result_coefficient = m1.a * m2.a
    result_exponents = []
    
    for i in range(len(m1.k)):
        result_exponents.append(m1.k[i] + m2.k[i])
    
    return Monomial(a=result_coefficient, k=result_exponents)
        
    
m1 = Monomial(a=6, k=[2, 1])
m2 = Monomial(a=-10, k=[2, 1])
print(multiply_two_monomial(m1, m2))
