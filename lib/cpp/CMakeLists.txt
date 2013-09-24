cmake_minimum_required(VERSION 2.8)

project(thryft CXX)

file(GLOB INCLUDE_ "include/*.hpp")
file(GLOB INCLUDE_THRYFT "include/thryft/*.hpp")
file(GLOB INCLUDE_THRYFT_PROTOCOL "include/thryft/protocol/*.hpp")
source_group("Header Files\\" FILES ${INCLUDE_})
source_group("Header Files\\thryft\\" FILES ${INCLUDE_THRYFT_})
source_group("Header Files\\thryft\\protocol\\" FILES ${INCLUDE_THRYFT_PROTOCOL})
add_library(thryft
	${INCLUDE_}
	${INCLUDE_THRYFT}
	${INCLUDE_THRYFT_PROTOCOL}
)
set_target_properties(thryft PROPERTIES LINKER_LANGUAGE CXX)
