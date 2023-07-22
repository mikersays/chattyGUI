import openai
import time
import threading
import os
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

# Set up your API key. Replace the entire <API key> string with your OpenAI API key.
openai.api_key = "<API key>"

# Function to generate a response using GPT-4
def generate_response(prompt, messages, max_tokens=5000, temperature=1):
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        top_p=1,
    )
    messages.append({"role": "assistant", "content": response.choices[0].message['content']})
    return response.choices[0].message['content']

# Function to call GPT-4 API without a loading animation
def call_gpt(prompt, messages, conversation_text, output_file_path, loading_label):
    response = generate_response(prompt, messages)

    # Hide the loading text
    loading_label.config(text="")

    # Append the AI's response to the conversation text widget
    conversation_text.insert(tk.END, "AI: ", "ai")
    conversation_text.insert(tk.END, response + "\n")
    with open(output_file_path, "a") as output_file:
        output_file.write(f"AI: {response}\n\n") 

# Function to get the user's desktop path
def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

# Function to read the instruction from an external file
def read_instruction_from_file(file_path):
    with open(file_path, "r") as file:
        instruction = file.read().strip()
    return instruction

# Main function to start the chatbot
def chatbot():
    print("Ask me anything! Type 'q' to exit.")
    print("----------------------------------")
    user_input = ""

    # Prepare the output file
    desktop_path = get_desktop_path()
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"chat_output_{current_time}.md"  # Changed the file extension to ".md"
    output_file_path = os.path.join(desktop_path, output_filename)

    system_instruction = read_instruction_from_file("AIpersona.txt")
    messages = [{"role": "system", "content": system_instruction}]
    
    with open(output_file_path, "w") as output_file:
        while user_input.lower() != "q":
            user_input = input("User: ")  # Replace this line

            if user_input.lower() != "q":
                output_file.write(f"User: {user_input}\n\n")  # Added an extra line

                print("AI: ", end="", flush=True)
                response = call_gpt_with_spinner(user_input, messages)
                print(response)

                output_file.write(f"AI: {response}\n\n")  # Added an extra line

    print(f"Chatbot conversation saved to: {output_file_path}")

if __name__ == "__main__":
    chatbot()
