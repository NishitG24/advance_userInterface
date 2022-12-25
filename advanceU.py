import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x300")

def login():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12,padx=10)

entryuser = customtkinter.CTkEntry(master=frame, placeholder_text="username")
entryuser.pack(pady=12, padx=10)


entrypassword = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
entrypassword.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="login", command=login)
button.pack(pady=12, padx=10)

checkBox= customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkBox.pack(pady=12, padx=10)

root.mainloop()

