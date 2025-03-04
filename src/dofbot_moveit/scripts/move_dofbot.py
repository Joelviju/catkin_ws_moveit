#!/usr/bin/env python3
import rospy
import math
import moveit_commander

# Initialize MoveIt and ROS node
rospy.init_node('dofbot_motion_controller')
moveit_commander.roscpp_initialize([])

# Create MoveIt group for planning (for "robot1")
group = moveit_commander.MoveGroupCommander("robot1")

# Define target joint angles in DEGREES
TARGET_JOINT_ANGLES_DEG = [ -12, -78, 0, 3]

# Convert to RADIANS
TARGET_JOINT_ANGLES = [math.radians(angle) for angle in TARGET_JOINT_ANGLES_DEG]

def move_robot():
    rospy.loginfo("Moving DOFBOT to Target Position")

    # Set target joint positions
    group.set_joint_value_target(TARGET_JOINT_ANGLES)

    # Plan and execute the motion
    success, plan, _, _ = group.plan()
    if success:
        group.execute(plan, wait=True)
        rospy.loginfo("DOFBOT has reached the target position.")
    else:
        rospy.logwarn("Motion planning failed!")

if __name__ == "__main__":
    move_robot()
