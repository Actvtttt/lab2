import matplotlib.pyplot as plt

def brezenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    points = []

    while x <= y:
        #симметричные точки
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y), 
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x), 
            (xc + y, yc - x), (xc - y, yc - x)])

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x- y) + 10
            y -= 1
        x += 1

    return points

def draw_circle(points):

    x_coords, y_coords = zip(*points)

    
    plt.figure(figsize=(7, 7))
    plt.scatter(x_coords, y_coords, s=10, c="orange")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("Растеризация окружности")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

def main():
    print("Введите координаты центра окружности и радиус")
    xc = int(input("Координата x центра: "))
    yc = int(input("Координата y центра: "))
    r = int(input("Радиус окружности: "))

    if r <= 0:
        print("Радиус должен быть положительным")
        return

    points = brezenham_circle(xc, yc, r)
    draw_circle(points)

if __name__ == "__main__":
    main()
