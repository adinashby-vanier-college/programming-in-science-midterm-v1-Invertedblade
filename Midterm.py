import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    result = round((math.pi) * (radius ** 2), 2)
    return result

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""
    if n > 4:
        for i in range(1, n)
            for j in range(1, i + 1)
                result += "*"
    else:
        return "The pyramid height should be at least 4."


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    if n > 3:
    for i in range(1, n):
        for j in range(1, i + 1):
            result += " " + ("*" * (n + 2))
        result += "\n"
        n -= 2
    return result
else:
        return "The pyramid height should be at least 3."


# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()