cmake_minimum_required(VERSION 2.8)

project(thryft CXX)

file(GLOB INCLUDE_THRYFT_PROTOCOL "include/thryft/protocol/*.hpp")
source_group("Header Files\\thryft\\protocol\\" FILES ${INCLUDE_THRYFT_PROTOCOL})
add_library(thryft ${INCLUDE_THRYFT_PROTOCOL})
set_target_properties(thryft PROPERTIES LINKER_LANGUAGE CXX)
