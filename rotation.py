import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

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

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original cube
for edge in edges:
    ax.plot3D(*zip(*vertices[edge]), color='b')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Cube Rotation')

# Define the angle of rotation in radians
theta = np.pi / 4  # 45 degrees


def update(frame):
    ax.cla()  # Clear the previous plot

    # Define the rotation matrix around the Z-axis for the current frame
    rotation_matrix = np.array([[np.cos(frame), -np.sin(frame), 0],
                                [np.sin(frame), np.cos(frame), 0],
                                [0, 0, 1]])
    # Rotate the vertices of the cube
    rotated_vertices = vertices @ rotation_matrix.T  # Transpose the rotation matrix

    # Plot the original cube
    for edge in edges:
        ax.plot3D(*zip(*vertices[edge]), color='b')

    # Plot the rotated cube
    for edge in edges:
        ax.plot3D(*zip(*rotated_vertices[edge]), color='r')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(f'3D Cube Rotation (Frame {frame:.2f})')


# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100),
                    blit=False, interval=50)

plt.show()
