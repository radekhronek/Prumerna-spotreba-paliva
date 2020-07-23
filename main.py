import tkinter as tk

window = tk.Tk()
window.title("Spotřeba paliva")
font_muj = ("Times New Roman", 20)
font_vysl = ("Ariel", 30)


def opravavstupu(vstup):
    try:
        comma = vstup.index(",")
        oprava_vstup = vstup[:comma] + "." + vstup[comma + 1:]
        return float(oprava_vstup)
    except:
        return float(vstup)


def spotreba():
    kilometers = opravavstupu(e1_value.get())
    litres = opravavstupu(e2_value.get())
    spot = round(float(100 * litres / kilometers), 2)
    vysl.config(font=font_vysl, text=spot, relief="solid", bg="red")


l1 = tk.Label(window, text="Ujeté kilometry")
l1.config(font=font_muj)
l1.grid(row=0, column=0)

e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

l2 = tk.Label(window, text="Natankováno litrů")
l2.config(font=font_muj)
l2.grid(row=1, column=0)

e2_value = tk.StringVar()
e2 = tk.Entry(window, textvariable=e2_value)
e2.grid(row=1, column=1)

b1 = tk.Button(window, text="SPOČÍTEJ", command=spotreba, bg="blue")
b1["font"] = font_muj
b1.grid(row=2, column=0, columnspan=2)

vysl = tk.Label(window, text="", height=1, width=10)
vysl["font"] = font_vysl
vysl.grid(row=3, column=0, columnspan=2)

window.mainloop()
