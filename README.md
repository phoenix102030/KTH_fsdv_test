# KTH_fsdv_test
The entry tests for the KTH Formula DV group
## The training exercises for recruitment
This Git repository contains a set of ROS (Robot Operating System) packages designed for various exercises. Follow the instructions below to set up and run these packages.

## Downloading Instructions

1. Clone this repository inside the `src` folder of your Catkin workspace (`catkin_ws`):

    ```bash
    git clone <repository_url> catkin_ws/src
    ```

2. Navigate to your Catkin workspace:

    ```bash
    cd catkin_ws
    ```

3. Rebuild the Catkin workspace to resolve dependencies:

    ```bash
    catkin build
    ```

## Running the Files

### Exercise 1 (ROS Required)

- Source the environment:

    ```bash
    source devel/setup.bash
    ```

- Open three terminals (Ubuntu 18.04, ROS Melodic):

    - **Terminal 1:** Run ROS core

        ```bash
        roscore
        ```

    - **Terminal 2:** Run the publisher node

        ```bash
        rosrun publisher exec1_pub.py
        ```

    - **Terminal 3:** Run the subscriber node

        ```bash
        rosrun subscriber exec1_sub.py
        ```

### Exercise 2 (No ROS Required)

- Navigate to the `kthfsdv-plotting` folder:

    ```bash
    cd kthfsdv-plotting
    ```

- Run the Python script:

    ```bash
    python Visualisation.py
    ```

## Additional Information

Make sure to follow these instructions in the specified order to ensure a smooth setup and execution of the exercises.

For any issues or questions, refer to the package documentation and the `README` files within each package.

**Note:** Exercise 2 does not require ROS and is included for convenience.
