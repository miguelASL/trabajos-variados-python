import tkinter as tk
import time

def start_cronometru():
    global running, start_time
    running = True
    start_time = time.time() - elapsed_time
    update_cronometru()
    
def stop_cronometru():
    global running
    running = False

def reset_cronometru():
    global elapsed_time
    elapsed_time = 0
    cronometru_label.config(text= 'Cronometro: 00:00:00.000')

def update_cronometru():
    if running:
        global elapsed_time
        elapsed_time = time.time() - start_time
        ore, rem = divmod(elapsed_time, 3600)
        minute, secunde = divmod(rem, 60)
        secunde, zecimi = divmod(secunde, 1)
        cronometru_label.config(text= f"Cronometro: {int(ore):02}:{int(minute):02}:{int(secunde):02}.{int(zecimi*1000):03d}")
        cronometru_label.after(1, update_cronometru)

app = tk.Tk()
app.title('Cronometro de Miguel Sarmiento !')

cronometru_label = tk.Label(app, text= 'Cronometro: 00:00:00.000', font= ('Helvetica', 20))
cronometru_label.pack()

button_frame = tk.Frame(app)
button_frame.pack()

start_button = tk.Button(button_frame, text= 'Start', command= start_cronometru)
start_button.pack(side= tk.LEFT, padx= 10)

stop_cronometru = tk.Button(button_frame, text= 'Stop', command= stop_cronometru)
stop_cronometru.pack(side= tk.LEFT, padx= 10)

reset_cronometru = tk.Button(button_frame, text= 'Reset', command= reset_cronometru)
reset_cronometru.pack(side= tk.LEFT, padx= 10)

runnign = False
elapsed_time = 0

app.mainloop()