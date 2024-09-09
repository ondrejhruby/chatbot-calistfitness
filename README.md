# CalistFitness Chatbot

The CalistFitness Chatbot is a Rasa-based conversational assistant designed to provide personalized fitness coaching and support for clients. It combines the principles of calisthenics and traditional fitness to deliver unique, tailored advice to help users achieve their health and fitness goals. The bot answers frequently asked questions, offers training and nutrition guidance, and provides 24/7 support to enhance the coaching experience.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Skills Learned](#skills-learned)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)

## Features

- **Personalized Fitness Coaching**: Offers guidance on fitness routines and meal plans based on individual goals and available equipment.
- **Calendly Integration**: Persuades potential clients to book a consultation call.
- **24/7 Client Support**: Provides continuous assistance via automated responses and personalized feedback.
- **Hybrid Training Insights**: Explains the benefits of combining calisthenics and traditional fitness for optimal results.
- **FAQs Handling**: Answers common questions about training, nutrition, subscriptions, and coaching services.
- **Progress Tracking**: Offers feedback on exercises and nutrition adherence, encouraging clients to stay on track.

## Skills Learned

- **Rasa Framework**: Developing chatbots with Rasa, including NLU training, dialogue management, and custom action development.
- **Natural Language Processing (NLP)**: Extracting intents and entities from user input to deliver accurate and relevant responses.
- **Model Explainability and Interpretability**: Insights into how the bot interprets user intents and entities.
- **Optimization and Hyperparameter Tuning**: Customizable models for enhanced accuracy and performance.
- **Python Programming**: Writing custom actions and backend logic to enhance the bot’s capabilities.
- **Conversational Design**: Creating engaging conversation flows that cater to fitness enthusiasts.
- **Problem Solving**: Debugging and troubleshooting to ensure a seamless user experience.
- **API Integration**: Linking the bot with external platforms like WhatsApp for communication and client interaction.
- **Fitness and Nutrition Knowledge**: Integrating domain-specific knowledge into the bot to provide expert advice.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/calistfitness-chatbot.git
    ```
2. Navigate into the project directory:
    ```bash
    cd calistfitness-chatbot
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Train the chatbot:
    ```bash
    rasa train
    ```
6. Run the action server:
    ```bash
    rasa run actions
    ```
7. Run the chatbot:
    ```bash
    rasa run
    ```

## Future Improvements

- **Fix Current Errors**
- **Advanced Personalization**: Incorporate user analytics to further personalize advice based on past interactions and progress.
- **Voice Interaction**: Enable voice command capabilities to make the chatbot accessible in hands-free scenarios.
- **Enhanced NLP Models**: Integrate advanced language models for more sophisticated responses and understanding of complex queries.

## How to Contribute

Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request. For significant changes, please open an issue first to discuss what you would like to change.


