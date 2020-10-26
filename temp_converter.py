import tkinter as tk
window = tk.Tk()  #establishing tk context

window.title("temperature_converter")

#Create entry form called frm_entry, then put it on the window (assign master to window)
frm_entry = tk.Frame(master=window)

#Input field
#Width is how long we want the textbox to be
ent_temperature = tk.Entry(master=frm_entry, width=10)

lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

#Sticky, e for right
#w for left
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

#def (C - 32) = 32 + 1.8*f
#(5/9) * (float(f) - 32)
def f_2_c():
    #Get the temp from the entry field
    f = ent_temperature.get()

    celsius = (5/9) * (float(f) - 32)
    lbl_temp["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    

#Assigned to window
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command = f_2_c
    )

lbl_result = tk.Label(master=window, text ="\N{DEGREE CELSIUS}")

#Pack all the visuals
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

#Run the application
window.mainloop()
