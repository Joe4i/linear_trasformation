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

# Define the scaling factors
scale_x = 1.5
scale_y = 0.5
scale_z = 1.0

# Define the scaling transformation matrix
scaling_matrix = np.array([[scale_x, 0, 0],
                            [0, scale_y, 0],
                            [0, 0, scale_z]])

# Scale the vertices of the cube
scaled_vertices = vertices @ scaling_matrix.T  # Transpose the scaling matrix

# Plot the original and scaled cube
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot original cube
for edge in edges:
    ax.plot3D(*zip(*vertices[edge]), color='b')

# Plot scaled cube
for edge in edges:
    ax.plot3D(*zip(*scaled_vertices[edge]), color='r')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Cube Scaling Transformation')
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

def update(frame):
    ax.cla()  # Clear the previous plot
    # Calculate new scaling transformation matrix for the current frame
    scale_x = 1 + np.sin(frame) * 0.5  # Vary scale factor sinusoidally
    scaling_matrix = np.array([[scale_x, 0, 0],
                               [0, scale_y, 0],
                               [0, 0, scale_z]])
    scaled_vertices = vertices @ scaling_matrix.T
    for edge in edges:
        ax.plot3D(*zip(*vertices[edge]), color='b')  # Plot original cube
        ax.plot3D(*zip(*scaled_vertices[edge]), color='r')  # Plot scaled cube
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(f'3D Cube Scaling Transformation (Frame {frame:.2f})')
    ax.set_box_aspect([1, 1, 1])

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100),
                    blit=False, interval=50)
plt.show()
