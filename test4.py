import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the head pose data (x, y, z, roll, pitch, yaw)
data = np.loadtxt("head_pose2.txt")

# Extract position and orientation
x, y, z = data[:, 0], data[:, 1], data[:, 2]
roll, pitch, yaw = np.radians(data[:, 3]), np.radians(data[:, 4]), np.radians(data[:, 5])  # Convert degrees to radians

# Create a figure with two 3D subplots
fig = plt.figure(figsize=(12, 6))

# 1️⃣ 3D Trajectory Plot (Position)
ax1 = fig.add_subplot(121, projection="3d")
ax1.plot(x, y, z, color="blue", linewidth=2, label="Head Trajectory")
ax1.set_xlabel("X Position")
ax1.set_ylabel("Y Position")
ax1.set_zlabel("Z Position")
ax1.set_title("3D Head Position")
ax1.legend()

# 2️⃣ 3D Orientation Plot (Roll, Pitch, Yaw)
ax2 = fig.add_subplot(122, projection="3d")
ax2.plot(roll, pitch, yaw, color="red", linewidth=2, label="Orientation (Roll, Pitch, Yaw)")
ax2.set_xlabel("Roll")
ax2.set_ylabel("Pitch")
ax2.set_zlabel("Yaw")
ax2.set_title("3D Head Orientation")
ax2.legend()

plt.tight_layout()
plt.show()

