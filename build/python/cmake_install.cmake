# Install script for directory: /home/ece411c/pybombs/src/gr-uhdgps/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ece411c/pybombs")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/uhdgps" TYPE FILE FILES
    "/home/ece411c/pybombs/src/gr-uhdgps/python/gps_probe.py"
    "/home/ece411c/pybombs/src/gr-uhdgps/python/meta_to_json_file.py"
    "/home/ece411c/pybombs/src/gr-uhdgps/python/cpdu_average_power.py"
    "/home/ece411c/pybombs/src/gr-uhdgps/python/__init__.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/uhdgps" TYPE FILE FILES
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/gps_probe.pyc"
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/meta_to_json_file.pyc"
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/cpdu_average_power.pyc"
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/__init__.pyc"
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/gps_probe.pyo"
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/meta_to_json_file.pyo"
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/cpdu_average_power.pyo"
    "/home/ece411c/pybombs/src/gr-uhdgps/build/python/__init__.pyo"
    )
endif()

