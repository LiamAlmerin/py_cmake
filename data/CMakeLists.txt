cmake_minimum_required (VERSION 3.20)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

set(PROJECT_NAME
	default_project
)

project(${PROJECT_NAME})

set(TARGET_NAME_0
	default_target
)
add_executable (${TARGET_NAME_0})

add_subdirectory(src)

set_property(TARGET ${TARGET_NAME_0} 
	PROPERTY CXX_STANDARD 20
)

set(BIN_DESTINATION 
	bin
)
set(LIB_DESTINATION 
	libs
)

install(TARGETS ${TARGET_NAME_0} 
	RUNTIME DESTINATION ${BIN_DESTINATION}  
	ARCHIVE DESTINATION ${LIB_DESTINATION}  
	LIBRARY DESTINATION ${LIB_DESTINATION}
)