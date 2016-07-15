from Tkinter import *

root = Tk()
root.title("MU Report Generator")
root.minsize(width=500, height=500)
# Code to add widgets will go here...

def mu_sel():
   mu_stage = "You selected " + mu_var.get()
   label.config(text = mu_stage)

def url_entry():
   firm_url = "You selected " + url_var.get()
   label.config(text=firm_url) 

#Entry field for firm url
url_var = StringVar()
L1 = Label(root, text="Enter the firm url for the practice:")
L1.pack(side=LEFT, anchor=NE)	
E1 = Entry(root, bd=1, exportselection=0, textvariable=url_var)
E1.pack(side=LEFT, anchor=NE)
B1 = Button(root, text="Press to save URL:", width=10, command=url_entry)
B1.pack(side=LEFT, anchor=NE)

#Radiobuttons to select the MU Stage
mu_var = StringVar()
R1 = Radiobutton(root, text="Stage 1", variable=mu_var, value="STAGE_1", command=mu_sel)
R1.pack(padx=5, pady=10, side=LEFT)
R2 = Radiobutton(root, text="Stage 2", variable=mu_var, value="STAGE_2", command=mu_sel)
R2.pack(padx=5, pady=10, side=LEFT)
R3 = Radiobutton(root, text="Modified Stage 1", variable=mu_var, value="MODIFIED_SCHEDULED_STAGE_1", command=mu_sel)
R3.pack(padx=5, pady=10, side=LEFT)
R4 = Radiobutton(root, text="Modified Stage 2", variable=mu_var, value="MODIFIED_SCHEDULED_STAGE_2", command=mu_sel)
R4.pack(padx=5, pady=10, side=LEFT)

label = Label(root)
label.pack(anchor=CENTER, side=BOTTOM)
root.mainloop()
