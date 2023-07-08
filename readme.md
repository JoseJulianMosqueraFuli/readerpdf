# Text-to-Speech using gTTS in WSL2

This guide will walk you through the process of setting up a text-to-speech program using the Google Text-to-Speech (gTTS) library in Windows Subsystem for Linux (WSL2). We'll be using the Ubuntu distribution as an example, but you can choose any Linux distribution within WSL2.

## Prerequisites

- WSL2 installed and set up on your Windows machine.
- Basic familiarity with the Linux command line.

## Step 1: Set up WSL2

1. Install WSL2 if you haven't already. You can find instructions on the Microsoft website or various online tutorials.

2. Set up a Linux distribution within WSL2. For example, to install Ubuntu, open the Microsoft Store, search for Ubuntu, and follow the installation steps.

## Step 2: Install the necessary packages

1. Open your WSL2 terminal.

2. Update the package lists by running the following command:

   ```bash
   sudo apt update
   ```

3. Install the required packages:
   ```bash
   sudo apt install python3 python3-pip mpg123
   ```

## Step 3: Install gTTS library

- _Optional_: Could be create a venv in your folder:
  ```bash
  python3 -m venv venv
  # Next activate venv:
  source venv/bin/activate
  ```

1. In the WSL2 terminal, install the gTTS library using pip:

   ```bash
   pip3 install gTTS
   ```

## Step 4: Create the text-to-speech script

1. Open a text editor within WSL2, such as Nano or Vim.

2. Create a new Python script. For example, you can name it `tts.py`.

3. Paste the following code into the script:

   ```python
   from gtts import gTTS
   import os

   def text_to_speech(text, filename):
       tts = gTTS(text)
       tts.save(filename)

   if __name__ == "__main__":
       text = "Hello, World!"  # Replace with your desired text
       filename = "output.mp3"  # Output file name

       text_to_speech(text, filename)
       os.system("mpg123 " + filename)
   ```

4. Modify the `text` variable with the desired text you want to convert to speech.

5. Save the file and exit the text editor.

## Step 5: Run the text-to-speech program

1. In the WSL2 terminal, navigate to the directory where you saved the `tts.py` file.

2. Run the script using the following command:

   ```bash
   python3 main.py
   ```

3. The program will generate an MP3 file with the speech output and play it using the `mpg123` command.

Congratulations! You have successfully set up a text-to-speech program using the gTTS library in WSL2. Feel free to modify the script and experiment with different texts and options to suit your specific needs.
