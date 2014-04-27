cmake_minimum_required(VERSION 2.8)

project(thryft CXX)

include_directories(
	include
	share/gtest-1.6.0/fused-src
)

if (MSVC)
else()
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-rtti")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()

add_subdirectory(include)
add_subdirectory(share)
add_subdirectory(test)
