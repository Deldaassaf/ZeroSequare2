from Stage1 import Stage1
from Stage2 import Stage2
from Stage3 import Stage3
import tkinter as tk
from tkinter import messagebox

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Zero Squares Game")
        
        # إعداد المرحلة الأولى
        self.current_stage = 1
        self.stages = [Stage1(), Stage2(), Stage3()]
        self.colors = ["red", "blue"]  # لون كل حالة وهدفها
        
        self.setup_board()
        self.bind_keys()
        self.display_stage()

    def setup_board(self):
        # إعداد اللوحة الرسومية للعبة
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.cell_size = 400 // 8  # حجم الخلية
        self.rects = {}

    def display_stage(self):
        # تحديث المرحلة الحالية
        self.canvas.delete("all")
        stage = self.stages[self.current_stage - 1]
        
        # رسم الشبكة والخلايا
        for i in range(8):
            for j in range(8):
                color = "white"
                if stage.board[i][j] == 0:
                    color = "gray"  # عائق
                elif stage.board[i][j] == "I":
                    color = self.colors[stage.initial_states.index((i, j)) % len(self.colors)]  # لون الحالة
                elif stage.board[i][j] == "W":
                    color = self.colors[stage.goals.index((i, j)) % len(self.colors)]  # لون الهدف
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.rects[(i, j)] = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

    def bind_keys(self):
        # ربط مفاتيح الأسهم للتحريك
        self.root.bind("<Up>", lambda e: self.move("up"))
        self.root.bind("<Down>", lambda e: self.move("down"))
        self.root.bind("<Left>", lambda e: self.move("left"))
        self.root.bind("<Right>", lambda e: self.move("right"))

    def move(self, direction):
        # تحريك الحالات في المرحلة الحالية
        stage = self.stages[self.current_stage - 1]
        stage.move(direction)
        self.display_stage()
        
        # التحقق من حالة الفوز
        if stage.game_over:
            if self.current_stage < len(self.stages):
                messagebox.showinfo("تهانينا!", f"لقد أنهيت المرحلة {self.current_stage}!")
                self.current_stage += 1
                self.display_stage()
            else:
                messagebox.showinfo("تهانينا!", "لقد أنهيت جميع المراحل! ستعود الآن إلى المرحلة الأولى.")
                self.current_stage = 1
                self.display_stage()



# تشغيل اللعبة
root = tk.Tk()
game_gui = GameGUI(root)
root.mainloop()
