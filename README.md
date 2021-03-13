# post107mb.f90

post107mb.f90 Development Cycle [v.1.0.0]
---------------------

 1) Required Files
 2) How to run?
 3) Technical Feasibility / Prototype
 4) Design / Development 
 5) Configuration
 6) Troubleshooting / Testing
 7) Deployment
 8) Remarks

VERSION CONTROL PERMISSION
---------------------
 * The top-level administration categories require permission to be
   accessible. Permission for merging is only given to the owner of the repository.

INTRODUCTION
------------

post107mb.f90 is a postprocessing code written in Fortran to allow for generating the Wing Surfaces by extracting the data points from the output files of Syn3d.

 * For a full description of the code, please visit the Syn3d repository.

 * To submit bug reports and feature suggestions, or track changes, please reach out to kit71717 on Github or to https://www.linkedin.com/in/calvin-li-69b360123/

REQUIRED FILES
------------

	- Core files: (Required for ANY run)
		1) Makefile – This runs the fortran code and also, executes the “a.out” file.
		2) post107mb.f90 – This runs the postprocessing of the two flo.case1.##.dat (initial and final design case)
		3) Result_Out.py – This runs the macro in ParaView
   
   	- Input files: (Required for specific run)
		1) flo.case1.##.dat – design iteration input data files
		2) MBL1.CONN – connection file for each test case (used for extracting “-7”)
		3) output – output of the design iteration (used for extracting “RHO0, P0, U0, V0”)

		
   - Version Number (With trademark at the bottom of app)
   		- Copyright © 2021 Chun Kit Calvn Li. All rights reserved. v.1.0.0

HOW TO RUN?
------------

	1) Copy Makefile and post107mb.f90 to the test directory.
		- REMARK: Make sure the input files (referred in previous section) are all present
	2) Run the following command: “make check”
	3) Two files should be created in the current directory in the format of: Wing_Analysis_1.##.dat
	4) Open ParaView
	5) In the Menu Bar, click Macro -> Add new macro -> select “Result_Out.py”
		- REMARK: “Result_Out.py” can be located anywhere on your local machine
	6) In the Menu Bar, click File -> Open -> select “Wing_Analysis_1.##.dat”
		- REMARK: Import the two Wing_Analysis_1.##.dat files from test directory
	7) In the Menu Bar, click Macro -> click Result_Out.py
	8) In the first window that pops up, input number of cross sections desired
	9) In the subsequent windows that pops up, input the % - span location
		- REMARK: There should be as many subsequent popup windows as the inputted
cross section number
	10) Wait for Macro to run and obtain the desired Outputs.

TECHNICAL FEASIBILITY / PROTOTYPE
------------

DESIGN / DEVELOPMENT
------------

CONFIGURATION
------------

TROUBLESHOOTING / TESTING
------------

DEPLOYMENT 
------------

REMARKS
------------


