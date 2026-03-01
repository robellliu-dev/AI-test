cmake_minimum_required(VERSION 3.16)
project(cpp_sample LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(sample_lib src/math_utils.cpp)
target_include_directories(sample_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

add_executable(cpp_sample src/main.cpp)
target_link_libraries(cpp_sample PRIVATE sample_lib)

add_executable(cpp_sample_tests tests/test_math.cpp)
target_link_libraries(cpp_sample_tests PRIVATE sample_lib)

enable_testing()
add_test(NAME cpp_sample_tests COMMAND cpp_sample_tests)
