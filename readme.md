<p align="center">
  <img src="https://github.com/jthom2/langchain-weather-chatbot/assets/134821369/9eb6d14f-49dd-43c9-a16d-3aaf398cf50e" alt="Weather Chatbot">
</p>


# Weather Chatbot

## Overview
This project is a chatbot designed to provide weather updates to users. It's built using Langchain for the AI component and Streamlit for the web interface. The chatbot can process user queries about the weather and generate responses using external APIs.

## Features
- AI-driven chatbot for weather information.
- User-friendly web interface built with Streamlit.
- Supports multiple languages.
- Customizable traits for the chatbot assistant.

## Installation

Before installing, ensure you have Python installed on your system.

1. **Clone the Repository**
- Clone this repository to your local machine using:
     `git clone https://github.com/jthom2/langchain-weather-chatbot`

2. **Install Dependencies**
- Navigate to the cloned repository and install the required Python packages:
    `pip install -r requirements.txt`

3. **Setting Up Environment Variables**
Set up the necessary environment variables for OpenAI and DataForSeoAPI:
- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATAFORSEO_LOGIN`: Your DataForSeo API login.
- `DATAFORSEO_PASSWORD`: Your DataForSeo API password.

These can be set in your environment or using a `.env` file.

4. **Run the Application**
- Start the Streamlit app:
    `streamlit run main.py`

## Usage
- Launch the chatbot interface in your web browser.
- Select your desired language and assistant traits from the sidebar.
- Type your weather-related queries in the chat and receive real-time responses.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- Langchain for the AI framework.
- OpenAI for the GPT model used in generating responses.
- DataForSeo for providing weather data APIs.
- Streamlit for the web interface framework.
