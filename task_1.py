import pulp

# Створюємо LP проблему
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Оголошуємо змінні
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
y = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Функція цілі
model += x + y, "Total Production"

# Обмеження ресурсів
model += 2 * x + y <= 100, "Water Constraint"
model += x <= 50, "Sugar Constraint"
model += x <= 30, "LemonJuice Constraint"
model += 2 * y <= 40, "FruitPuree Constraint"

# Розв'язуємо модель
model.solve()

# Виводимо результати
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal number of Lemonade: {x.varValue}")
print(f"Optimal number of FruitJuice: {y.varValue}")
print(f"Total Production: {pulp.value(model.objective)}")
