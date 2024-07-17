Tony - Voice Assistant


Tony is a Python-based voice assistant that utilizes various libraries to perform tasks through voice commands. It leverages speech recognition, text-to-speech capabilities, and external APIs to provide functionality such as playing YouTube videos, searching the web, fetching information from Wikipedia, telling jokes, and more.

Features

Voice Recognition: Tony listens for commands using the microphone and recognizes speech using Google's Speech Recognition API.

Text-to-Speech: Responses and information are conveyed back to the user audibly using the pyttsx3 library.

Web Interaction: Searches the web using pywhatkit and fetches summaries from Wikipedia.

Entertainment: Plays YouTube videos based on user commands.

Utility Commands: Provides current time, shutdown scheduling, joke telling, and handles basic inquiries.


Usage

Installation:

Ensure you have Python 3.x installed.
Install required packages using pip install -r requirements.txt.
Setup:

Run the script tony.py.
Tony will greet you and await commands prefixed with "Tony".
Commands:

Play [song name]: Plays a song on YouTube.

Search [query]: Searches the web for the specified query.

Time: Tells the current time.

Who is [person]: Provides a summary from Wikipedia about the person.

Joke: Tells a random joke.

Power off: Schedules the system to shut down in 1 minute.

Cancel: Cancels a previously scheduled shutdown.

Exit: Terminates the program.


Contributing

Feel free to contribute by forking the repository, making changes, and submitting a pull request. You can enhance functionality, improve speech recognition accuracy, add new features, or fix bugs.


Make sure to adjust paths and details as per your project structure and specific implementation. This README provides an overview of what the project does, how to use it, how to contribute, and details about its license, which are essential for any GitHub repository.
