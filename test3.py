import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Load the head pose data (x, y, z, roll, pitch, yaw)
data = np.loadtxt("head_pose2.txt")

# Extract position and orientation
x, y, z = data[:, 0], data[:, 1], data[:, 2]
roll, pitch, yaw = np.radians(data[:, 3]), np.radians(data[:, 4]), np.radians(data[:, 5])  # Convert degrees to radians

# Create figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

for i in range(len(x)):
    ax.clear()  # Clear previous frame

    # Plot trajectory up to current frame
    ax.plot(x[:i+1], y[:i+1], z[:i+1], color="blue", linewidth=2, label="Head Pose Trajectory")

    # Compute direction unit vectors from yaw and pitch
    ux = np.cos(yaw[i]) * np.cos(pitch[i])
    uy = np.sin(yaw[i]) * np.cos(pitch[i])
    uz = np.sin(pitch[i])

    # Draw orientation arrow
    ax.quiver(x[i], y[i], z[i], ux, uy, uz, length=0.3, color="red")

    # Labels and settings
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.set_zlabel("Z Position")
    ax.set_title(f"3D Head Pose Visualization - Frame {i+1}/{len(x)}")
    ax.legend()
    ax.set_xlim([min(x), max(x)])
    ax.set_ylim([min(y), max(y)])
    ax.set_zlim([min(z), max(z)])

    plt.pause(0.1)  # Pause to create animation effect

plt.show()

