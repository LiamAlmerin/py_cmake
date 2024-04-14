
project(${PROJECT_NAME})

set(TARGET_SRCS
	main.cpp
#	END_TARGET_SRCS
)

# Add source to this project's executable.
add_executable (${TARGET_NAME} 
	${TARGET_SRCS}
)
