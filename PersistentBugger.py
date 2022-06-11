def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is integer
            and 0 <= num  # param is non-negative
        )

    def digitalproduct(num):
        product = 1
        while num > 0:
            product = product * (num % 10)
            num = num // 10
        return product

    if validator(num):
        if num <= 9:
            return 0
        if digitalproduct(num) <= 9:
            return 1
        return 2
    return False
