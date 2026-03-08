# 🗳️ Online Voting System (Python)

A simple **GUI-based Voting System** built with **Python and Tkinter**.
This project allows users to vote for candidates through a graphical interface, while the votes are securely stored in a **CSV file**.
The voting results are **hidden from the public** and can only be viewed by the **admin with a password**.

---

## 📌 Features

* Simple **graphical user interface**
* **Vote for candidates using buttons**
* **Automatic CSV file creation**
* **Votes stored securely**
* **Results hidden from public**
* **Admin password required to view results**
* Easy to **add candidates through code**

---

## 🛠 Requirements

You need the following installed:

* Python 3.x
* Tkinter (comes built-in with Python)

Check Python installation:

```bash
python --version
```

---

## 📂 Project Structure

```
online-voting-system
│
├── app.py
├── votes.csv
└── README.md
```

* **app.py** → Main Python voting program
* **votes.csv** → Stores vote counts
* **README.md** → Project documentation

---

## ⚙️ How to Run the Project

1. Download or clone the project.
2. Open the project folder.
3. Run the Python file:

```bash
python app.py
```

4. The voting window will open.

---

## 🗳 How Voting Works

1. Users click the **Vote button** for their preferred candidate.
2. The vote is **recorded in the CSV file**.
3. A confirmation message appears.
4. The results remain **hidden from voters**.

---

## 🔐 Admin Access

To view election results:

1. Click the **Admin: Show Results** button.
2. Enter the **admin password**.
3. The vote counts will be displayed.

Change the password in the code:

```python
admin_password = "1234"
```

---

## 👥 Adding Candidates

Edit this line in the code:

```python
candidates = ["Prachanda", "Oli", "Balen"]
```

Example:

```python
candidates = ["Candidate 1", "Candidate 2", "Candidate 3"]
```

The program will automatically update the **votes.csv** file.

---

## 📊 Example votes.csv

```
Candidate,Votes
Pushpa Kamal Dahal (Prachanda),3
KP Sharma Oli,2
Balen Shah,5
```

---

## 🎯 Future Improvements

* One vote per user system
* Voter login system
* Graphical vote statistics
* Network-based voting
* Modern UI design

---

## 👨‍💻 Author

**Himanshu Sapkota**

---

## 📜 License

This project is open-source and free to use for educational purposes.
