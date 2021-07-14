def convert(number):
    reslut = ''

    if number % 3 == 0:
        reslut += 'Pling'
    if number % 5 == 0:
        reslut += 'Plang'
    if number % 7 == 0:
        reslut += 'Plong' 
    if reslut:
        return reslut
    
    return str(number)
