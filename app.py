import os
import customtkinter as ctk
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config_main_windown()
        self.login_screen()

    #ConfigMainWindown
    def config_main_windown(self):
        self.geometry("700x420")
        self.title("LoginSys")
        self.resizable(False, False)

    def login_screen(self):
            img_path = os.path.join("Images", "loginimage.png")

            #images
            self.img = PhotoImage(file=img_path)
            self.img = self.img.subsample(3,3)
            self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
            self.lb_img.grid(row=1, column=0, padx=20)

            #plataform title
            self.title = ctk.CTkLabel(self, text="Login necessário. Faça login\n ou cadastre-se para continuar.", font=("Century Gothic", 15, "bold"))
            self.title.grid(row=0, column=0, pady=10, padx=10)

            #formloginframe
            self.frame_login = ctk.CTkFrame(self, width=350, height=380)
            self.frame_login.place(x=350, y=10)

            #Loginformframewidgets
            self.lb_title = ctk.CTkLabel(self.frame_login, text="Login", font=("Century Gothic", 22, "bold"))
            self.lb_title.grid(row=0, column=0, padx=10, pady=10)
            
            #InputUsername
            self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Nome...", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="#1E3A8A")
            self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

            #InputPassword
            self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Senha...", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="#1E3A8A", show="*")
            self.password_login_entry.grid(row=2, column=0, padx=10, pady=10)

            #ShowPasswordCheckBox
            self.show_password = ctk.CTkCheckBox(self.frame_login, text="Clique para mostrar a senha.", font=("Century Gothic", 12, "bold"), corner_radius=20, border_color="#1E3A8A")
            self.show_password.grid(row=3, column=0, padx=10, pady=10)

            #LoginButton
            self.login_button = ctk.CTkButton(self.frame_login, width=300, text="Entrar".upper(), font=("Century Gothic", 16, "bold"), fg_color="#1E3A8A")
            self.login_button.grid(row=4, column=0, padx=10)

            #RegisterBindAndText
            self.sap = ctk.CTkLabel(self.frame_login, width=250, text="Ainda não tem uma conta?\nClique aqui para se cadastrar.", text_color="#6C8BDF", cursor="hand2")
            self.sap.grid(row=5, column=0, padx=10, pady=10)
            self.sap.bind("<Button-1>", self.register_screen)


    def register_screen(self, event=None):

        #RemoveLoginForm
        self.frame_login.place_forget()

        #FormRegisterFrame
        self.frame_register = ctk.CTkFrame(self, width=350, height=380)
        self.frame_register.place(x=350, y=10)

       #Registerformframewidgets
        self.lb_title = ctk.CTkLabel(self.frame_register, text="Cadastre-se", font=("Century Gothic", 22, "bold"))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        #InputUsername
        self.username_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text="Crie um nome...", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="#1E3A8A")
        self.username_register_entry.grid(row=1, column=0, padx=10, pady=10)

        #InputPassword
        self.password_register_entry = ctk.CTkEntry(self.frame_register, width=300, placeholder_text="Crie uma senha...", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="#1E3A8A", show="*")
        self.password_register_entry.grid(row=2, column=0, padx=10, pady=10)

        self.confirm_password = ctk.CTkEntry(self.frame_register, width=300, placeholder_text="Confirme sua senha...", font=("Century Gothic", 16, "bold"), corner_radius=15, border_color="#1E3A8A", show="*")
        self.confirm_password.grid(row=3, column=0, padx=10, pady=10)

        #ShowPasswordCheckBox
        self.show_password = ctk.CTkCheckBox(self.frame_register, text="Clique para mostrar a senha.", font=("Century Gothic", 12, "bold"), corner_radius=20, border_color="#1E3A8A")
        self.show_password.grid(row=4, column=0, padx=10, pady=10)

        #RegisterButton
        self.register_button = ctk.CTkButton(self.frame_register, width=300, text="Cadastrar".upper(), font=("Century Gothic", 16, "bold"), fg_color="#1E3A8A")
        self.register_button.grid(row=5, column=0, padx=10)

        #LoginBindAndText
        self.sap_register = ctk.CTkLabel(self.frame_register, width=250, text="Já tem uma conta? Clique aqui e faça seu login.", text_color="#6C8BDF", cursor="hand2")
        self.sap_register.grid(row=6, column=0, padx=10, pady=10)
        self.sap_register.bind("<Button-1>", self.Back_login)

    def Back_login(self, event):
        self.frame_register.place_forget()
        self.login_screen()


if __name__ == "__main__":
    app = App()
    app.mainloop()