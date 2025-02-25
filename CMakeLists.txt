cmake_minimum_required(VERSION 3.10)
project(CoinRowProject C)

set(CMAKE_C_STANDARD 11)

# Define source file paths with proper quoting
set(COIN_ROW_SOURCE "${CMAKE_CURRENT_SOURCE_DIR}/Design and Analysis of Algorithms/CoinRowProblem.c")
set(QUEUE_SOURCE "${CMAKE_CURRENT_SOURCE_DIR}/Design and Analysis of Algorithms/queue.c")

# Include all source files
add_executable(CoinRowProblem
        "${COIN_ROW_SOURCE}"
        "${QUEUE_SOURCE}"
)