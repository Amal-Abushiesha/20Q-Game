import customtkinter
from PIL import Image
import receive_mail_IMAP as rec
import tkinter.messagebox as msg

customtkinter.set_appearance_mode("dark")

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("image")
        self.geometry("500x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
                
   
        self.large_test_image = customtkinter.CTkImage(Image.open(r"F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\FTP_RCV\new.jpg"), size=(500, 500))
        self.home_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.large_test_image).pack()

class App(customtkinter.CTk):
    width = 600
    height = 750
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.bind("<Return>", self.button_click)

        self.title("Client")
        self.geometry(f"{self.width}x{self.height}+550+50")
        self.resizable(False, False)
        self.question_guess = ""
        self.textvar = customtkinter.StringVar()

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=45)
        self.login_frame.place(x = 300, y= 375,anchor="center", relwidth=0.9, relheight=0.9)
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Client",
                                                  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.login_label.place(x=225, y=10)
        
        
        self.textbox = customtkinter.CTkTextbox(self.login_frame, width=490, height=555, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.textbox.place(x=25, y=60)
        

        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=350, placeholder_text="Question / Guess", textvariable= self.textvar)
        self.username_entry.place(x=25, y=625)
        
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Send", command=self.button_click)
        self.login_button.place(x=380, y=625)


    def button_click(self, x=1):
        self.question_guess = self.textvar.get()
        print(self.question_guess)
        
        self.textvar.set("")
        self.login_button.configure(state="disabled")

        
        
    def get_input(self):
        send = self.question_guess
        self.question_guess= ""
        return send
    
    def ViewText(self, text):
        print(self.username_entry.get())
        self.textbox.configure(state="normal")
        print(text)
        self.textbox.insert("end", text = f"{text} \n")
        self.textbox.configure(state="disabled")
        

    def open_toplevel(self, y=1):
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed

    def print_mail(self):
        dialog = customtkinter.CTkInputDialog(text="Enter your password to show the email", title="Password")
        check = rec.get_mail(dialog.get_input())
        if not check:
            msg.showerror(title="Error", message="Incorrect password")



if __name__ == "__main__":
    app = App()
    app.mainloop()
