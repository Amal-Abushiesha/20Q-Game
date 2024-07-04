import customtkinter

customtkinter.set_appearance_mode("dark")




class App(customtkinter.CTk):
    width = 600
    height = 400
    
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Server")
        self.geometry(f"{self.width}x{self.height}+550+50")
        self.resizable(False, False)
        self.textvar = customtkinter.StringVar()

        dialog = customtkinter.CTkInputDialog(text="Enter Object name", title="Object Name")
        self.object = dialog.get_input()
        self.filename = self.selectfile()
        self.answer = ""
        self.photo = False
        
        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=45)
        self.login_frame.place(x = 300, y= 200,anchor="center", relwidth=0.9, relheight=0.9)
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Server",
                                                  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.login_label.place(x=225, y=10)
        
        
        self.textbox = customtkinter.CTkTextbox(self.login_frame, width=490, height=205, font=customtkinter.CTkFont(size=20, weight="bold"), state="disabled")
        self.textbox.place(x=25, y=60)
        

        self.yes_btn = customtkinter.CTkButton(self.login_frame, text="Yes", command=self.button_click_yes, border_width=2, fg_color="transparent", text_color=("gray10", "#DCE4EE"), font=("arial", 15))

        self.yes_btn.place(x=50, y=(625-340))
        
        self.no_btn = customtkinter.CTkButton(self.login_frame, text="No", command=self.button_click_no, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), hover_color="#b00e0e", font=("arial", 15))
        self.no_btn.place(x=355, y=(625-340))


    def button_click_yes(self):
        self.answer = self.textvar.get()
        print(self.answer)
        
        self.yes_btn.configure(state="disabled")
        self.no_btn.configure(state="disabled")

        self.answer = "yes"
    
    def button_click_no(self):
        self.answer = self.textvar.get()
        print(self.answer)
        
        self.no_btn.configure(state="disabled")
        self.yes_btn.configure(state="disabled")

        self.answer = "no"

        
        
    def get_input(self):
        send = self.answer
        self.answer= ""
        return send
    
    def ViewText(self, text):
        self.textbox.configure(state="normal")
        print(text)
        self.textbox.insert("end", text = f"{text} \n")
        self.textbox.configure(state="disabled")

    def selectfile(self):
            filename = customtkinter.filedialog.askopenfilename(filetypes =[('Image file', '*.jpg')])
            if filename == "":
                self.photo = False
            else:
                self.photo = True
            print(filename)
            
            return filename



if __name__ == "__main__":
    app = App()
    app.mainloop()