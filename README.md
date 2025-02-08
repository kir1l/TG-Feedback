# Feedback bot for Telegram

A scalable Telegram bot built with [Aiogram 3](https://docs.aiogram.dev/) and Python.  
This bot provides:

- A main inline menu with informational sections,
- A feedback mechanism where users can send messages to administrators,
- An administrative interface (broadcasting, replying to user feedback),
- A structured and maintainable codebase using best practices:
  - FSM (Finite State Machine) for managing conversation flow,
  - Centralized routing,
  - SQLite database for data persistence,
  - Extended logging (file rotation + console).

## Features

1. **Inline Menu**  
   The bot’s main menu is displayed via inline keyboard buttons (e.g., “Info,” “News,” “Feedback,” “Subscribe”).

2. **Feedback**  
   Users can send feedback directly to administrators. Administrators can reply to user feedback via inline buttons.

3. **Admin Commands**

   - **Broadcast**: Send a message to all subscribers (stored in the SQLite database).
   - **Reply**: Quickly reply to feedback, and the response goes directly to the user.

4. **Multiple Admins**  
   You can configure more than one administrator (by listing their Telegram user IDs).

5. **Logging**  
   Both console and file logging are supported with rotation.

6. **Scalable Structure**  
   The project is split into logical modules (handlers, keyboards, states, etc.) for easy maintenance and further extensions.

## File & Folder Structure

A simplified overview:

```
project/
├── bot/
│   ├── __init__.py
│   ├── config.py               # Bot configuration (token, admins, DB path, etc.)
│   ├── db.py                   # SQLite database operations
│   ├── router.py               # Centralized registration of all handlers
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── start.py            # /start command
│   │   ├── info.py             # Info callback handler
│   │   ├── news.py             # News callback handler
│   │   ├── feedback.py         # Feedback functionality
│   │   └── admin.py            # Admin commands (reply, broadcast)
│   ├── keyboards/
│   │   ├── __init__.py
│   │   └── main_menu.py        # Inline keyboard for the main menu
│   ├── states/
│   │   ├── __init__.py
│   │   ├── feedback_states.py  # Feedback states
│   │   ├── admin_states.py     # Admin reply states
│   │   └── broadcast_states.py # Broadcast states
│   └── utils/
│       ├── __init__.py
│       └── logger.py           # Logging configuration
├── data/
│   └── bot.db                  # SQLite DB file
├── logs/
│   └── bot.log                 # Log file with rotation
├── main.py                     # Entry point (initialize bot, register handlers, run polling)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Installation

### Local Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure `bot/config.py`:**

   - Add your Telegram bot token.
   - Adjust `ADMIN_IDS` to include the Telegram user IDs of admins.
   - Confirm the path to `DB_PATH`.

5. **Initialize the SQLite database (if needed):**

   ```bash
   python -c "from bot.db import init_db; init_db()"
   ```

6. **Run the bot locally:**
   ```bash
   python main.py
   ```
   The bot will start polling and respond to messages in Telegram.

## Deployment on an Ubuntu Server

Below is a simplified process for deploying on an Ubuntu server.

1. **Server Preparation**

   - Ensure Python 3.8+ is installed (`sudo apt-get update && sudo apt-get install python3 python3-venv -y`).
   - Install git if not already present (`sudo apt-get install git -y`).

2. **Clone/Update Repository & Install Dependencies**  
   Use the provided `deploy.sh` script (see below example) or handle manually:

   ```bash
   # Example usage if you have the deploy.sh script
   chmod +x deploy.sh
   ./deploy.sh
   ```

3. **Systemd Service (Optional)**  
   Create a systemd unit file to run your bot as a service:

   ```bash
   sudo nano /etc/systemd/system/telegram-bot.service
   ```

   Example contents:

   ```ini
   [Unit]
   Description=Telegram Bot Service
   After=network.target

   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/opt/telegram-bot
   ExecStart=/opt/telegram-bot/venv/bin/python main.py
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

   Reload systemd and enable/start:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable telegram-bot
   sudo systemctl start telegram-bot
   ```

4. **Logs**  
   By default, logs are written to `logs/bot.log`. Check logs for troubleshooting:
   ```bash
   tail -f /opt/telegram-bot/logs/bot.log
   ```
   Or via systemd:
   ```bash
   journalctl -u telegram-bot -f
   ```

## Usage

- **Start command**: `/start`  
  Sends a welcome message with an inline keyboard to choose among “Info,” “News,” “Feedback,” and “Subscribe.”

- **Feedback**:  
  Users can submit feedback, which is forwarded to all admins. Admins can reply from within the bot UI.

- **Admin Commands** (only accessible by users in `ADMIN_IDS`):
  - **Reply**: Inline button “Reply” attached to each feedback message.
  - **Broadcast**: `/broadcast` sends a message to all stored subscribers in the DB.

## Contributing

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Open a pull request describing the changes you made.

## License

This project is distributed under a license of your choice (MIT, Apache, etc.).  
Include a proper `LICENSE` file in the repository if needed.

**Questions / Suggestions?**  
Feel free to open an issue and create PR.
