def buyut(text):
    return text.upper()

def kucult(text):
    return text.lower()

def test(func, str=""):
    # storing the function in a variable
    sonuc = func(str)
    print(sonuc)

test(buyut, "python programlama dili")
test(kucult, "python programlama dili")
# PYTHON PROGRAMLAMA DILI
# python programlama dili