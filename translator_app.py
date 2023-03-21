import customtkinter
import tkinter
from morse_translator import MorseTranslator



class TranslatorApp:
    def __init__(self) -> None:
        
        # System Settings
        customtkinter.set_appearance_mode("System") # Light/dark theme == system theme
        customtkinter.set_default_color_theme("dark-blue")
        
        # Root frame
        self.root = customtkinter.CTk()
        self.root.geometry("450x800")
        self.root.title("Text to morse translator. By Diego")
        
        # New frame
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # New label
        self.label = customtkinter.CTkLabel(master=self.frame, text="Text to morse translator", font=("Roboto", 24))
        self.label.pack(pady=20, padx=10)
        
        # Text input
        self.input_text = customtkinter.CTkTextbox(self.frame, width=400, height=250, font=("Helvetic", 20, "bold"))
        self.input_text.pack(pady=20, padx=10)

        # Translate button
        self.translate_button = customtkinter.CTkButton(self.frame, text="Translate!", command=self.get_output)
        self.translate_button.pack(pady=20, padx=10)
        
        # Text output
        self.output_text = customtkinter.CTkTextbox(master=self.frame, width=400, height=250, font=("Helvetic", 20, "bold"))
        self.output_text.pack(pady=20, padx=10)
        self.output_text.insert("1.0", "PRUEBA PROBANDO")



        
    def run(self):
        self.root.mainloop()
        
    def get_input(self):
        return self.input_text.get("0.0", "end")
    
    def get_output(self):
        phrase = self.get_input().strip("\n")
        print(phrase.strip("\n"))
        translator = MorseTranslator("text_to_morse.db")
        morse_phrase = translator.translate(phrase.upper())
        self.output_text.delete("0.0", "end")
        self.output_text.insert("0.0", morse_phrase)
        
