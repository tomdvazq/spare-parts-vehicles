import tkinter as tk
from views.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Repuestos Vehículos')
    

    barra_menu(root)

    app = Frame(root = root)

    
    app.mainloop()


if __name__ == '__main__':
    main()
