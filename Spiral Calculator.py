#The import libraries
import math
from tkinter import *

#Here are the functions for making the calculations
def CalcDCFromRC(R_C):
	ans = 18000 / math.pi / R_C
	return round(ans, 10)
def CalcDCFromLS(THETA_S, LS): 
	ans = 200 * (THETA_S / LS)
	return round(ans, 10)
def CalcLSFromDC(THETA_S, D_C):
	ans = 200 * (THETA_S / D_C)
	return round(ans, 10)
def CalcTHETASFromDC(LS, D_C):
	ans = LS * D_C / 200
	return round(ans, 10)
def CalcDELTA(L, R_C):
	ans = 180 * L / (math.pi * R_C)
	return round(ans, 10)
def CalcTHETASFromRC(LS, R_C):
	ans = math.degrees(LS / 2 * R_C)
	return round(ans, 10)
def	CalcXC(LS, THETA_S):
	ans = (LS / 100) * (100 - 0.0030462 * math.pow(THETA_S, 2))
	return round(ans, 10)
def CalcYC(LS, THETA_S):
	ans = (LS / 100) * (0.58178 * THETA_S - 0.000012659 * math.pow(THETA_S, 3))
	return round(ans, 10)
def CalcP(Y_C, R_C, THETA_S):
	ans = Y_C - R_C * (1.0 - math.cos(math.radians(THETA_S)))
	return round(ans, 10)
def CalcA(THETA_S, LS):
	ans = 20000 * THETA_S / math.pow(LS, 2)
	return round(ans, 10)
def CalcK(LS, A):
	ans = 0.5 * LS - 0.000127 * math.pow(A, 2) * math.pow(LS / 100, 5)
	return round(ans, 10)
def CalcTS(R_C, P, DELTA, K):
	ans = (R_C + P) * math.tan(math.radians(DELTA / 2)) + K
	return round(ans, 10)
def CalcES(R_C, P, DELTA):
	ans = (R_C + P) * (math.tan(math.radians(DELTA / 2)) * math.tan(math.radians(DELTA / 4))) + P
	return round(ans, 10) 
def CalcLT(X_C, Y_C, THETA_S):
	ans = X_C - (Y_C * (1 / math.tan(math.radians(THETA_S))))
	return round(ans, 10)
def CalcST(Y_C, THETA_S):
	ans = Y_C / math.sin(math.radians(THETA_S))
	return round(ans, 10) 
def CalcLC(LS, A):
	ans = LS - 0.00034 * math.pow(A, 2) * math.pow((LS / 100), 5)
	return round(ans, 10)
def CalcDELTAC(DELTA, THETA_S):
	ans = DELTA - 2 * THETA_S
	return round(ans, 10) 

#Functions for the GUI
def IsNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def ClearAll():
	ClearLeft()
	ClearRight()
def ClearLeft():
	KnownR_C.delete(0, END)
	KnownD_C.delete(0, END)
	KnownLs.delete(0, END)
	KnownTHETA_S.delete(0, END)
	KnownL.delete(0, END)
	KnownDELTA.delete(0, END)
	KnownX_C.delete(0, END)
	KnownY_C.delete(0, END)
	KnownP.delete(0, END)
	KnownA.delete(0, END)
	KnownK.delete(0, END)
	KnownT_S.delete(0, END)
	KnownE_S.delete(0, END)
	KnownLT.delete(0, END)
	KnownST.delete(0, END)
	KnownLC.delete(0, END)
	KnownDELTA_C.delete(0, END)
def ClearRight():
	UnknownR_C.delete(0, END)
	UnknownD_C.delete(0, END)
	UnknownLs.delete(0, END)
	UnknownTHETA_S.delete(0, END)
	UnknownL.delete(0, END)
	UnknownDELTA.delete(0, END)
	UnknownX_C.delete(0, END)
	UnknownY_C.delete(0, END)
	UnknownP.delete(0, END)
	UnknownA.delete(0, END)
	UnknownK.delete(0, END)
	UnknownT_S.delete(0, END)
	UnknownE_S.delete(0, END)
	UnknownLT.delete(0, END)
	UnknownST.delete(0, END)
	UnknownLC.delete(0, END)
	UnknownDELTA_C.delete(0, END)
	
def	ComputeAll():
	ClearRight()
	
	#Checks if all entered are digits and copies them to the right
	if(IsNumber(KnownR_C.get())):
		UnknownR_C.insert(0, KnownR_C.get())
	if(IsNumber(KnownD_C.get())):
		UnknownD_C.insert(0, KnownD_C.get())
	if(IsNumber(KnownLs.get())):
		UnknownLs.insert(0, KnownLs.get())
	if(IsNumber(KnownTHETA_S.get())):
		UnknownTHETA_S.insert(0, KnownTHETA_S.get())
	if(IsNumber(KnownL.get())):
		UnknownL.insert(0, KnownL.get())
	if(IsNumber(KnownDELTA.get())):
		UnknownDELTA.insert(0, KnownDELTA.get())
	if(IsNumber(KnownX_C.get())):
		UnknownX_C.insert(0, KnownX_C.get())
	if(IsNumber(KnownY_C.get())):
		UnknownY_C.insert(0, KnownY_C.get())	
	if(IsNumber(KnownP.get())):
		UnknownP.insert(0, KnownP.get())
	if(IsNumber(KnownA.get())):
		UnknownA.insert(0, KnownA.get())
	if(IsNumber(KnownK.get())):
		UnknownK.insert(0, KnownK.get())
	if(IsNumber(KnownT_S.get())):
		UnknownT_S.insert(0, KnownT_S.get())
	if(IsNumber(KnownE_S.get())):
		UnknownE_S.insert(0, KnownE_S.get())
	if(IsNumber(KnownLT.get())):
		UnknownLT.insert(0, KnownLT.get())
	if(IsNumber(KnownST.get())):
		UnknownST.insert(0, KnownST.get())
	if(IsNumber(KnownLC.get())):
		UnknownLC.insert(0, KnownLC.get())
	if(IsNumber(KnownDELTA_C.get())):
		UnknownDELTA_C.insert(0, KnownDELTA_C.get())
		
	#Does the calculations based on what has been calculated or defined
	if(IsNumber(UnknownR_C.get()) and not IsNumber(UnknownD_C.get())):
		UnknownD_C.insert(0, CalcDCFromRC(float(KnownR_C.get())))
	if(IsNumber(UnknownTHETA_S.get()) and IsNumber(UnknownLs.get()) and not IsNumber(UnknownD_C.get())):
		UnknownD_C.insert(0, CalcDCFromLS(float(UnknownTHETA_S.get()), float(UnknownLs.get())))
	if(IsNumber(UnknownTHETA_S.get()) and IsNumber(UnknownD_C.get()) and not IsNumber(UnknownLs.get())):
		UnknownLs.insert(0, CalcLSFromDC(float(UnknownTHETA_S.get()), float(UnknownD_C.get())))
	if(IsNumber(UnknownLs.get()) and IsNumber(UnknownD_C.get()) and not IsNumber(UnknownTHETA_S.get())):
		UnknownTHETA_S.insert(0, CalcTHETASFromDC(float(UnknownLs.get()), float(UnknownD_C.get())))
	if(UnknownTHETA_S.get() and UnknownD_C.get() and not UnknownLs.get()):
		UnknownLs.insert(0, CalcLSFromDC(float(UnknownTHETA_S.get()), float(UnknownD_C.get())))
	if(IsNumber(UnknownL.get()) and IsNumber(UnknownR_C.get()) and not IsNumber(UnknownDELTA.get())):
		UnknownDELTA.insert(0, CalcDELTA(float(UnknownL.get()), float(UnknownR_C.get())))
	if(IsNumber(UnknownLs.get()) and IsNumber(UnknownR_C.get()) and not IsNumber(UnknownTHETA_S.get())):
		UnknownTHETA_S.insert(0, CalcTHETASFromRC(float(UnknownLs.get()), float(UnknownR_C.get())))
	if(IsNumber(UnknownLs.get()) and IsNumber(UnknownTHETA_S.get()) and not IsNumber(UnknownX_C.get())):
		UnknownX_C.insert(0, CalcXC(float(UnknownLs.get()), float(UnknownTHETA_S.get())))
	if(IsNumber(UnknownLs.get()) and IsNumber(UnknownTHETA_S.get()) and not IsNumber(UnknownY_C.get())):
		UnknownY_C.insert(0, CalcYC(float(UnknownLs.get()), float(UnknownTHETA_S.get())))
	if(IsNumber(UnknownY_C.get()) and IsNumber(UnknownR_C.get()) and IsNumber(UnknownTHETA_S.get()) and not IsNumber(UnknownP.get())):
		UnknownP.insert(0, CalcP(float(UnknownY_C.get()), float(UnknownR_C.get()), float(UnknownTHETA_S.get())))
	if(IsNumber(UnknownTHETA_S.get()) and IsNumber(UnknownLs.get()) and not IsNumber(UnknownA.get())):
		UnknownA.insert(0, CalcA(float(UnknownTHETA_S.get()), float(UnknownLs.get())))
	if(IsNumber(UnknownLs.get()) and IsNumber(UnknownA.get()) and not IsNumber(UnknownK.get())):
		UnknownK.insert(0, CalcK(float(UnknownLs.get()), float(UnknownA.get())))
	if(IsNumber(UnknownR_C.get()) and IsNumber(UnknownP.get()) and IsNumber(UnknownDELTA.get()) and IsNumber(UnknownK.get()) and not IsNumber(UnknownT_S.get())):
		UnknownT_S.insert(0, CalcTS(float(UnknownR_C.get()), float(UnknownP.get()), float(UnknownDELTA.get()), float(UnknownK.get())))
	if(IsNumber(UnknownR_C.get()) and IsNumber(UnknownP.get()) and IsNumber(UnknownDELTA.get()) and not IsNumber(UnknownE_S.get())):
		UnknownE_S.insert(0, CalcES(float(UnknownR_C.get()), float(UnknownP.get()), float(UnknownDELTA.get())))
	if(IsNumber(UnknownX_C.get()) and IsNumber(UnknownY_C.get()) and IsNumber(UnknownTHETA_S.get()) and not IsNumber(UnknownLT.get())):
		UnknownLT.insert(0, CalcLT(float(UnknownX_C.get()), float(UnknownY_C.get()), float(UnknownTHETA_S.get())))
	if(IsNumber(UnknownY_C.get()) and IsNumber(UnknownTHETA_S.get()) and not IsNumber(UnknownST.get())):
		UnknownST.insert(0, CalcST(float(UnknownY_C.get()), float(UnknownTHETA_S.get())))
	if(IsNumber(UnknownLs.get()) and IsNumber(UnknownA.get()) and not IsNumber(UnknownLC.get())):
		UnknownLC.insert(0, CalcLC(float(UnknownLs.get()), float(UnknownA.get())))
	if(IsNumber(UnknownDELTA.get()) and IsNumber(UnknownTHETA_S.get()) and not IsNumber(UnknownDELTA_C.get())):
		UnknownDELTA_C.insert(0, CalcDELTAC(float(UnknownDELTA.get()), float(UnknownTHETA_S.get())))
	

	
#The program starts here
#Do not edit
root = Tk()
root.title('Spiral Curve Calculator')
Label(root, text="Variable").grid(row = 0)
Label(root, text="Known").grid(row = 0, column = 1)
Label(root, text="Unknown").grid(row = 0, column = 2)

Label(root, text="R_C").grid(row = 1)
KnownR_C = Entry(root)
KnownR_C.grid(row = 1, column = 1)
UnknownR_C = Entry(root)
UnknownR_C.grid(row = 1, column = 2)

Label(root, text="D_C").grid(row = 2)
KnownD_C = Entry(root)
KnownD_C.grid(row = 2, column = 1)
UnknownD_C = Entry(root)
UnknownD_C.grid(row = 2, column = 2)

Label(root, text="Ls").grid(row = 3)
KnownLs = Entry(root)
KnownLs.grid(row = 3, column = 1)
UnknownLs = Entry(root)
UnknownLs.grid(row = 3, column = 2)

Label(root, text="THETA_S").grid(row = 4)
KnownTHETA_S = Entry(root)
KnownTHETA_S.grid(row = 4, column = 1)
UnknownTHETA_S = Entry(root)
UnknownTHETA_S.grid(row = 4, column = 2)

Label(root, text="L").grid(row = 5)
KnownL = Entry(root)
KnownL.grid(row = 5, column = 1)
UnknownL = Entry(root)
UnknownL.grid(row = 5, column = 2)

Label(root, text="DELTA").grid(row = 6)
KnownDELTA = Entry(root)
KnownDELTA.grid(row = 6, column = 1)
UnknownDELTA = Entry(root)
UnknownDELTA.grid(row = 6, column = 2)

Label(root, text="X_C").grid(row = 7)
KnownX_C = Entry(root)
KnownX_C.grid(row = 7, column = 1)
UnknownX_C = Entry(root)
UnknownX_C.grid(row = 7, column = 2)

Label(root, text="Y_C").grid(row = 8)
KnownY_C = Entry(root)
KnownY_C.grid(row = 8, column = 1)
UnknownY_C = Entry(root)
UnknownY_C.grid(row = 8, column = 2)

Label(root, text="p").grid(row = 9)
KnownP = Entry(root)
KnownP.grid(row = 9, column = 1)
UnknownP = Entry(root)
UnknownP.grid(row = 9, column = 2)

Label(root, text="A").grid(row = 10)
KnownA = Entry(root)
KnownA.grid(row = 10, column = 1)
UnknownA = Entry(root)
UnknownA.grid(row = 10, column = 2)

Label(root, text="k").grid(row = 11)
KnownK = Entry(root)
KnownK.grid(row = 11, column = 1)
UnknownK = Entry(root)
UnknownK.grid(row = 11, column = 2)

Label(root, text="T_S").grid(row = 12)
KnownT_S = Entry(root)
KnownT_S.grid(row = 12, column = 1)
UnknownT_S = Entry(root)
UnknownT_S.grid(row = 12, column = 2)

Label(root, text="E_S").grid(row = 13)
KnownE_S = Entry(root)
KnownE_S.grid(row = 13, column = 1)
UnknownE_S = Entry(root)
UnknownE_S.grid(row = 13, column = 2)

Label(root, text="LT").grid(row = 14)
KnownLT = Entry(root)
KnownLT.grid(row = 14, column = 1)
UnknownLT = Entry(root)
UnknownLT.grid(row = 14, column = 2)

Label(root, text="ST").grid(row = 15)
KnownST = Entry(root)
KnownST.grid(row = 15, column = 1)
UnknownST = Entry(root)
UnknownST.grid(row = 15, column = 2)

Label(root, text="LC").grid(row = 16)
KnownLC = Entry(root)
KnownLC.grid(row = 16, column = 1)
UnknownLC = Entry(root)
UnknownLC.grid(row = 16, column = 2)

Label(root, text="DELTA_C").grid(row = 17)
KnownDELTA_C = Entry(root)
KnownDELTA_C.grid(row = 17, column = 1)
UnknownDELTA_C = Entry(root)
UnknownDELTA_C.grid(row = 17, column = 2)

ClearButton = Button(root, text = "Clear", command = ClearAll)
ClearButton.grid(row = 18, column = 1)
ComputeButton = Button(root, text = "Compute", command = ComputeAll)
ComputeButton.grid(row = 18, column = 2)
root.mainloop()