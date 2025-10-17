"""
Microgravity Washing Machine Psudocode and Component Outline
Tommy Rohmann, 07/09/2024
"""

"""
Component Checklist
###Required Sensors
-Reservoir Pressure, P_Res
- Wash Chamber Pressure, P_Cha
- Load Cell 1, LC_Cha_1
- Load Cell 2, LC_Cha 2
- Load Cell 3, LC_Res_1
- Load Cell 4, LC_Res_1
- Valve Actuator Current Sensor, CS_VV
- Washing Machine Current Sensor, CS_WS
- Emergency Stop, E_Stop
- Absolute Rotary Encoder 1, ARE_Cha_1
- Absolute Rotary Encoder 2, ARE_Cha_2
- Absolute Rotary Encoder 3, ARE_Res_1
- Absolute Rotary Encoder 4, ARE_Res_2

Derived Data for Logging
- Load Cell Force Sum Wash Chamber, LC_Cha_Sum
- Load Cell Force Sum Reservior, LC_Res_Sum
- Load Cell Force Differential Chamber, LC_Cha_Dif
- Load Cell Force Differential Reservoir, LC_Res_Dif
- Elapsed Time, ET

Required Actuators
- Washwater Inlet Valve Actuator, VA_WW_I
- Washwater Outlet Valve Actuator, VA_WW_O
- Cross-over Valve Actuator, VA_XO
- Air Valve Actuator, VA_A
- Chamber Piston Drive Motor, DM_Cha
- Reservoir Piston Drive Motor, DM_Res

RPI TX List Format
[Actuator States, [end condition list]]
end condition list format:
 [[1],[2],[3]] condition 1, 2, or 3 will trigger endpoint
	contained in end condition [1]:
	[[1.1],[1.2],[1.3]] indicates that 1.1, 1.2, and 1.3 must be met for [1] to be met
	Contained in [1.1]:
		[1,2,3] where:
			1 - indicates the sensor ID which is read
			2 - indicates if the sensor must be greater than or less than a specified value
			3 - indicates the set sensor value the actual reading is checked against

RPI RX List Format
[State Progress, Which Endpoint was Met, Sensor Values]
	State Progress States:
		0: Process in Progress
		1: Process completed
		2: Process Error/Safety Shut Down
		
RPI File Structure
Save Folder: Saves Machine running hours, Current Wash Process Count for Datalogger, List of wash process files (Pre, Wash, and Post),

"""

"""
Initial Startup
	1) Initial variable definitions and file path settings
	2) Read Save Folder
		Current Wash Number
	
UI Loop
	Select Wash Process
	Run Wash Process
	Settings
	
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