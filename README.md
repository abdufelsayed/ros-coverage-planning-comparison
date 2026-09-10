# Coverage planning in ROS Stage

Group 11 coursework for Intelligent Robotics at the University of Birmingham, 2021. The project compares zigzag, spiral, and backtracking coverage on four simulated maps.

## Code

This repository contains the coursework ROS package, `ir_fp`:

- [Planners](src/planner/): the final zigzag, spiral, and BSA/backtracking implementations.
- [Robot controller](src/planner/robot_controller.py): motion commands, odometry feedback, and laser obstacle detection.
- [Maps](src/maps/): Stage worlds, map images, and map configuration files.
- [Path recorder](src/metrics/record_path.py) and [recording controls](scripts/).
- [Coverage analysis](scripts/coverage_stats.html): the browser tool used to analyse recorded paths.

The implementation comes from the [group repository](https://github.com/MilesCourtie/ir_fp/tree/1c95066). Its commit history retains the group's contributions. The shared heading enum is extracted into [direction.py](src/planner/direction.py); planner decisions, state, parameters, and controller behavior are preserved. [Exploratory scripts](experiments/) are separate from the final planners.

## Execution flow

Each planner calls the shared robot controller, which reads simulator feedback and publishes velocity commands. The separate path recorder saves ground-truth poses. The browser analysis tool calculates measurements from those recordings and map images; the workbook contains the reported results.

Abdullah implemented the initial controller and obstacle checks and helped integrate the planners. Teammates subsequently revised the controller and planning algorithms.

The moved experimental scripts still use `robot_controller`; to inspect them in the coursework environment, include `src/planner` on `PYTHONPATH`. They are not the entry points for the reported comparison.

## Results and project documents

[Recorded paths and the results workbook](results/) contain the measurements from the coursework. There is one primary recording for each planner-map combination, plus a second saved map5 spiral recording. The workbook labels the maps 1–4; the corresponding filenames use map2–map5.

Across the four reported runs, BSA averaged 65.9% coverage. Spiral had the highest mean coverage per reported travel distance. These are historical measurements, not results from a new simulator run.

The available project documents are the [proposal](report/Group%2011%20Project%20Proposal.docx) and [interim document](report/Group%2011%20Interim%20Report.docx). A submitted final report was not recovered. The proposal describes the earlier litter-collection idea; the implemented work here concerns coverage planning.

## Running the code

The package uses ROS 1, catkin, Python 3, NumPy, and ROS message packages. The recording scripts reference ROS Noetic. The launch files also reference the coursework's Pioneer robot packages.

Place the repository in a catkin workspace as the `ir_fp` package, build the workspace, and source its setup file. The planner entry points are `src/planner/zigzag.py`, `spiral.py`, and `bsa.py`. They expect a running simulator publishing `/base_pose_ground_truth` and `/base_scan`, and accept motion through `/cmd_vel`.

The complete coursework environment is not bundled, and these instructions have not been validated in a fresh ROS installation. The scripts retain their coursework configuration and behavior.

To inspect the recorded results without ROS, open the workbook or the CSV files. Open `scripts/coverage_stats.html` in a browser to inspect the analysis tool.

## Attribution

This was group coursework by Miles Courtie, Abdullah Elsayed, Isaac Orr, and Stephen Holmes. The Git history records individual code contributions. The package manifest retains its original license declaration.
