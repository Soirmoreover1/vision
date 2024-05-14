import tkinter as tk
import speech_recognition as sr
import sys

class SpeechToTextApp:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.output_file = open("output.txt", "a", encoding="utf-8")
        self.headphones_index = 2  
        self.password = "مرحبا"  
        self.listening = False

        self.root = tk.Tk()
        self.root.title("Speech to Text")
        self.root.geometry("500x500")

        self.label_login = tk.Label(self.root, text="قل كلمة السر للدخول", font=("Arial", 20))
        self.label_login.pack()

        self.close_button = tk.Button(self.root, text="إغلاق", command=self.close, font=("Arial", 16))
        self.close_button.pack(pady=10)

        self.listen_button_login = tk.Button(self.root, text="استمع", command=self.listen_password, font=("Arial", 16))
        self.listen_button_login.pack(pady=10)

        self.label_listen = tk.Label(self.root, text="قل شيئاً........", font=("Arial", 20))
        self.label_listen.pack()

        self.listen_button = tk.Button(self.root, text="استمع", command=self.toggle_listen, font=("Arial", 16))

    def toggle_listen(self):
        if not self.listening:
            self.listen_button.config(text="توقف")
            self.listening = True
            self.listen()
        else:
            self.listen_button.config(text="استمع")
            self.listening = False

    def listen_password(self):
        try:
            with sr.Microphone(device_index=self.headphones_index) as src:
                audio = self.rec.listen(src)
                spoken_password = self.rec.recognize_google(audio_data=audio, language="ar")
                if spoken_password == self.password:
                    self.label_login.pack_forget()
                    self.close_button.pack_forget()
                    self.listen_button_login.pack_forget()
                    self.label_listen.pack()
                    self.listen_button.pack(pady=20)
                else:
                    
                    from tkinter import messagebox
                    messagebox.showerror("خطأ في كلمة المرور", "كلمة المرور غير صحيحة.")
        except Exception as e:
        
            from tkinter import messagebox
            messagebox.showerror("حدث خطأ", "حدث خطأ أثناء تسجيل كلمة المرور: " + str(e))

    def listen(self):
        try:
            with sr.Microphone(device_index=self.headphones_index) as src:
                audio = self.rec.listen(src)
                text = self.rec.recognize_google(audio_data=audio, language="ar")
                self.label_listen.config(text="قلت: " + text)
                self.output_file.write(text + "\n")
                self.output_file.flush()
                if text == "اغلاق":
                    self.close()
        except Exception as e:
            self.label_listen.config(text="حدث خطأ: " + str(e))


    def close(self):
        self.output_file.close()
        self.root.destroy()
        sys.exit(0)

if __name__ == "__main__":
    app = SpeechToTextApp()
    app.root.mainloop()
