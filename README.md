# CRISP Controllers Demos

<img src="https://github.com/user-attachments/assets/284983f8-2311-4699-86ab-06fc2ea9d5af" alt="CRISP Controllers Logo" width="160" align="right"/>

<a href="https://github.com/utiasDSL/crisp_controllers_demos/actions/workflows/docker_build.yml"><img src="https://github.com/utiasDSL/crisp_controllers_demos/actions/workflows/docker_build.yml/badge.svg"/></a>
<img alt="Static Badge" src="https://img.shields.io/badge/arxiv-cite-b31b1b?style=flat&link=google.com">
<a href="https://utiasDSL.github.io/crisp_controllers/"><img alt="Static Badge" src="https://img.shields.io/badge/docs-passing-blue?style=flat&link=https%3A%2F%2FutiasDSL.github.io%2Fcrisp_controllers%2F"></a>

This repo provides Docker containers to provide directly test the [crisp_controllers](https://github.com/utiasDSL/crisp_controllers) with real hardware or in simulation with a simple [MuJoCo](https://github.com/google-deepmind/mujoco) `ros2_control` interface provided in this repository.

Check the [docs](https://utiasdsl.github.io/crisp_controllers/misc/demos/) on how to get started with the demos and with CRISP in general.

## Dual-FR3 mounting

The dual-FR3 launch uses a level `world` frame halfway between the arm bases.
The left and right bases are at y=0.1065 m and y=-0.1065 m, with roll -0.7854
rad and 0.7854 rad, respectively. Cartesian `target_pose` values and published
`current_pose` values are expressed in `world`. The controllers do not transform
`PoseStamped` messages, so target pose headers should also use `frame_id: world`.
The mounted descriptions are published as `/left/robot_description` and
`/right/robot_description`.
