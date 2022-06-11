def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is integer
            and 0 <= num  # param is non-negative
        )

    if validator(num):
        return int(num > 9)
    return False
