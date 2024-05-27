import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integration(f, a, b, num_points):
    x = np.random.uniform(a, b, num_points)
    y = f(x)
    integral = (b - a) * np.mean(y)
    return integral

# Параметри для методу Монте-Карло
num_points = 10000
mc_result = monte_carlo_integration(f, a, b, num_points)

# Аналітичне обчислення інтеграла
analytical_result = (b**3 / 3) - (a**3 / 3)

# Обчислення інтеграла за допомогою функції quad
quad_result, error = spi.quad(f, a, b)

# Виведення результатів
print(f"Метод Монте-Карло: {mc_result}")
print(f"Аналітичний результат: {analytical_result}")
print(f"Quad результат: {quad_result} (з похибкою {error})")

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
