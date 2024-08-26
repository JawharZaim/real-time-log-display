# real-time-log-display

`real-time-log-display` is a web application built with FastAPI that provides real-time viewing of log files. This project allows users to:

- **Submit Project Names:** Enter a project name to view its corresponding log file.
- **View Logs:** Display the last 100 lines of the selected log file.
- **Live Updates:** Receive live updates of the log file content using WebSockets, ensuring that changes are reflected in real-time without needing a manual refresh.
- **Dynamic Log File Selection:** Select log files from a predefined directory and view their contents.
- **Customizable Line Count:** Set the number of lines to display, with a default value of 100.

## Features

- **Real-Time Log Viewing:** Uses WebSockets to stream log updates live.
- **User-Friendly Interface:** Simple and intuitive interface for selecting projects and viewing logs.
- **Dynamic File Listing:** Automatically fetches and displays available log files from a specified directory.
- **Responsive Design:** Ensures a good user experience across different devices.

## Technologies Used

- **FastAPI:** For building the web application and WebSocket communication.
- **HTML/CSS/JavaScript:** For the front-end user interface.
- **WebSockets:** For real-time updates of log files.

## Installation

To run this project locally, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/real-time-log-display.git
cd real-time-log-display
pip install -r requirements.txt
uvicorn main:app --reload
