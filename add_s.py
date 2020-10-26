import tkinter as tk
window = tk.Tk()  #establishing tk context

window.title("temperature_converter")

#Create entry form called frm_entry, then put it on the window (assign master to window)
frm_entry = tk.Frame(master=window)

#Input field
#Width is how long we want the textbox to be
ent_temperature = tk.Entry(master=frm_entry, width=6)

lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

#Sticky, e for right
#w for left
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

#Delete f_2_c()
#And replace it with your own function
#Function must read .get() value from ent_temperature
#Function must set lbl_temp["text"] = .get() value + "s"
def add_s():
    #Get the text from the entry field
    f = ent_temperature.get()

    #celsius = (5/9) * (float(f) - 32)
    lbl_temp["text"] = f"{f}s" #f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    

#Assigned to window
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command = add_s #f_2_c
    )

lbl_result = tk.Label(master=window, text ="\N{DEGREE CELSIUS}")

#Pack all the visuals
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, padx=10)
lbl_result.grid(row=0, column=2, padx=10)

#Run the application
window.mainloop()
