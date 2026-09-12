import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class WashDashboard(tb.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tb.Label(self, text="WashDashboard", font=("Helvetica", 8)).pack(pady=30)
        tb.Button(self, text="Halt Process",
                   command=lambda: controller.show_frame("HaltProcess"),
                   bootstyle=SECONDARY).pack(pady=10)
        
        Progress_Bar = tb.Progressbar(self, bootstyle="success.Striped.Horizontal", length=200, mode="determinate")
        Progress_Bar.pack(pady=10)
        Progress_Bar.start(10)
        Sensor_Status = tb.Label(self, text=f"""
WPS:{0}, P_Res:{1}, P_Wash:{2}, LC_Wash_1:{3},LC_Wash_2:{4}, LC_Res_1:{5}, LC_Res_2:{6}, NF_W:{7}, NF_R:{8},
DR_W:{9}, DF_R:{10}, CS_VV:{11}, CS_WS:{12}, RE_Wash:{12}, RE_Res:{13},
LS_RFR:{14}, LS_PTC:{15}, LS_WFE:{16}, E_Stop:{17}, LS_WC:{18}, ET:{19}, TET:{20}
                                 """.format(*[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]),#Wash Data String Placeholder
            font=("Helvetica", 6),  anchor="sw")
        Sensor_Status.place(anchor="sw", relx=0, rely=1)# relwidth=1, relheight=0.3
                                 
'''
        Sensor_Status = tb.Label(self, text="""
    
    VA_WWI {}, VA_WWO: {}, VA_XO {}, VA_A {}, VB {}, 
    DM_DIR_WASH {}, DM_SPD_WASH {}, DM_DIR_RES {}, DM_SPD_RES{},
    P_DD
    NST1_i
    NST1_r
    NST1_v
    NST2_i
    NST2_r
    NST2_v

                                 """, font=("Helvetica", 8))
'''