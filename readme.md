# Rule-Based AI Chatbot

## Project Overview

This is a simple rule-based chatbot developed as part of the DecodeLabs Industrial Training Kit (Project 1). The chatbot responds to predefined user inputs using if-else logic and runs in a continuous loop until the user decides to exit.

The chatbot demonstrates fundamental AI concepts through explicit programmatic decision-making, without machine learning or deep neural networks.

## Features

### Core Functionality

- **Greeting Recognition:** Responds to various greeting inputs (hello, hi, hey, good morning, greeting, bonjour)
- **Exit Commands:** Recognizes and handles exit requests gracefully (bye, quit, exit, au revoir, goodbye, see you later, later)
- **Weather Information:** Provides weather responses based on user queries (today, tomorrow, or general)
- **Personal Questions:** Answers basic questions like "How are you?" and "What's your name?"
- **Continuous Loop:** Keeps the conversation running until the user exits
- **Random Responses:** Uses random selection to provide varied responses from predefined options

### Technical Highlights

- Control flow using while loops and if-else statements
- Decision-making logic based on user input
- Dictionary data structures for organized response management
- Case-insensitive input handling
- Unrecognized input handling with helpful prompts

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only the built-in `random` module)

## Usage

### Running the Chatbot

1. Navigate to the directory containing the chatbot script
2. Run the script using Python:
```bash
python chatbot.py
```

3. The chatbot will display:
```
Welcome to the chatbot py

Type 'exit' to end the conversation

BOT: How can I help you?
You: 
```

### Example Conversation

```
Welcome to the chatbot py

Type 'exit' to end the conversation

BOT: How can I help you?
You: hello
BOT: Hi there!

BOT: How can I help you?
You: how are you?
BOT: I am fine, how are you?

BOT: How can I help you?
You: what's your name?
BOT: My name is rule-based chatbot

BOT: How can I help you?
You: what's the weather today?
BOT: It's sunny today.

BOT: How can I help you?
You: will it rain tomorrow?
BOT: It will be rainy tomorrow.

BOT: How can I help you?
You: exit
BOT: See you later!
```

## Code Structure

### Dictionaries

**greeting** - Set of recognized greeting inputs
```python
greeting = {"hello", "hi", "hey", "good morning", "greeting", "bonjour"}
```

**greeting_response** - Random greeting responses
```python
greeting_response = {"Hello! How can I help you today?", "Hi there!", "What's up?"}
```

**exit_commands** - Recognized exit commands
```python
exit_commands = {"bye", "quit", "exit", "au revoir", "goodbye", "see you later", "later"}
```

**exit_msg** - Random exit messages
```python
exit_msg = {"Goodbye! Have a great day!", "See you later!", "Bye!"}
```

### Main Loop

The main while loop performs the following steps:

1. Accepts user input
2. Converts input to lowercase for case-insensitive matching
3. Checks input against defined conditions
4. Provides appropriate response
5. Continues until exit command is received

### Condition Handling

- **Greetings:** Matches any greeting and returns a random greeting response
- **How are you:** Responds to personal questions
- **What's your name:** Identifies the bot
- **Weather:** Uses nested conditions to handle "today", "tomorrow", or general weather queries
- **Exit:** Terminates the program with a random farewell message
- **Default:** Handles unrecognized input with helpful guidance

## Skills Demonstrated

### Programming Concepts

- Control Flow: while loops, if-elif-else statements
- Data Structures: Sets and Lists
- Input/Output: user input handling and console output
- String Operations: case conversion, string matching, string concatenation
- Random Selection: using the random module for varied responses

### AI Concepts

- Rule-Based Decision Making: Explicit rules determine responses
- Conversational Flow: Managing multi-turn dialogue
- Natural Language Processing Basics: Input parsing and pattern matching
- State Management: Continuous conversation state through loops

## Customization

### Adding New Greetings

To add new greeting patterns, edit the greeting set:
```python
greeting = {"hello", "hi", "hey", "good morning", "greeting", "bonjour", "howdy", "g'day"}
```

And add corresponding responses to greeting_response:
```python
greeting_response = {"Hello! How can I help you today?", "Hi there!", "What's up?", "Howdy!"}
```


## Limitations

- Responds only to predefined rules and inputs
- Does not learn from conversations
- Cannot handle complex or context-dependent queries
- No natural language understanding beyond keyword matching
- Limited to single-topic responses per query
- No memory between sessions
- No real data sources for weather or other dynamic information


## File Structure

```
rule-based-chatbot/
├── chatbot.py          # Main chatbot script
├── README.md           # This file
```

## Running the Tests

To verify the chatbot works correctly, test these scenarios:

1. Greeting recognition: Type "hello", "hi", "hey", "good morning"
2. Exit functionality: Type "exit", "bye", "quit"
3. Personal questions: Ask "how are you?" and "what's your name?"
4. Weather queries: Ask "what's the weather today?" and "will it rain tomorrow?"
5. Unrecognized input: Type gibberish to see the default response

## Troubleshooting

### ChatBot doesn't respond

- Ensure input is typed correctly
- Check that you're not using special characters that might break matching
- Verify the Python script is running without errors

### Exit command doesn't work

- Ensure you typed an exact match from the exit_commands set
- Try typing just "exit" if other variations don't work
- Check for extra spaces or punctuation

## Notes

- This is a beginner-level project designed to teach fundamental programming concepts
- The rule-based approach does not use machine learning or neural networks
- Focus is on control flow, logic, and decision-making
- Treat unexpected outputs as learning opportunities
- Experiment with unique solutions and custom enhancements