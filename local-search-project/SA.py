import numpy as np

def objective(x, y):
    value = 3*(1-x)**2*np.exp(-x**2 - (y+1)**2) - 10*(x/5 - x**3 - y**5)*np.exp(-x**2 - y**2) -1/3*np.exp(-(x+1)**2 - y**2)
    return value

def rastrigin(x, y):
    value = 2 + (x**2 - (np.cos(2 * x * np.pi))) + (y**2 - (np.cos(2 * y * np.pi)))
    return value


def simulated_annealing(func, bounds, max_iter, initial_temp, cooling_rate):
    x = np.random.uniform(bounds[0][0], bounds[0][1])
    y = np.random.uniform(bounds[1][0], bounds[1][1])
    current = func(x, y)
    best = current
    best_coords = (x, y)
    temp = initial_temp

    for i in range(max_iter):
        new_x = np.clip(x + np.random.normal(), bounds[0][0], bounds[0][1])
        new_y = np.clip(y + np.random.normal(), bounds[1][0], bounds[1][1])
        new = func(new_x, new_y)

        delta = new - current
        if delta > 0 or np.random.rand() < np.exp(delta / temp):
            x, y = new_x, new_y
            current = new

        if current > best:
            best = current
            best_coords = (x, y)

        temp *= (1 - cooling_rate)


    return best_coords, best


bounds_objective = [(-3, 3), (-3, 3)]
bounds_rastrigin = [(-1.5, 1.5), (-1.5, 1.5)]
max_iter = 100000
initial_temp = 100
cooling_rate = 0.003

max_coords_objective, max_value_objective = simulated_annealing(objective, bounds_objective, max_iter, initial_temp, cooling_rate)
min_coords_objective, neg_min_value_objective = simulated_annealing(lambda x, y: -objective(x, y), bounds_objective, max_iter, initial_temp, cooling_rate)
min_value_objective = -neg_min_value_objective

min_coords_rastrigin, min_value_rastrigin = simulated_annealing(lambda x, y: -rastrigin(x, y), bounds_rastrigin, max_iter, initial_temp, cooling_rate)

print("Objective function")
print(f"Global Minimum:\nCoordinates: {float(max_coords_objective[0]):.6f}, {float(max_coords_objective[1]):.6f}, Value: {min_value_objective}")
print(f"Global Maximum:\nCoordinates: {float(max_coords_objective[0]):.6f}, {float(max_coords_objective[1]):.6f}, Value: {max_value_objective}")
print("-------------------------------------------------------------")
print("Rastrigin Function")
print(f"Global Minumum :\nCoordinates: {float(min_coords_rastrigin[0]):.6f}, {float(min_coords_rastrigin[1]):.6f}, Value: {min_value_rastrigin}")


#---------------------------- RESULTS ----------------------------#
# Objective function
# Global Minimum:
# Coordinates: -0.010423, 1.585069, Value: -6.5504069504519284
# Global Maximum:
# Coordinates: -0.010423, 1.585069, Value: 8.105979765597635
# -------------------------------------------------------------
# Rastrigin Function
# Global Minumum :
# Coordinates: 0.002819, -0.004284, Value: -0.000545336905528826