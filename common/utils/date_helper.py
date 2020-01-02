from datetime import date


def test():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("d1 =", d1)
    # Textual month, day and year
    d2 = today.strftime("%B %d, %Y")
    print("d2 =", d2)
    # mm/dd/y
    d3 = today.strftime("%m/%d/%y")
    print("d3 =", d3)
    # Month abbreviation, day and year
    d4 = today.strftime("%b-%d-%Y")
    print("d4 =", d4)


def current_yyyy_mm_dd():
    today = date.today()
    return today.strftime("%Y/%m/%d")

# if __name__ == "__main__":
#     print(current_yyyy_mm_dd())
