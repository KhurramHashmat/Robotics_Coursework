from controller import Robot
from controller import Camera
from controller import CameraRecognitionObject
TIME_STEP = 64

# create the Robot instance.
robot = Robot()

# initialize distance sensors
dsNames = ['dist_sensor_right', 'dist_sensor_left']
ds = []
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)

# initialize camera
camera = robot.getDevice("CAM")
camera.enable(TIME_STEP)
camera.recognitionEnable(TIME_STEP)

# initialize motors
wheels = []
wheelsNames = ['wheel0', 'wheel1', 'wheel2', 'wheel3']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

Obstacle_Counter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = 5.0
    rightSpeed = 5.0
    if Obstacle_Counter > 0:
        Obstacle_Counter -= 1
        leftSpeed = 1.0
        rightSpeed = -1.0
    else:  # read sensors
        for i in range(2):
            if ds[i].getValue() < 950.0:
                Obstacle_Counter = 100
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)