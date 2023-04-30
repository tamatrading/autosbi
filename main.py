import tkinter as tk
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

DISP_MODE = "ON"   # "ON" or "OFF"

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Input Form")
        self.geometry("400x300")

        self.entries = {}
        self.submitted_data = None

        self.create_label_entry("ユーザーネーム", "g_username")
        self.create_label_entry("ログインパスワード", "g_loginpass")
        self.create_label_entry("発注パスワード", "g_ordpass")
        self.create_label_entry("メールアドレス", "g_mailaddr")
        self.create_label_entry("メールパスワード", "g_mailpass")
        self.create_label_entry("設定パーセント", "g_setper")

        self.load_previous_input()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()

    def create_label_entry(self, label_text, key):
        label = tk.Label(self, text=label_text)
        label.pack()
        entry = tk.Entry(self)
        entry.pack()
        self.entries[key] = entry

    def load_previous_input(self):
        try:
            with open("new_previous_input.pkl", "rb") as f:
                previous_input = pickle.load(f)
                for key, entry in previous_input.items():
                    entry_widget = self.entries[key]
                    entry_widget.insert(0, entry)
        except FileNotFoundError:
            pass

    def submit(self):
        submitted_data = {}
        for key in ["g_username", "g_loginpass", "g_ordpass", "g_mailaddr", "g_mailpass", "g_setper"]:
            entry_widget = self.entries[key]
            input_text = entry_widget.get()
            submitted_data[key] = input_text
            #print(f"Submitted {key}: {input_text}")

        with open("new_previous_input.pkl", "wb") as f:
            pickle.dump(submitted_data, f)

        self.submitted_data = submitted_data
        self.quit()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
    user_input = app.submitted_data
    ret = 0

    if user_input is not None:
        if DISP_MODE == "OFF":
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            ret = sbiIpoOrder(driver, user_input)

        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        print(f"ret={ret}")


    else:
        print("quit!")
