# 🥫 Food Bank Registration Checker

This small Python utility automatically checks the [SSF Food Bank webpage](https://ssfinc.ca/food-bank) for the weekly registration link (hosted on JotForm). Once the link becomes available, the program will automatically open it in your default browser.

---

## 🚀 Features

- Automatically checks for the “Click here to register” JotForm link
- Randomized user-agent and delay to mimic human behavior
- Automatically opens the registration page once found
- Lightweight and easy to use
- Works even on systems without Python (via `.exe`)

---

## 🖥️ How to Use

### ✅ Option 1: Run the `.exe` directly (no Python required)

1. Go to the `dist/` folder or download `goForFoodBank.exe`.
2. Double-click `goForFoodBank.exe` to launch it.
3. When prompted, type `ok` and press Enter.
4. The program will begin checking the SSF Food Bank page every 0.5–2 seconds.
5. Once the registration link is found, it will open in your browser.
6. Press `Ctrl+C` to manually stop the program at any time.

---

### 🐍 Option 2: Run the Python script locally

#### Requirements:
- Python 3.7 or later installed
- Packages: `requests`, `beautifulsoup4`

#### Steps:

1. Open a terminal and navigate to the script folder.
2. Install the required packages:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the script:
   ```bash
   python goForFoodBank.py
   ```
4. Type `ok` to start checking.

---

## 📁 File Structure

```
FoodBankChecker/
├── goForFoodBank.py        # Source code
├── goForFoodBank.exe       # Compiled executable (in dist/)
├── README.md               # You are here
```

---

## 🛑 Notes

- You must be connected to the Internet for this program to work.
- Make sure the SSF Food Bank page has the registration link posted when the program is running.
- This tool is designed for personal use and does not bypass any restrictions or forms.

---

## 📄 License

This tool is for personal use only. Redistribution or modification is not allowed without permission.

