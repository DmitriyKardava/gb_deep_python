a = int(input("Первая сторона треугольника: "))
b = int(input("Вторая сторона треугольника: "))
c = int(input("Третья сторона треугольника: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
else:
    print("Треугольник не существует")