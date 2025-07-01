import tkinter as tk
from tkinter import messagebox
from levels import get_levels
import os

class TreasureHuntGame:
    def __init__(self, master):
        self.master = master
        master.title("Giải mã kho báu")

        self.levels = get_levels()
        self.level = None
        self.score = 0
        self.highscore = self.load_highscore()

        # Màn hình chọn cấp độ
        self.select_frame = tk.Frame(master, bg="#e6f0ff")
        tk.Label(self.select_frame, text="🎯 Chọn cấp độ để bắt đầu", font=("Helvetica", 18, "bold"), bg="#e6f0ff").pack(pady=15)
        for i, level in enumerate(self.levels):
            btn = tk.Button(
                self.select_frame,
                text=f"Cấp độ {i+1}: {level['name']}",
                font=("Helvetica", 12),
                width=30,
                command=lambda idx=i: self.start_level(idx)
            )
            btn.pack(pady=5)
        self.highscore_label = tk.Label(self.select_frame, text=f"🏆 Điểm cao nhất: {self.highscore}", font=("Helvetica", 12), bg="#e6f0ff")
        self.highscore_label.pack(pady=10)
        self.select_frame.pack()

        # Màn hình chơi
        self.play_frame = tk.Frame(master, bg="#f0f5f5")

        self.label = tk.Label(self.play_frame, text="", font=("Helvetica", 16, "bold"), fg="blue", bg="#f0f5f5")
        self.label.pack(pady=10)

        self.cipher_label = tk.Label(self.play_frame, text="", font=("Helvetica", 13), wraplength=550, bg="#f0f5f5")
        self.cipher_label.pack()

        self.entry = tk.Entry(self.play_frame, width=60, font=("Helvetica", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.play_frame, text="Giải mã", font=("Helvetica", 12), command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.feedback_label = tk.Label(self.play_frame, text="", font=("Helvetica", 13), bg="#f0f5f5")
        self.feedback_label.pack()

        self.score_label = tk.Label(self.play_frame, text="Điểm: 0", font=("Helvetica", 12), bg="#f0f5f5")
        self.score_label.pack(pady=5)

        self.back_button = tk.Button(self.play_frame, text="🔙 Quay lại menu", font=("Helvetica", 12), command=self.back_to_menu)
        self.back_button.pack(pady=5)

    def start_level(self, idx):
        self.level = idx
        self.score = 0
        self.select_frame.pack_forget()
        self.play_frame.pack()
        self.load_level()

    def load_level(self):
        if self.level >= len(self.levels):
            self.label.config(text="🎉 Chúc mừng! Bạn đã tìm được kho báu!")
            self.cipher_label.config(text="")
            self.submit_button.config(state="disabled")
            self.entry.config(state="disabled")
            if self.score > self.highscore:
                self.save_highscore(self.score)
                self.feedback_label.config(text="🏆 Điểm cao mới!", fg="purple")
            else:
                self.feedback_label.config(text="")
        else:
            level_info = self.levels[self.level]
            self.label.config(text=f"Cấp độ {self.level + 1}: {level_info['name']}")
            self.cipher_label.config(text=f"Thông điệp mã hóa:\n{level_info['cipher']}")
            self.entry.config(state="normal")
            self.entry.delete(0, tk.END)
            self.feedback_label.config(text="")
            self.submit_button.config(state="normal")
            self.score_label.config(text=f"Điểm: {self.score}")

    def check_answer(self):
        user_input = self.entry.get().strip().lower()
        expected = self.levels[self.level]["answer"].strip().lower()
        if user_input == expected:
            self.feedback_label.config(text="✅ Chính xác! Tiếp tục...", fg="green")
            self.score += 1
            self.level += 1
            self.master.after(1200, self.load_level)
        else:
            self.feedback_label.config(text=f"❌ Sai rồi!\nĐáp án đúng: {self.levels[self.level]['answer']}", fg="red")

    def back_to_menu(self):
        self.play_frame.pack_forget()
        self.select_frame.pack()
        self.level = None
        self.score = 0
        self.highscore = self.load_highscore()
        self.highscore_label.config(text=f"🏆 Điểm cao nhất: {self.highscore}")

    def load_highscore(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r", encoding="utf-8") as f:
                return int(f.read().strip())
        return 0

    def save_highscore(self, score):
        with open("highscore.txt", "w", encoding="utf-8") as f:
            f.write(str(score))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("640x450")
    game = TreasureHuntGame(root)
    root.mainloop()
