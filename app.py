import tkinter as tk
import csv
import os
from tkinter import simpledialog, messagebox


candidates = ["Parchanda", "Oli", "Balen"]  
file = "votes.csv"
admin_password = "1234" 


if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Candidate", "Votes"])
        for c in candidates:
            writer.writerow([c, 0])
else:
    with open(file, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    header = data[0] if data else ["Candidate", "Votes"]
    existing_candidates = [row[0] for row in data[1:]]  # skip header
    for c in candidates:
        if c not in existing_candidates:
            data.append([c, 0])
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def read_votes():
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        return {row[0]: int(row[1]) for row in reader}

def save_votes(data):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Candidate", "Votes"])
        for k,v in data.items():
            writer.writerow([k,v])

def vote(name):
    data = read_votes()
    data[name] += 1
    save_votes(data)
    messagebox.showinfo("Vote Submitted", f"Your vote for {name} has been recorded!")

def admin_view():
    pwd = simpledialog.askstring("Admin Login", "Enter password:", show="*")
    if pwd == admin_password:
        data = read_votes()
        result_text = ""
        for c,v in data.items():
            result_text += f"{c} : {v} votes\n"
        messagebox.showinfo("Election Results", result_text)
    else:
        messagebox.showerror("Error", "Incorrect password!")

# ===============================
# 4️⃣ GUI
# ===============================
root = tk.Tk()
root.title("Private Voting System")
root.geometry("400x450")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Vote for Your Candidate", font=("Arial", 18))
title.pack(pady=10)

# Vote buttons
frame = tk.Frame(root)
frame.pack(pady=5)

for c in candidates:
    btn = tk.Button(frame, text=f"Vote for {c}", width=25, height=2,
                    command=lambda x=c: vote(x))
    btn.pack(pady=5)

# Admin button
admin_btn = tk.Button(root, text="Admin: Show Results", width=25, height=2, bg="red", fg="white",
                      command=admin_view)
admin_btn.pack(pady=20)

root.mainloop()