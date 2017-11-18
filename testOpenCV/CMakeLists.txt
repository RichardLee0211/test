cmake_minimum_required(VERSION 2.8)
OpenCV_INCLUDE_DIRS=
OpenCV_LIBS=
Image_Path=$PWD/testImage
project( DisplayImage )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( DisplayImage DisplayImage.cpp )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )
