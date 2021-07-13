def convert(number):
    reslut = []
    if number % 3 == 0:
        reslut.append("Pling")
    if number % 5 == 0:
        reslut.append("Plang")
    if number % 7 == 0:
        reslut.append("Plong")
    if not reslut:
        reslut.append(str(number))
    
    reslut_str = ''.join(reslut)

    return reslut_str

