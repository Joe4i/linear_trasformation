import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the vertices of the cube
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Define the edges of the cube
edges = [[0, 1], [1, 2], [2, 3], [3, 0],
         [4, 5], [5, 6], [6, 7], [7, 4],
         [0, 4], [1, 5], [2, 6], [3, 7]]

# Define the angle of rotation in radians
theta = np.pi / 4  # 45 degrees

# Define the shear transformation matrix
shear_matrix = np.array([[1, np.tan(theta / 2), 0],
                         [0, 1, 0],
                         [0, 0, 1]])

# Rotate the vertices of the cube using shear transformation
sheared_vertices = vertices @ shear_matrix.T  # Transpose the shear matrix

# Plot the original and sheared cube
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot original cube
for edge in edges:
    ax.plot3D(*zip(*vertices[edge]), color='b')

# Plot sheared cube
for edge in edges:
    ax.plot3D(*zip(*sheared_vertices[edge]), color='r')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Cube Shear Transformation')
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

def update(frame):
    ax.cla()  # Clear the previous plot
    # Calculate new shear transformation matrix for the current frame
    theta = frame
    shear_matrix = np.array([[1, np.tan(theta / 2), 0],
                             [0, 1, 0],
                             [0, 0, 1]])
    sheared_vertices = vertices @ shear_matrix.T
    for edge in edges:
        ax.plot3D(*zip(*vertices[edge]), color='b')  # Plot original cube
        ax.plot3D(*zip(*sheared_vertices[edge]), color='r')  # Plot sheared cube
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(f'3D Cube Shear Transformation (Frame {frame:.2f})')
    ax.set_box_aspect([1, 1, 1])

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, np.pi, 100),
                    blit=False, interval=50)
plt.show()
