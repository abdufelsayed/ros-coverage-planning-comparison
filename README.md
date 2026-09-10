# Coverage planning with ROS and Stage

This ROS 1 project compares three coverage planners on indoor maps in Stage. It
was built for the Intelligent Robotics module at the University of Birmingham
in 2021.

- **Zigzag** sweeps the map in alternating rows.
- **Spiral** chooses unvisited cells to the right, ahead, then left.
- **BSA** adds backtracking to the spiral strategy so the robot can return to
  unexplored branches.

Each planner uses odometry for motion control and laser scans for obstacle
detection. A separate ROS node records the robot's path for coverage and
distance measurements.

## Results

The coursework recorded one run for each planner on four maps.

| Planner | Mean coverage | Mean coverage per distance |
| --- | ---: | ---: |
| BSA | 65.9% | 0.00173 |
| Zigzag | 30.1% | 0.00172 |
| Spiral | 28.3% | 0.00209 |

BSA covered the largest area. Spiral recorded the most coverage per unit of
travel. The paths and workbook used for these figures are in
[`results/`](results/).

## Code

- [`src/planner/`](src/planner/) has the three planners and the shared robot
  controller.
- [`src/maps/`](src/maps/) has the Stage worlds, map images, and configuration
  files.
- [`src/metrics/record_path.py`](src/metrics/record_path.py) records
  ground-truth poses.
- [`scripts/coverage_stats.html`](scripts/coverage_stats.html) calculates path
  length and map coverage from a recorded run.
- [`report/`](report/) has the project proposal and interim report.

## Running the planners

The catkin package is named `ir_fp`. It requires ROS 1, Python 3, NumPy, and the
Pioneer and Stage packages referenced by the launch files.

Add the repository to a catkin workspace, build it, and source the workspace.
With Stage running, start one planner:

```bash
rosrun ir_fp zigzag.py
rosrun ir_fp spiral.py
rosrun ir_fp bsa.py
```

The planners read `/base_pose_ground_truth` and `/base_scan`. They publish
velocity commands to `/cmd_vel`.

## AI assistance

I used AI tools in 2026 to organise this repository, restructure the existing
code, and edit the documentation. My teammates and I completed the original
coursework in 2021 without AI assistance. Our original code, reports,
experiments, and recorded results are preserved in this repository or its Git
history.
