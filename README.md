# Toy-car-simulation-using-ros

## ENPM662 Intro to Robot Modeling Project 1

|Team Members
|--
|Bharadwaj Chukkala

## Contents
1. Assembly
2. rat_bot

## Dependencies
- python 3.9 (works for any python 3 version)
- Python running IDE. (I used PyCharm IDE to program the Code and Execute the Code)
- Libraries: rospy, sys, select, termios, tty

## How to run the code
--> Create a catkin_ws and build it, then source it

--> Download the package

--> Paste the package in the source directory

--> Build and source the workspace

--> Commands to run (open separate terminals and run in the same order)
```bash
  roslaunch rat_bot rat_bot_launch.launch
```
```bash
  rosrun rat_bot publisher.py
```
```bash
  rosrun rat_bot subscriber.py
```
```bash
  rosrun rat_bot teleop_template.py
```

### Contact Author

Name : __Bharadwaj Chukkala__ <br>
Email : bchukkal@terpmail.umd.edu <br>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

