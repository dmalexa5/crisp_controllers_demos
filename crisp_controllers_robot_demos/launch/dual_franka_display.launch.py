import os

import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace

fr3_config_dir = os.path.join(
    get_package_share_directory("crisp_controllers_robot_demos"),
    "config",
    "fr3",
)


def arm_group(arm_prefix, mounting):
    """Publish one mounted arm description and drive its joints with sliders."""
    robot_description = xacro.process_file(
        os.path.join(fr3_config_dir, "fr3_single.urdf.xacro"),
        mappings={
            "arm_prefix": arm_prefix,
            "mounting": mounting,
            "use_fake_hardware": "true",
        },
    ).toprettyxml(indent="  ")

    return GroupAction([
        PushRosNamespace(arm_prefix),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[{"robot_description": robot_description}],
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui",
        ),
    ])


def generate_launch_description():
    use_rviz = LaunchConfiguration("use_rviz")

    rviz_file = os.path.join(fr3_config_dir, "dual_fr3.rviz")

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["--display-config", rviz_file],
        condition=IfCondition(use_rviz),
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_rviz",
            default_value="true",
            description="Visualize the robots in Rviz",
        ),
        arm_group("left", "dual_left"),
        arm_group("right", "dual_right"),
        rviz_node,
    ])
