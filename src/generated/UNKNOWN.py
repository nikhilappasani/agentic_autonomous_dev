def calculate_area_of_circle(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    import math
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius * radius


def calculate_circumference_of_circle(radius: float) -> float:
    """
    Calculate the circumference of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The circumference of the circle.
    """
    import math
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius


def main():
    """
    Main function to demonstrate the calculation of area and circumference of a circle.
    """
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area_of_circle(radius)
        circumference = calculate_circumference_of_circle(radius)
        print(f"Area of the circle: {area:.2f}")
        print(f"Circumference of the circle: {circumference:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()