
# Mecanum Car Project  

## 📖 Overview  
This project involves a **Mecanum-wheeled vehicle** controlled by a **Raspberry Pi Pico** and **Bluetooth** communication. The Mecanum wheels allow omnidirectional movement (forward, backward, sideways, and diagonally), offering exceptional maneuverability.  

The project integrates **embedded systems programming** with control logic for precise motor control and real-time command processing via Bluetooth.

---

## ⚙️ Features  
- **Mecanum Wheels:** Enables omnidirectional movement  
- **Raspberry Pi Pico:** Main controller responsible for processing commands  
- **Bluetooth Communication:** Wireless control using a mobile app or other Bluetooth-enabled devices  

---

## 🚀 Getting Started  

### 1. **Clone the repository:**  
```bash
git clone https://github.com/martowicz/mecanum_car.git
```

### 2. **Hardware Requirements:**  
- **Raspberry Pi Pico**  
- **Mecanum wheels with motors**  
- **Motor driver module (compatible with the Pico)**  
- **Bluetooth module (e.g., HC-05)**  
- **Power supply (battery pack)**  

---

## 🔧 Setup and Installation  
1. **Connect the components:**  
   - Connect the motors to the motor driver.  
   - Connect the motor driver and Bluetooth module to the Raspberry Pi Pico according to the circuit diagram.  
   
2. **Flash the code:**  
   - Install [Thonny](https://thonny.org/) or another MicroPython IDE.  
   - Flash MicroPython firmware on the Raspberry Pi Pico.  
   - Upload the project files to the Pico.

3. **Bluetooth pairing:**  
   - Pair the Bluetooth module with your mobile device.  
   - Use a compatible app to send movement commands (forward, backward, rotate, etc.).  

---

## 📱 Bluetooth Control Commands  
- **Forward:** `F`  
- **Backward:** `B`  
- **Left:** `L`  
- **Right:** `R`  
- **Stop:** `S`  

---

## 🛠️ Future Improvements  
- Adding sensor-based obstacle detection  
- Implementing autonomous driving mode  
- Enhancing the mobile app interface for smoother control  

---

## 📄 License  
This project is licensed under the [MIT License](LICENSE).  
