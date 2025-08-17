import os

folders = [
    "01_Introduction_to_Robotics",
    "02_Mechanics_and_Electronics",
    "03_Microcontrollers_Programming",
    "04_Sensors_and_Actuators",
    "05_Control_Systems",
    "06_Robot_Simulation_ROS",
    "07_AI_and_Computer_Vision",
    "08_Projects_and_Portfolio"
]

day = 1
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    for i in range(10):  # 10 days each section
        filename = f"{folder}/Day_{day:02}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Day {day}\n\n")
            f.write("📌 **Topic:** \n\n")
            f.write("🎥 **YouTube Tutorial:** \n\n")
            f.write("🛠️ **Practical Task:** \n\n")
            f.write("📒 **Notes:** \n")
        day += 1
