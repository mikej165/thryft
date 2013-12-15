@ECHO OFF
astyle --options=%~dp0astylerc --recursive %* "%~dp0..\include\*.hpp" "%~dp0..\test\*.cpp" "%~dp0..\test\*.hpp"