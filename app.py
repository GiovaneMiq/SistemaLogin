import os
import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
import sys
import bcrypt


def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

class BackEnd():

    #--------------- DATABASE ----------------
    def db_connect(self):
        db_path = resource_path("users.db")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        print("Database connected.")

    def db_disconnect(self):
        self.conn.close()
        print("Database disconnected.")

    def create_user_table(self):
        self.db_connect()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
            )
        """)

        self.conn.commit()
        print("User table ensured.")
        self.db_disconnect()

    def add_user(self):
        self.register_username = self.username_register_entry.get()
        self.register_password = self.password_register_entry.get()
        self.confirm_password_register = self.confirm_password_entry.get()

        try:
            if (self.register_username == "" or self.register_password == "" or self.confirm_password_register == ""):
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

            elif (len(self.register_username) < 5):
                messagebox.showerror("Erro", "O nome de usuário deve ter pelo menos 5 caracteres.")
            elif (len(self.register_password) < 6):
                messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
            elif (self.register_password != self.confirm_password_register):
                messagebox.showerror("Erro", "As senhas não coincidem.")
            elif (self.register_password == self.confirm_password_register):
                self.db_connect()
                hashed_password = self.hash_password(self.register_password)
                self.cursor.execute("""INSERT INTO users(username, password)
                    VALUES (?, ?)""", (self.register_username, hashed_password))
                self.conn.commit()
                self.db_disconnect()
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                self.register_clean_entry()
                self.show_login()
            else:
                self.conn.commit()
                messagebox.showinfo("Sistema de login", "Usuário cadastrado com sucesso!")
        except sqlite3.IntegrityError:
            self.db_disconnect()
            messagebox.showerror("Erro", "Nome de usuário já existe. Escolha outro.")

        except Exception as e:
            self.db_disconnect()
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


    #--------------- HASH ----------------
    def hash_password(self, password: str) -> str:
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed.decode()

    def check_password(self, password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed.encode())

    #--------------- LOGINAUTH ----------------
    def login_user(self):
        self.login_username = self.username_login.get()
        self.login_password = self.password_login.get()

        try:
            if (self.login_username == "" or self.login_password == ""):
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            else:
                self.db_connect()
                self.cursor.execute("""SELECT password FROM users WHERE username = ?""",
                                    (self.login_username,))
                result = self.cursor.fetchone()
                self.db_disconnect()

                if result and self.check_password(self.login_password, result[0]):
                    messagebox.showinfo("Sucesso", f"Bem-vindo, {self.login_username}!")
                    self.login_clean_entry()
                else:
                    messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
        except Exception as e:
            self.db_disconnect()
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.create_user_table()
        self.config_main_windown()
        self.create_static_elements()
        self.create_login_screen()
        self.create_register_screen()
        self.show_login()

    # ---------------- WINDOWN CONFIG ----------------
    def config_main_windown(self):
        self.geometry("700x420")
        self.title("LoginSys")
        self.resizable(False, False)

    def create_static_elements(self):
        img_path = resource_path("loginimage.png")


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

        #InputLoginUsername
        self.username_login = ctk.CTkEntry(
            self.frame_login, width=300,
            placeholder_text="Nome...",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.username_login.grid(row=1, column=0, pady=10)

        #INputLoginPassword
        self.password_login = ctk.CTkEntry(
            self.frame_login, width=300,
            placeholder_text="Senha...",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.password_login.grid(row=2, column=0, pady=10)

        # Login show password checkbox
        self.show_password_login_var = IntVar(value=0)
        self.show_password_login = ctk.CTkCheckBox(
            self.frame_login,
            text="Mostrar senha",
            variable=self.show_password_login_var,
            command=self._toggle_login_show_password
        )
        self.show_password_login.grid(row=3, column=0, pady=5)
        # Bind focus handlers for login password field
        self.password_login.bind(
            "<FocusIn>", lambda e: self._entry_mask_focus_in(self.password_login, e)
        )
        self.password_login.bind(
            "<FocusOut>", lambda e: self._entry_mask_focus_out(self.password_login, e)
        )

        #LoginButton
        ctk.CTkButton(
            self.frame_login, width=300,
            text="ENTRAR",
            font=("Century Gothic", 16, "bold"),
            command=self.login_user
        ).grid(row=4, column=0, pady=10)

        #GoToRegisterFrameButton
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

        #Title
        ctk.CTkLabel(
            self.frame_register, text="Cadastre-se",
            font=("Century Gothic", 22, "bold")
        ).grid(row=0, column=0, pady=10)

        #InputUsername
        self.username_register_entry = ctk.CTkEntry(
            self.frame_register, width=300,
            placeholder_text="Crie um nome...",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.username_register_entry.grid(row=1, column=0, pady=10)

        #InputPassword
        self.password_register_entry = ctk.CTkEntry(
            self.frame_register, width=300,
            placeholder_text="Crie uma senha...",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.password_register_entry.grid(row=2, column=0, pady=10)

        #InputConfirmPassword
        self.confirm_password_entry = ctk.CTkEntry(
            self.frame_register, width=300,
            placeholder_text="Confirme sua senha...",
            font=("Century Gothic", 16, "bold"),
            corner_radius=15
        )
        self.confirm_password_entry.grid(row=3, column=0, pady=10)

        # Show password checkbox (keeps placeholders visible until toggled)
        self.show_password_var = IntVar(value=0)
        self.show_password = ctk.CTkCheckBox(
            self.frame_register,
            text="Mostrar senha",
            variable=self.show_password_var,
            command=self._toggle_register_show_password
        )
        self.show_password.grid(row=4, column=0, pady=5)

        # Register button
        self.register_button = ctk.CTkButton(
            self.frame_register, width=300,
            text="CADASTRAR",
            font=("Century Gothic", 16, "bold"),
            command=self.add_user
        )
        self.register_button.grid(row=5, column=0, pady=10)

        #RegisterTextButton
        lb_login = ctk.CTkLabel(
            self.frame_register,
            text="Já tem uma conta? Clique aqui e faça seu login.",
            text_color="#6C8BDF",
            cursor="hand2"
        )
        lb_login.grid(row=6, column=0, pady=10)
        lb_login.bind("<Button-1>", self.show_login)

        # Bind focus handlers so password placeholders remain visible
        # until the user focuses the field; on focus we enable masking.
        self.password_register_entry.bind(
            "<FocusIn>", lambda e: self._entry_mask_focus_in(self.password_register_entry, e)
        )
        self.password_register_entry.bind(
            "<FocusOut>", lambda e: self._entry_mask_focus_out(self.password_register_entry, e)
        )
        self.confirm_password_entry.bind(
            "<FocusIn>", lambda e: self._entry_mask_focus_in(self.confirm_password_entry, e)
        )
        self.confirm_password_entry.bind(
            "<FocusOut>", lambda e: self._entry_mask_focus_out(self.confirm_password_entry, e)
        )

    def register_clean_entry(self, event=None):
        self.username_register_entry.delete(0, END)
        self.password_register_entry.delete(0, END)
        self.confirm_password_entry.delete(0, END)

    def login_clean_entry(self):
        self.username_login.delete(0, END)
        self.password_login.delete(0, END)


    # ---------------- SWITCH ----------------
    def show_login(self, event=None):
        self.frame_register.place_forget()
        self.frame_login.place(x=350, y=10)

    def show_register(self, event=None):
        self.frame_login.place_forget()
        self.frame_register.place(x=350, y=10)

    def _entry_mask_focus_in(self, entry, event=None):
        try:
            entry.configure(show="*")
        except Exception:
            pass

    def _entry_mask_focus_out(self, entry, event=None):
        try:
            if entry.get() == "":
                entry.configure(show="")
            else:
                entry.configure(show="*")
        except Exception:
            pass

    def _toggle_register_show_password(self):
        # When checkbox checked -> show plain text; unchecked -> follow focus/content rules
        try:
            if self.show_password_var.get():
                self.password_register_entry.configure(show="")
                self.confirm_password_entry.configure(show="")
            else:
                # if fields empty keep placeholder visible, else mask
                if self.password_register_entry.get() == "":
                    self.password_register_entry.configure(show="")
                else:
                    self.password_register_entry.configure(show="*")
                if self.confirm_password_entry.get() == "":
                    self.confirm_password_entry.configure(show="")
                else:
                    self.confirm_password_entry.configure(show="*")
        except Exception:
            pass

    def _toggle_login_show_password(self):
        try:
            if self.show_password_login_var.get():
                self.password_login.configure(show="")
            else:
                if self.password_login.get() == "":
                    self.password_login.configure(show="")
                else:
                    self.password_login.configure(show="*")
        except Exception:
            pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
