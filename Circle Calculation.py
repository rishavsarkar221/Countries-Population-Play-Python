def circle_calc(pie):
    try:
        radius = round(float(input("Enter Radius of the Circle: ")), 2)

        area = round(pie * (radius ** 2))
        circumference = round(2 * pie * radius)
        diameter = round(2 * radius)

        return print(f"Area: {str(area)}\nCircumference: {str(circumference)}\nDiameter: {str(diameter)}")

    except ValueError:
        print("Enter Numbers only for radius")


circle_calc(3.14)