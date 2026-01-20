# Moore Machine Simulator

A Python-based simulator for Moore and Mealy Machines with a GUI built using **PyQt6**. This tool allows users to define finite-state machines, add states and transitions, simulate input strings, and visualize the automata using **Graphviz**.

## Contributors🙌

<span>
    <a href="https://www.github.com/ahmedyar7">
        <img alt="Static Badge" src="https://img.shields.io/badge/Ahmed%20Yar-black?style=for-the-badge&logo=github">
    </a>
    <a href="https://www.github.com/SameerTalreja">
        <img alt="Static Badge" src="https://img.shields.io/badge/Sameer%20Talreja-%20%2329424d?style=for-the-badge&logo=github">
    </a>
    <a href="https://www.github.com/AbulBasit">
        <img alt="Static Badge" src="https://img.shields.io/badge/Abul%20Basit-%20%232a294d?style=for-the-badge&logo=github">
    </a>
    <a href="https://www.github.com/HumayunJunaid">
        <img alt="Static Badge" src="https://img.shields.io/badge/Humayun%20Junaid-%20%23320954?style=for-the-badge&logo=github">
    </a>
    <a href="https://github.com/DevStudent101-yk">
        <img alt="Static Badge" src="https://img.shields.io/badge/Younus%20Khan-%20%234b9965?style=for-the-badge&logo=github">
    </a>
</span>

## ✨ Features

- Define **states** with outputs (Moore) or transitions with outputs (Mealy).
- Set the **initial state**.
- Add transitions dynamically through the GUI.
- Simulate **input strings** and view step-by-step output.
- Generate and view **state transition graphs**.
- Switch between **Moore and Mealy** machine modes.
- User-friendly GUI built with **PyQt6**.
- Graph rendering using **Graphviz**.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **PyQt6** – GUI framework
- **Graphviz** – For visualizing the automata
- **Qt Designer** (optional) – To design the UI
- **OOP** and modular architecture

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Moore-Machine-Simulator.git
cd Moore-Machine-Simulator
```

### Step 2: Create a Virtual Environment
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python main.py
```

The GUI will launch, and you can start defining your Moore or Mealy machines.

---

## 📸 Screenshots

| Moore Machine Simulator                   | Graph View                                   |
| ----------------------------------------- | -------------------------------------------- |
| ![UI Screenshot](./assets/imgs/image.png) | ![Graph](./machine_images/moore_machine.png) |

---

## 🧠 How It Works

### Moore Machine

- Outputs are associated **with states**.
- Transition: `A --0--> B`
- Output string is based on the **states visited**.

### Mealy Machine

- Outputs are associated **with transitions**.
- Transition: `A --0/1--> B`
- Output string is based on **input symbols** and transitions.

---

## 🧪 Simulation Example

For a Moore machine:

- States: A (Output=0), B (Output=1)
- Initial: A
- Transitions:
  - A --0--> B
  - B --1--> A
- Input: `01`
- Output: `0 1 0`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- graphviz
- Install the graphviz and add to the system environment Variables

```
https://graphviz.org/download/
```

### Install Dependencies

```bash
pip install pyqt5 graphviz
```

### Run the App

```bash
python main.py
```

---

## 📂 Project Structure

```
moore_mealy_simulator/
│
├── main.py                 # Main GUI launcher
├── moore_machine.py        # Moore machine logic
├── mealy_machine.py        # Mealy machine logic
├── graph_generator.py      # Graphviz logic
├── simulator_controller.py # Central logic to handle events
├── ui_mainwindow.ui        # Qt Designer file
├── README.md
└── assets/imgs/
    ├── image.png
```

---

## 👨‍💻 License

[MIT-LICENSE](./LICENSE)
