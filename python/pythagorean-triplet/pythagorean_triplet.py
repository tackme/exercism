from math import gcd


def triplets_with_sum(number):
    primitive_pythagoras = []

    m = 1
    while m ** 2 <= number:
        for n in range(1, m):
            if 2 * m * (m + n) > number:
                break

            if (m - n) % 2 != 0 and gcd(m, n) == 1:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                if a < b:
                    primitive_pythagoras.append([a, b, c])
                else:
                    primitive_pythagoras.append([b, a, c])
        m += 1

    triplet = []

    for a, b, c in primitive_pythagoras:
        if number % (a + b + c) == 0:
            q = number // (a + b + c)
            triplet.append([q * a, q * b, q * c])

    return triplet
