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

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

set(TARGET_NAME_0
	default_target
)
add_executable (${TARGET_NAME_0})
add_subdirectory(src)
set_property(TARGET ${TARGET_NAME_0} 
	PROPERTY CXX_STANDARD 20
)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

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

enable_testing()
add_executable(test)
add_subdirectory(test)
target_link_libraries(
  test
  GTest::gtest_main
)
include(GoogleTest)
gtest_discover_tests(hello_test)

