def main(num=None):
    def validator(num=None):
        return (
            "num" in vars()  # param defined
            and isinstance(num, int)  # param is integer
            and 0 <= num  # param is non-negative
        )

    if validator(num):
        if num > 9:
            return 1
        return 0

    return False
