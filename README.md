# Elevator Fuzzy Logic System

Welcome to the **Elevator Fuzzy Logic System**! 🚀

This project models the acceleration behavior of an elevator using fuzzy logic. Instead of rigid rules, it uses *fuzzy* concepts like “Low Weight” or “High Speed” to make smooth, human-like decisions for elevator acceleration based on the current weight, speed, and position.

---

## What’s Inside?

- A fuzzy logic controller that takes three inputs:
  - **Weight** (0 to 500 units)
  - **Speed** (0 to 5 units)
  - **Position** (0 to 50 units)
- Outputs an **acceleration** value (ranging roughly from -7 to -1) to control the elevator's movement smoothly.
- Uses the **Takagi-Sugeno fuzzy inference system** with intuitive rules.
- Generates a 3D surface plot showing how acceleration changes with speed and position for a fixed weight.

---

## Why Fuzzy Logic?

Elevators don’t move in strict yes/no patterns. Real-world scenarios have uncertainties and gradual transitions. Fuzzy logic captures this by handling vague concepts (like “Medium Speed”) and outputs smooth control signals, making the elevator ride safer and more comfortable.

---

## How To Use

1. **Clone the repo** and install dependencies:
   ```bash
   pip install numpy scikit-fuzzy matplotlib tqdm

Run the script:
python elevator_fuzzy.py

Enter the constant weight of the elevator load when prompted (between 0 and 500).
Enter the number of data points to define resolution for the surface plot.
Watch the program evaluate acceleration across speed and position ranges and display a 3D plot.

What You’ll See:
A colorful 3D surface showing acceleration based on speed and position.
Acceleration decreases (more negative) with higher weights and speeds, mimicking real elevator dynamics.

Code Highlights
Fuzzy sets defined using trapezoidal membership functions (e.g., Low, Medium, High for weight).
Singleton membership functions for outputs (specific acceleration values).
Intuitive rules combining inputs to determine output acceleration.

Efficient system setup: fuzzy system is built once, then used repeatedly for evaluation.
User input validation to ensure realistic data.
Visualized with Matplotlib’s 3D plotting.

Feel free to...
Experiment with different rules or membership functions.
Integrate this fuzzy controller into a bigger elevator simulation.
Use it as a learning resource for fuzzy logic concepts.

If you have questions or suggestions, just ask! Happy fuzzing! 🌀
