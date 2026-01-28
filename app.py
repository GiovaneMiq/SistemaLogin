import os
import customtkinter as ctk
from tkinter import PhotoImage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config_main_windown()
        self.create_static_elements()
        self.create_login_screen()
        self.create_register_screen()
        self.show_login()

    # ---------------- CONFIG ----------------
    def config_main_windown(self):
        self.geometry("700x420")
        self.title("LoginSys")
        self.resizable(False, False)

    def create_static_elements(self):
        img_path = os.path.join("Images", "loginimage.png")

        self.img = PhotoImage(file=img_path).subsample(3, 3)
        self.lb_img = ctk.CTkLabel(self, image=self.img, text=None)
        self.lb_img.grid(row=1, column=0, padx=20)

        self.lb_main_title = ctk.CTkLabel(
            self,
            text="Login necessário. Faça login\nou cadastre-se para continuar.",
            font=("Century Gothic", 15, "bold")
        )
        self.lb_main_title.grid(row=0, column=0, pady=10)

    # ---------------- LOGIN ----------------
    def create_login_screen(self):
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)

        ctk.CTkLabel(
            self.frame_login, text="Login",
            font=("Century Gothic", 22, "bold")
        ).grid(row=0, column=0, pady=10)

        self.username_login = ctk.CTkEntry(
            self.frame_login, width=300,
            placeholder_text="Nome...",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.username_login.grid(row=1, column=0, pady=10)

        self.password_login = ctk.CTkEntry(
            self.frame_login, width=300,
            placeholder_text="Senha...",
            show="*",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.password_login.grid(row=2, column=0, pady=10)

        ctk.CTkButton(
            self.frame_login, width=300,
            text="ENTRAR",
            font=("Century Gothic", 16, "bold")
        ).grid(row=4, column=0, pady=10)

        lb_register = ctk.CTkLabel(
            self.frame_login,
            text="Ainda não tem uma conta?\nClique aqui para se cadastrar.",
            text_color="#6C8BDF",
            cursor="hand2"
        )
        lb_register.grid(row=5, column=0, pady=10)
        lb_register.bind("<Button-1>", self.show_register)

    # ---------------- REGISTER ----------------
    def create_register_screen(self):
        self.frame_register = ctk.CTkFrame(self, width=350, height=380)

        ctk.CTkLabel(
            self.frame_register, text="Cadastre-se",
            font=("Century Gothic", 22, "bold")
        ).grid(row=0, column=0, pady=10)

        ctk.CTkEntry(
            self.frame_register, width=300,
            placeholder_text="Crie um nome...",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        ).grid(row=1, column=0, pady=10)

        ctk.CTkEntry(
            self.frame_register, width=300,
            placeholder_text="Crie uma senha...",
            show="*",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        ).grid(row=2, column=0, pady=10)

        ctk.CTkEntry(
            self.frame_register, width=300,
            placeholder_text="Confirme sua senha...",
            show="*",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        ).grid(row=3, column=0, pady=10)

        ctk.CTkButton(
            self.frame_register, width=300,
            text="CADASTRAR",
            font=("Century Gothic", 16, "bold")
        ).grid(row=5, column=0, pady=10)

        lb_login = ctk.CTkLabel(
            self.frame_register,
            text="Já tem uma conta? Clique aqui e faça seu login.",
            text_color="#6C8BDF",
            cursor="hand2"
        )
        lb_login.grid(row=6, column=0, pady=10)
        lb_login.bind("<Button-1>", self.show_login)

    # ---------------- SWITCH ----------------
    def show_login(self, event=None):
        self.frame_register.place_forget()
        self.frame_login.place(x=350, y=10)

    def show_register(self, event=None):
        self.frame_login.place_forget()
        self.frame_register.place(x=350, y=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
