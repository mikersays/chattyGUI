# chattyGUI

## Introduction

This application is a simple text-based chatbot that uses OpenAI's GPT-4 model to generate responses to user input. It utilizes the Tkinter library in Python to provide a basic graphical user interface.

## Features

- A text-based interface where the user can enter their messages.
- Real-time response generation using the GPT-4 model.
- Color-coded messages for the user (blue) and the AI (red) for easy distinction.
- Word wrapping to ensure that messages do not get cut off at the window edge.
- Messages from both the user and the AI are saved to a markdown (.md) file on the user's desktop.

## Prerequisites

- Python 3.6 or higher.
- OpenAI Python library.
- Tkinter Python library.

## Setup

1. Install the required Python libraries with pip:

    ```
    pip install openai
    pip install tkinter
    ```

2. Clone this repository or download the Python file.

3. Replace the `<API key>` string in the script with your OpenAI API key.

## Running the Application

Run the script using a Python interpreter. A window titled "Chatty" will appear. You can type your message in the input field at the bottom of the window and press Enter to send it. The chatbot will then generate a response, which will appear in the chat area.

## Application Structure

The `chatbot` function is the main function that starts the chatbot. It prepares the output file, creates the GUI application window, and starts the GUI event loop.

The `generate_response` function is used to generate a response from the GPT-4 model based on the user's input.

The `call_gpt` function calls the `generate_response` function and returns the response.

The `get_desktop_path` function is used to get the user's desktop path, which is used to save the output markdown file.

The `handle_enter_pressed` function is bound to the Enter key. It gets the user's input, clears the input field, and updates the GUI to show the user's message and the AI's response.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
