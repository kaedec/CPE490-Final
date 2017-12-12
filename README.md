# CPE490-Final

## Smart Sensor Network utilizing the BeagleBone Black

This project is a Internet of Things (IoT) system which is interested in two environmental factors: light level and temperature.  The central piece to this project is the single-board computer BeagleBone Black.  The BeagleBone collects data via attached hardware (sensors), performs required data processing, and allows that data to be accessible to devices on the same local network via Node-RED.  The network senses when the light level of its environment has decreased below a certain threshold (it is dark) and begins taking temperature data while in this state.

The folder *CppProject* contains all files (source, header, makefiles) relevant to the C++ program.

The folder *Python* contains the python data parser script and raw data.

The folder *LaTeX* contains materials relating to the written report (found in the root directory as **Final_Katelyn_Charbonneau.pdf**).

The folder *tmp36* contains reference material for the C++ program.

The file **report.txt** in the root directory is the system output file that is written by the Python script and read by Node-RED.  
**Note**: Node-RED is accessable by devices on the same network at *BeagleBoneIPv4Address*:1880.

See **Final_Katelyn_Charbonneau.pdf** for references and external links.
