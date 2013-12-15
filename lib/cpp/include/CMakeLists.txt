file(GLOB INCLUDE_ "${CMAKE_SOURCE_DIR}/include/*.hpp")
file(GLOB INCLUDE_THRYFT "${CMAKE_SOURCE_DIR}/include/thryft/*.hpp")
file(GLOB INCLUDE_THRYFT_PROTOCOL "${CMAKE_SOURCE_DIR}/include/thryft/protocol/*.hpp")
source_group("Header Files\\" FILES ${INCLUDE_})
source_group("Header Files\\thryft\\" FILES ${INCLUDE_THRYFT_})
source_group("Header Files\\thryft\\protocol\\" FILES ${INCLUDE_THRYFT_PROTOCOL})
add_library(thryft
	${INCLUDE_}
	${INCLUDE_THRYFT}
	${INCLUDE_THRYFT_PROTOCOL}
)
set_target_properties(thryft PROPERTIES LINKER_LANGUAGE CXX)
