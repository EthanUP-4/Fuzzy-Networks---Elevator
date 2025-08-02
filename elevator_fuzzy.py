import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def elevatorfuzzy_sys():
    W = ctrl.Antecedent(np.arange(0, 501, 1), "Weight")
    S = ctrl.Antecedent(np.arange(0, 6, 1), "Speed")
    P = ctrl.Antecedent(np.arange(0, 51, 1), "Position")
    A = ctrl.Consequent(np.arange(-8, 1, 1), "Acceleration")

    # Singleton outputs
    A['-1'] = fuzz.trimf(A.universe, [-1, -1, -1])
    A['-2'] = fuzz.trimf(A.universe, [-2, -2, -2])
    A['-3'] = fuzz.trimf(A.universe, [-3, -3, -3])
    A['-4'] = fuzz.trimf(A.universe, [-4, -4, -4])
    A['-5'] = fuzz.trimf(A.universe, [-5, -5, -5])
    A['-6'] = fuzz.trimf(A.universe, [-6, -6, -6])
    A['-7'] = fuzz.trimf(A.universe, [-7, -7, -7])

    W['Low'] = fuzz.trapmf(W.universe, [0, 0, 100, 150])
    W['Med'] = fuzz.trapmf(W.universe, [100, 150, 250, 350])
    W['High'] = fuzz.trapmf(W.universe, [250, 350, 500, 500])

    S['Low'] = fuzz.trapmf(S.universe, [0, 0, 1.5, 2])
    S['Med'] = fuzz.trapmf(S.universe, [1.5, 2, 3.5, 4.5])
    S['High'] = fuzz.trapmf(S.universe, [3.5, 4.5, 5, 5])

    P['Close'] = fuzz.trapmf(P.universe, [0, 0, 12, 20])
    P['Med'] = fuzz.trapmf(P.universe, [12, 20, 28, 35])
    P['Far'] = fuzz.trapmf(P.universe, [28, 35, 50, 50])

    # Rules
    rules = [
        ctrl.Rule(W['Low'] & S['Low'] & P['Close'], A['-3']),
        ctrl.Rule(W['Low'] & S['Low'] & P['Med'], A['-2']),
        ctrl.Rule(W['Low'] & S['Low'] & P['Far'], A['-1']),
        ctrl.Rule(W['Low'] & S['Med'] & P['Close'], A['-4']),
        ctrl.Rule(W['Low'] & S['Med'] & P['Med'], A['-3']),
        ctrl.Rule(W['Low'] & S['Med'] & P['Far'], A['-2']),
        ctrl.Rule(W['Low'] & S['High'] & P['Close'], A['-5']),
        ctrl.Rule(W['Low'] & S['High'] & P['Med'], A['-4']),
        ctrl.Rule(W['Low'] & S['High'] & P['Far'], A['-3']),
    
        ctrl.Rule(W['Med'] & S['Low'] & P['Close'], A['-4']),
        ctrl.Rule(W['Med'] & S['Low'] & P['Med'], A['-3']),
        ctrl.Rule(W['Med'] & S['Low'] & P['Far'], A['-2']),
        ctrl.Rule(W['Med'] & S['Med'] & P['Close'], A['-5']),
        ctrl.Rule(W['Med'] & S['Med'] & P['Med'], A['-4']),
        ctrl.Rule(W['Med'] & S['Med'] & P['Far'], A['-3']),
        ctrl.Rule(W['Med'] & S['High'] & P['Close'], A['-6']),
        ctrl.Rule(W['Med'] & S['High'] & P['Med'], A['-5']),
        ctrl.Rule(W['Med'] & S['High'] & P['Far'], A['-4']),
        
        ctrl.Rule(W['High'] & S['Low'] & P['Close'], A['-5']),
        ctrl.Rule(W['High'] & S['Low'] & P['Med'], A['-4']),
        ctrl.Rule(W['High'] & S['Low'] & P['Far'], A['-3']),
        ctrl.Rule(W['High'] & S['Med'] & P['Close'], A['-6']),
        ctrl.Rule(W['High'] & S['Med'] & P['Med'], A['-5']),
        ctrl.Rule(W['High'] & S['Med'] & P['Far'], A['-4']),
        ctrl.Rule(W['High'] & S['High'] & P['Close'], A['-7']),
        ctrl.Rule(W['High'] & S['High'] & P['Med'], A['-6']),
        ctrl.Rule(W['High'] & S['High'] & P['Far'], A['-5'])
    ]

    system = ctrl.ControlSystem(rules)
    return system

def evaluate_acceleration(sim, weight, speed, position):
    sim.input['Weight'] = weight
    sim.input['Speed'] = speed
    sim.input['Position'] = position
    sim.compute()
    return sim.output['Acceleration']

weight = int(input("Enter Constant Weight (0-500): "))
while not (0 <= weight <= 500):
    weight = int(input("Re-Enter Constant Weight: "))

datapoints = int(input("Enter number of data points: "))

system = elevatorfuzzy_sys()   


speed_array = np.linspace(0, 5, datapoints)
position_array = np.linspace(0, 50, datapoints)
X, Y = np.meshgrid(speed_array, position_array)
Z = np.zeros_like(X)

sim = ctrl.ControlSystemSimulation(system)

# Compute acceleration grid
print("Evaluating fuzzy system...")
for i in range(datapoints):
    for j in range(datapoints):
        Z[i, j] = evaluate_acceleration(sim, weight, X[i, j], Y[i, j])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Set z-axis to show only integer values from -5 to 0
ax.set_zlim(-5, 0)
ax.set_zticks(np.arange(-5, 1, 1))  # Only show integer ticks from -5 to 0

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Speed')
ax.set_ylabel('Position')
ax.set_zlabel('Acceleration')
ax.set_title('Fuzzy System Acceleration Surface')
plt.show()
