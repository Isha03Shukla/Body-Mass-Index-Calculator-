import tkinter

root =tkinter.Tk()
root.title("BMI Calculator")

def calculate_bmi():
    kg=float(entry_kg.get())
    hgt=float(entry_hgt.get())
    bmi=round(kg/(hgt ** 2),2)
    label_res['text']=f"BMI: {bmi}"
    

#Creating GUI
label_kg=tkinter.Label(root, text="KG: ")
label_kg.pack()

entry_kg=tkinter.Entry(root)
entry_kg.pack()

label_hgt=tkinter.Label(root, text="HEIGHT: ")
label_hgt.pack()

entry_hgt=tkinter.Entry(root)
entry_hgt.pack()

label_res=tkinter.Label(root, text="BMI: ")
label_res.pack()

btn_cal=tkinter.Button(root, text="Calculate", command=calculate_bmi)
btn_cal.pack()

root.mainloop()