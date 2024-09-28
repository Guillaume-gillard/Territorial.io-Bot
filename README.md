# **Territorial.io Bot**

This project is a basic bot that interacts with the game [Territorial.io](https://territorial.io) using Selenium. It automatically joins lobbies and performs simple actions.

## **Environment Setup**

1. **Clone the repository**:
    ```bash
    git clone git@github.com:Guillaume-gillard/Territorial.io-Bot.git
    cd Territorial.io-Bot
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    # For Windows
    env\Scripts\activate
    # For Mac/Linux
    source env/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the bot**:
    ```bash
    python main.py
    ```

### **Project Brief**
This bot automatically selects a lobby in [Territorial.io](https://territorial.io), chooses a starting position, and performs actions such as expanding territory and analyzing opponents.

### **File Structure**
- **`main.py`**: Entry point for starting the bot.
- **`player.py`**: Contains the logic for interacting with the game (e.g., selecting start positions, expanding, etc.).
- **`worker.py`**: Contains common functions such as taking screenshots and analyzing pixels.
- **`game.py`**: Helper class for managing game states and UI interactions.
