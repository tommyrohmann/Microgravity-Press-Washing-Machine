#Washing Machine Control Loop

"""
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
                        """
"""
1) Washwater Inlet Valve Actuator, VA_WWI
2) Washwater Outlet Valve Actuator, VA_WWO
3) Cross-over Valve Actuator, VA_XO
4) Air Valve Actuator, VA_A
5) Chamber Piston Drive Motor, DM_Cha
6) Reservoir Piston Drive Motor, DM_Res
7) Detergent Pump, P_Det
[VA_WWI, VA_WWO, VA_XO, VA_A, DM_Wash, DM_Res, P_Det]
"""
"""
1) Reservoir Pressure, P_Res
2) Wash Chamber Pressure, P_Cha
3) Load Cell 1, LC_Cha_1
4) Load Cell 2, LC_Cha 2
5) Load Cell 3, LC_Res_1
6) Load Cell 4, LC_Res_1
7) Valve Actuator Current Sensor, CS_VV
8) Washing Machine Current Sensor, CS_WS 
9) Rotary Encoder, Enc_Wash
10) Rotary Encoder, Enc_Res
11) Wash Piston Limit Switch
12) Limit Switch
13) Limit Switch
14) Emergency Stop, E_Stop

Derived Data for Logging
1) Load Cell Force Sum Wash Chamber, LC_Cha_Sum
2) Load Cell Force Sum Reservior, LC_Res_Sum
3) Load Cell Force Differential Chamber, LC_Cha_Dif
4) Load Cell Force Differential Reservoir, LC_Res_Dif
5) Elapsed Time, ET
"""
WashInstructions = 

for i in WashInstructions