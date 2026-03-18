# 💘 Do You Like Me? — A Simple Question App

A cute little desktop app built with Python and Tkinter that asks one very important question.

## 📸 What It Does

- Displays a centered GUI window with the question **"Do You Like Me?"**
- Offers three buttons: **Yes**, **No**, and **Cancel**
- **Yes** → closes the window and prints a sweet message with a typing effect
- **No / Cancel** → restarts the program (because "no" is simply not an option 😄)

## 🚀 Getting Started

### Prerequisites

- Python 3.x (Tkinter is included in the standard library)

### Run the App

```bash
python main.py
```

## 📁 Project Structure

```
.
└── main.py       # Main application file
```

## 🧩 Features

| Feature | Description |
|---|---|
| Centered window | Opens right in the middle of your screen |
| Typing effect | Terminal response is printed character by character |
| Auto-restart | Pressing No or Cancel relaunches the app |
| Clean UI | Soft background with color-coded buttons |

## 🛠️ How It Works

```
User opens app
     │
     ▼
┌─────────────────────┐
│   Do You Like Me?   │
│  [Yes] [No] [Cancel]│
└─────────────────────┘
     │              │
    Yes           No / Cancel
     │              │
 Print sweet      Restart
  message          app
```

## 💡 Customization

- **Typing speed** — adjust the `delay` parameter in `typing_effect()` (default: `0.05s` per character)
- **Window size** — change `window_width` and `window_height` in `create_window()`
- **Message** — edit the string inside `on_yes()` to say whatever you'd like

## 📄 License

Free to use, share, and spread love. 💕
