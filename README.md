# Amazon Automation Assessment

An automated test suite built with **Python** and **Playwright** to search for products (iPhone and Galaxy devices) and add them to the cart on Amazon.com. 

This project fulfills all assessment requirements, including **parallel execution** of test cases.

## 📁 Project Structure
- `tests/test_amazon.py`: Contains the core automation logic and Pytest configurations.
- `requirements.txt`: Lists the Python dependencies required to run the project.
- `*_cart_proof.png`: Automated screenshots verifying the script reached the final cart state.

## ⚙️ Prerequisites
Ensure you have the following installed on your machine:
- Python 3.8+
- Git

## 🚀 Setup & Installation Instructions

**1. Clone the repository**
- git clone `(https://github.com/rahuldhama/amazon_automation.git)`
-`cd amazon_automation`

**2. Create a virtual environment**

`python -m venv venv`

**3. Activate the virtual environment**

Windows (Command Prompt): `venv\Scripts\activate.bat`
Windows (PowerShell): `\venv\Scripts\activate`
Mac/Linux: `source venv/bin/activate`

**4. Install project dependencies**

`pip install -r requirements.txt`

**5. Install Playwright browsers**

`playwright install chromium`

**▶️ Running the Tests**

To run the test cases in parallel (simultaneously) with the browser visible, run the following command:

`python -m pytest -n 2 --headed`

To view the detailed print logs upon completion:
Because the parallel runner hides real-time console output, append the -rP flag to see the [SUCCESS] logs after the test finishes.

`python -m pytest -n 2 --headed -rP`


