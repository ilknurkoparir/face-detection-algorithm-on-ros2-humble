# STEP 1 : Create Workspace and Package
# Create Workspace
```bash
$ source /opt/ros/humble/setup.bash
$ mkdir ros2_opencv 
$ ls
$ cd ros2_opencv
$ mkdir src
$ cd ..
$ colcon build

```
# Create Package
```bash
$ ros2 pkg create --build-type ament_python my_package my_node --dependencies rclpy image_transport cv_bridge sensor_msgs std_msgs opencv2
$ cd ros2_opencv
$ colcon build
$ source install/local_setup.bash
$ ros2 run my_package my_node

```
# STEP 2 : Create the Python script for Publisher and Subscriber
Open terminal and copy this command
```bash
$ wget https://raw.githubusercontent.com/ros2/examples/humble/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py

```
Move to the Setup.py
```python
 entry_points={
        'console_scripts': [
            'my_node = my_package.my_node:main',
            'alici = my_package.alici:main'

        ],
        
    },


```
Run Publisher and Subscriber
```bash
$ ros2 run my_package my_node #publisher
$ ros2 run my_package alici #subscriber


```
# STEP 3 : Results

![1](https://github.com/ilknurkoparir/face-detection-algorithm-on-ros2-humble/assets/129418387/7a60245c-c9fd-4fa5-9918-ee65eb487bae)








