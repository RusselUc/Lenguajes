from tkinter import *
from funciones import infija_a_sufija, infija_a_prefija,evaluacionNotacionSufija


class Calculadora:

    def __init__(self):

        self.ventana = Tk()
        self.ventana.geometry('320x320')
        self.ventana.title("Lenguaje y automatas")

        self.componentes()

        self.ventana.mainloop()

    def componentes(self):
        self.resPrefijo = StringVar()
        self.dato = StringVar()
        self.resPosfijo = StringVar()
        self.resultado = StringVar()

        texto = Label(self.ventana, text = "Use espaciados despues de cada caracter ejemplo: \n ( 6 + 4 ) * 8 ( 7 + 4 )")
        texto.grid(row = 0, column = 0, padx = 5, pady =5, sticky = E)

        infijo = Label(self.ventana, text="Infijo: ")
        infijo.config(
            # fg="white",
            # bg="darkgray",
            font=("Open Sans", 12),
            padx=10,
            pady=10,
        )
        infijoInput = Entry(self.ventana, textvariable=self.dato)

        infijo.grid(row = 1, column = 0, padx = 5, pady =5, sticky = W)
        infijoInput.grid(row = 1, column = 0, padx = 0, pady =5, ipadx=25, sticky = E)

        prefijo = Label(self.ventana, text="prefijo: ")
        prefijo.config(
            # fg="white",
            # bg="darkgray",
            font=("Open Sans", 12),
            padx=10,
            pady=10,
        )
        self.prefijoOut = Label(self.ventana, textvariable=self.resPrefijo)

        prefijo.grid(row = 3, column = 0, padx = 5, pady =5, sticky = W)
        self.prefijoOut.grid(row = 3, column = 0, padx = 5, pady =5, sticky = E)

        posfijo = Label(self.ventana, text="posfijo: ")
        posfijo.config(
            # fg="white",
            # bg="darkgray",
            font=("Open Sans", 12),
            padx=10,
            pady=10,
        )
        self.posfijoOut = Label(self.ventana, textvariable=self.resPosfijo)

        posfijo.grid(row = 4, column = 0, padx = 5, pady =5, sticky = W)
        self.posfijoOut.grid(row = 4, column = 0, padx = 5, pady =5, sticky = E)

        r = Label(self.ventana, text="Resultado: ")
        r.config(
            # fg="white",
            # bg="darkgray",
            font=("Open Sans", 12),
            padx=10,
            pady=10,
        )

        r.grid(row = 5, column = 0, padx = 5, pady =5, sticky = W)

        self.result = Label(self.ventana, textvariable = self.resultado)
        self.result.grid(row = 5, column = 0, padx = 5, pady =5, sticky = E)

        btn = Button(self.ventana, text = "Resultado", command = self.resolve)
        btn.grid(row = 6, column = 0, sticky = E)
    
    def resolve(self):
        self.resPrefijo.set(infija_a_prefija(self.dato.get()))
        self.resPosfijo.set(infija_a_sufija(self.dato.get()))
        try:
            self.resultado.set(evaluacionNotacionSufija((self.resPosfijo.get())))
        except IndexError:
            self.resultado.set(self.dato.get())

        if len(self.resPosfijo.get()) >= 1:
            self.posfijoOut.config(
                fg = "white",
                bg = "black",
                font=("Open Sans", 10),
                padx=5,
                pady=5,
            )
        
        if len(self.resPrefijo.get()) >= 1:
            self.prefijoOut.config(
                fg = "white",
                bg = "black",
                font=("Open Sans", 10),
                padx=5,
                pady=5,
            )

        if len(self.resultado.get()) >= 1:
            self.result.config(
                fg = "white",
                bg = "black",
                font=("Open Sans", 10),
                padx=5,
                pady=5,
            )

