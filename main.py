import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Step 1: Read the CSV file
data = pd.read_csv('frag0.csv')

# Extract x and y coordinates using the correct column names
x_points = data['4.194200134277343750e+01'].values
y_points = data['6.898000335693359375e+01'].values

# Step 2: Generate a parameter t for Bezier curve
t = np.linspace(0, 1, 100)

# Create a B-spline representation of the curve
spl_x = make_interp_spline(np.arange(len(x_points)), x_points, k=3)
spl_y = make_interp_spline(np.arange(len(y_points)), y_points, k=3)

# Generate new points
t_new = np.linspace(0, len(x_points) - 1, 100)
x_new = spl_x(t_new)
y_new = spl_y(t_new)

# Step 3: Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_new, y_new, label='Bezier Curve', color='blue')
plt.plot(x_points, y_points, 'ro', label='Data Points')  # Original data points
plt.legend()
plt.title('Bezier Curve through Given Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
