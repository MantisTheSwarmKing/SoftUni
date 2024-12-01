

shape = input()

if shape == 'square':
    size = float(input())
    print(f'{size * size:.3f}')
elif shape == 'rectangle':
    size_a = float(input())
    size_b = float(input())
    print(f'{size_a * size_b:.3f}')
elif shape == 'circle':
    size = float(input())
    print(f'{3.14159265359 * (size * size):.3f}')
elif shape == 'triangle':
    size_a = float(input())
    size_b = float(input())
    print(f'{(1/2)* size_a * size_b:.3f}')