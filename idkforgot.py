def q(n,d):
    a = []
    for _ in range(n):
        a.append(int(input()))
        k = a[0] // d + 1
    for i in range(1, n):
        if i + 1 <= k:
            t = a[i] // d + i + 1
            if k < t:
                k = t
        else:
            break
    if k > len(a):
        k = len(a)
    return k
#n=количество лиан,d=длина которую проходит за один прыжок с одной лианы на другую,a=массив расстояний между лианами,выводит сколько до какой лианы можно допрыгнуть
n=3
d=5