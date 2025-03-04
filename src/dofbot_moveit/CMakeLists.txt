

cmake_minimum_required(VERSION 3.0.2)
project(dofbot_moveit)

## Compile as C++11
add_compile_options(-std=c++11)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
    roscpp
    rosmsg
    rospy
    moveit_core
    moveit_msgs
    moveit_visual_tools
    moveit_ros_move_group
    moveit_ros_planning_interface
)

## Declare the package
catkin_package(
    INCLUDE_DIRS include
    LIBRARIES dofbot_kinematics
    CATKIN_DEPENDS roscpp rosmsg rospy moveit_core moveit_msgs moveit_visual_tools moveit_ros_planning_interface
)

## Include directories
include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)

## 🔹 Define the `dofbot_kinematics` library
#add_library(dofbot_kinematics src/dofbot_kinematics.cpp)
#target_link_libraries(dofbot_kinematics ${catkin_LIBRARIES})

## 🔹 Build Executables
#add_executable(dofbot_kinematics_fk src/dofbot_kinematics_fk.cpp)
#add_executable(dofbot_kinematics_ik src/dofbot_kinematics_ik.cpp)
#target_link_libraries(dofbot_kinematics_fk ${catkin_LIBRARIES} dofbot_kinematics)
#target_link_libraries(dofbot_kinematics_ik ${catkin_LIBRARIES} dofbot_kinematics)

#add_executable(01_random_move src/01_random_move.cpp)
#add_executable(02_motion_plan src/02_motion_plan.cpp)
#add_executable(03_attached_object src/03_attached_object.cpp)
#target_link_libraries(01_random_move ${catkin_LIBRARIES})
#target_link_libraries(02_motion_plan ${catkin_LIBRARIES})
#target_link_libraries(03_attached_object ${catkin_LIBRARIES})

## Install targets
#install(TARGETS dofbot_kinematics_fk dofbot_kinematics_ik 01_random_move 02_motion_plan 03_attached_object
 #   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)

#install(TARGETS dofbot_kinematics
 #   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  #  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   # RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
#)

install(DIRECTORY include/${PROJECT_NAME}/
    DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
    FILES_MATCHING PATTERN "*.h"
    PATTERN ".svn" EXCLUDE
)

## Unit Testing
#if (CATKIN_ENABLE_TESTING)
 #   catkin_add_gtest(${PROJECT_NAME}-test test/test_dofbot_moveit.cpp)
  #  if(TARGET ${PROJECT_NAME}-test)
   #     target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
    #endif()
#endif()
