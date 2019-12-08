-->This package should be saved as hyper_car in a workspace.
    -->Contents:
        1)bag folder with recorded bag data
        2)rviz config file in rviz folder
        3)CMakelists.txt and package.xml
        4)car_model with the URDF of hyper_car 
        5)launch folder containing two launch files one for gazebo simulation and other for rviz visualization
        6)scripts containing hyper_car_test.py for performing the required operation

-->Run catkin_make and source ws

-->($roslaunch hyper_car  spawn_hyper_car.launch) for gazebo simulation of car starting from 0 m/s to 5 m/s and back to 0 m/s in roughly 6s
    -->After closing logs stored in ros log directory and also recorded in this-<time>-.bag
    -->To view run rqt_bag and view raw

-->roslaunch hyper_car hyper_car_rviz.launch to view model in rViz
