cmake_minimum_required(VERSION 2.8)

set(TOP_LEVEL_PROJECT_NAME "${PROJECT_NAME}")

project(thryft CXX)

include_directories(
	include
	share/gtest-1.7.0/fused-src
)

if (MSVC)
else()
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-rtti")
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()

add_subdirectory(include)
if ("${TOP_LEVEL_PROJECT_NAME}" STREQUAL "")
	add_subdirectory(share)
	add_subdirectory(test)
endif()
