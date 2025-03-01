import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

history = np.array(history)

x_min, x_max = np.min(history[:, :, 0]), np.max(history[:, :, 0])
y_min, y_max = np.min(history[:, :, 1]), np.max(history[:, :, 1])

X = np.linspace(x_min, x_max, 50)
Y = np.linspace(y_min, y_max, 50)
X, Y = np.meshgrid(X, Y)

Z = np.array([[profit_function(np.array([x, y])) for x, y in zip(X_row, Y_row)] for X_row, Y_row in zip(X, Y)])

particle_profits = np.array([[profit_function(p) for p in history[:, i]] for i in range(len(history[0]))])
best_index = np.argmax([profit_function(p) for p in history[-1]])
best_x, best_y = history[-1, best_index]
best_z = profit_function([best_x, best_y])

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='k', zorder=1)

for i in range(len(history[0])):
    ax.plot(history[:, i, 0], history[:, i, 1], particle_profits[i], 
            marker='o', linestyle='-', color='red', alpha=0.8, zorder=2)

ax.scatter(best_x, best_y, best_z, 
           color='gold', s=1000, edgecolors='black', linewidth=3, marker='*', 
           label="Best Solution", zorder=20)

ax.plot([best_x, best_x], [best_y, best_y], [0, best_z], linestyle="dashed", color="black", linewidth=2, zorder=5)

text_x = x_max - 20 
text_y = y_max - 15 
text_z = np.max(Z) + 5

ax.text(text_x, text_y, text_z,  
        f"Best Solution:\n({best_x:.2f}, {best_y:.2f}, {best_z:.2f})",  
        color='black', fontsize=10, fontweight='bold',
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='black', boxstyle="round,pad=0.4"),
        zorder=10)

# Labels
ax.set_xlabel("μ1", fontsize=12, fontweight='bold')
ax.set_ylabel("μ2", fontsize=12, fontweight='bold')
ax.set_zlabel("Profit (per unit time)", fontsize=12, fontweight='bold', labelpad=0)
ax.set_title("PSO Optimization Process with Contour Surface", fontsize=12, fontweight='bold')

fig.canvas.draw()

ax.grid(True, linestyle='--', linewidth=0.5)

ax.legend()
plt.show()