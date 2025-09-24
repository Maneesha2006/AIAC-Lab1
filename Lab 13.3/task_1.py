def area_rectangle(x, y):
    return x * y

def area_square(x):
    return x * x

def area_circle(x):
    return 3.14 * x * x

AREA_FUNCTIONS = {
    "rectangle": lambda x, y=0: area_rectangle(x, y),
    "square": lambda x, y=0: area_square(x),
    "circle": lambda x, y=0: area_circle(x)
}

def calculate_area(shape, x, y=0):
    if shape not in AREA_FUNCTIONS:
        raise ValueError(f"Unknown shape: {shape}")
    return AREA_FUNCTIONS[shape](x, y)
print(calculate_area("rectangle", 10, 5))  # 50
print(calculate_area("square", 4))         # 16
print(calculate_area("circle", 7))         # 153.86
