def find_common(a, b):
    return list(set(a) & set(b))

if __name__ == "__main__":
    a = input("Enter first list of elements separated by spaces: ").split()
    b = input("Enter second list of elements separated by spaces: ").split()
    result=find_common(a,b)
    print("Common elements in ascending order:", sorted(map(int, result)))