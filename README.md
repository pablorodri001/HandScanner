# HandScanner

HandScanner is a Python project designed to scan and analyze hand gestures using computer vision and machine learning techniques. This project leverages OpenCV, MediaPipe, NumPy, and Scikit-learn to achieve real-time hand gesture recognition.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

Follow these steps to set up the project on your local machine.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pablorodri001/HandScanner.git
    cd HandScanner
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - On macOS and Linux:
        
        ```bash
        source venv/bin/activate
        ```

    - On Windows:
        
        ```bash
        .\venv\Scripts\activate
        ```

4. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the dependencies are installed, you can run the main script to start the hand scanner.

```bash
python main.py
