cmake_minimum_required(VERSION 3.13)
project(NMPC_MPI)

set(CMAKE_CXX_STANDARD 11)

add_executable(NMPC_MPI
        mc_walks.cpp)
