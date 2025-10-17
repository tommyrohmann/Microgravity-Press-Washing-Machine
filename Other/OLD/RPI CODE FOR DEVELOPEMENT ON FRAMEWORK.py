"""
Microgravity Washing Machine Psudocode and Component Outline
Tommy Rohmann, 07/09/2024
"""

"""
Component Checklist
Required Sensors
1) Reservoir Pressure, P_Res
2) Wash Chamber Pressure, P_Cha
3) Load Cell 1, LC_Cha_1
4) Load Cell 2, LC_Cha 2
5) Load Cell 3, LC_Res_1
6) Load Cell 4, LC_Res_1
7) Valve Actuator Current Sensor, CS_VV
8) Washing Machine Current Sensor, CS_WS
9) Emergency Stop, E_Stop
10) Wash Rotary Encoder, RE_Wash
11) Reservior Rotary Encoder, RE_Res


Derived Data for Logging
1) Load Cell Force Sum Wash Chamber, LC_Wash_Sum
2) Load Cell Force Sum Reservior, LC_Res_Sum
3) Load Cell Force Differential Chamber, LC_Wash_Dif
4) Load Cell Force Differential Reservoir, LC_Res_Dif
5) Elapsed Time, ET

Required Actuators
1) Washwater Inlet Valve Actuator, VA_WW_I
2) Washwater Outlet Valve Actuator, VA_WW_O
3) Cross-over Valve Actuator, VA_XO
4) Air Valve Actuator, VA_A
5) Chamber Piston Drive Motor, DM_Cha
6) Reservoir Piston Drive Motor, DM_Res

RPI TX List Format
	[Actuator States, [endpoints list]]
	endpoint condition format: [(1),(2),(3)]
	(1): Int Indicating which sensor is being read
	(2): Bool/bit, True means endpoint condition met if value is greater than set value, if false than less than
	(3): Int, Set point sensor is checked against

	Conditions in the given list are formatted as such
	[
		[
			[Condition 1]
		]
		[
			[Condition 2], [Condition 3]
		]
	]

	this statement indicates that if Condition 1 is met, or if Condition 2 and 3 are met simutaniously, the wash phase is ended

	Examples
	[[[1,1,20]],[[2,0,40]]] - if 1 is greater than 20, or 2 is less than 40
	[[[1,0,20],[3,1,500]],[[1,1,40]]] - if 1 is less than 20 while 3 is greater than 500, or 1 is greater than 40

RPI RX List Format
[State Progress, Endpoint , Sensor Values]
	State Progress States:
		0: Process in Progress
		1: Process 
		
RPI File Structure
Save Folder: Saves Machine running hours, Current Wash Process Count for Datalogger, List of wash process files (Pre, Wash, and Post),

Initial Startup
	1) Initial variable definitions and file path settings
	2) Read Save Folder
		Current Wash Number
	
UI Loop
	Select Wash Process
		
	Run Wash Process
	
	Edit Wash Process/Make New Wash Process
	
	Troubleshoot Mode
	
Control Loop
	1) Create File for Data Logger
	2) Read selected wash process, preprocess, and postprocess files for instructions, commit to corrosponding lists
	3) Process Select Loop
		1) Initiates Process loop with corrosponding file selected for preprocess, wash process, or postprocess
		2) if at the end of process select loop, control loop completed
		3) Process Loop
			1) Selects first or next control state of selected process folder (Preprocess, Process, or Postprocess)
			2) If at end of process, proceed from beginning of process select loop
			3) Read Loop
					1) Read current Serial Bus Output from ESP32
					2) Write Serial Output to Data Log File
					3) Evaluate if control or safety endpoint is met
						If ctrl endpoint met restart process loop
						If safety endpoint met, stop and display error summary

Postwash
	Close Datalogger
	Find time elapsed during wash process, add to runtime
	Increment Wash Process Count by 1 for data logger
	Return to UI Loop
    

ESP Code
TX
	
RX
    
"""