# Use Euler method to solve an IVP of the form
# y' = g(x,y) and y(a) = b
# Input: g(x,y), a, b, step size h and number of steps n
# Output: y(a + nh)


def euler_approx(g, a, b, h, n):
    y_values = [b]
    for i in range(1, n + 1):
        new_y = y_values[i - 1] + h * g(a + (i-1) * h, y_values[i-1])
        y_values.append(new_y)
    return y_values


if __name__ == '__main__':
    user_function = input('Please enter the function g(x,y): ')
    g = lambda x, y: eval(user_function)
    a, b, h = [float(val) for val in input('Enter a, b, h: ').split(',')]
    n = int(input('Please enter n: '))
    print(f'Your IVP is y\' = {user_function}, y({a}) = {b}.')
    print(f'Euler approximation with {n} steps and step size {h}:')
    print('x', end=': ')
    for i in range(n+1):
        print(f'{a + i*h:6.3f}', end='   ')
    print('\ny', end=': ')
    for i in range(n + 1):
        print(f'{euler_approx(g, a, b, h, n)[i]:6.3f}', end='   ')
