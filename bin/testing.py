import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Testing")

if __name__ == "__main__":
    app = App()
    app.mainloop()