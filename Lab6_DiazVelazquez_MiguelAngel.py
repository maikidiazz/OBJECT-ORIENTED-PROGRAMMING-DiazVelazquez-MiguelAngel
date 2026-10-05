import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self):
        return f" {self.name}: Turning on light with 80% brightness."


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa Smart Speaker")

    def turn_on(self):
        return f" {self.name}: Playing favorite playlist."


class SmartAC(SmartDevice):
    def __init__(self):
        super().__init__("Samsung Smart AC")

    def turn_on(self):
        return f" {self.name}: Cooling room to 22°C."


class SmartTV(SmartDevice):
    def __init__(self):
        super().__init__("LG Smart TV 4K")

    def turn_on(self):
        return f" {self.name}: Screen turned on, opening Netflix."


class SmartLock(SmartDevice):
    def __init__(self):
        super().__init__("August Smart Lock")

    def turn_on(self):
        return f" {self.name}: Main door safely locked."


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Nest Smart Thermostat")

    def turn_on(self):
        return f" {self.name}: Heating schedule activated."


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6 - Smart Home Controller (Polymorphism)")
        self.geometry("480x420")
        self.resizable(False, False)

        try:
            self.iconbitmap("icon.ico")
        except Exception:
            pass

        self.items = {
            "Smart Light": SmartLight(),
            "Smart Speaker": SmartSpeaker(),
            "Smart AC": SmartAC(),
            "Smart TV": SmartTV(),
            "Smart Lock": SmartLock(),
            "Smart Thermostat": SmartThermostat(),
        }

        self._build_interface()

    def _build_interface(self):
        lbl_header = tk.Label(
            self,
            text="Polymorphism in Smart Home Devices",
            font=("Arial", 14, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=10)

        group_box = tk.LabelFrame(
            self,
            text=" Select a Smart Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        self.selected_key = tk.StringVar(value="")

        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=2)

        btn_action = tk.Button(
            self,
            text="EXECUTE ACTION",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=10)

        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'EXECUTE ACTION'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        chosen_key = self.selected_key.get()

        if not chosen_key:
            self.lbl_output.config(
                text="PELIGRO, selecciona una opción antes de continuar.",
                font=("Arial", 10, "bold"),
                fg="#c0392b"
            )
            return

        active_object: SmartDevice = self.items[chosen_key]
        result_message = active_object.turn_on()

        self.lbl_output.config(
            text=result_message,
            font=("Arial", 10, "normal"),
            fg="#27ae60"
        )


if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()