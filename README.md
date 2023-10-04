# chatbot_assessment
This is a simple chat application that allows users to interact with a chatbot about different fruits using a web interface. The chatbot is powered by a Flask backend, and the template is built using HTML and JavaScript.

## Usage

1. Make sure you have Python (version 3.11+) and pip installed on your system.

2. Install the required packages by running the following command:
   
   ```bash
   pip install -r requirements.txt

3. Run the Flask backend:

    ```bash
    python api.py

4. Open the url: localhost:5000 in a web browser to access the chat application.

5. Type a message in the input field, click "Send," and the chatbot will respond accordingly.

## Project Structure

1. api.py: The Flask backend code.

2. index.html: The flask template.

3. requirements.txt: Contains the required Python packages.

## Explanation

1. Rule-Based Chatbot using Intents:

In the rule-based mode, the chatbot recognizes intents based on predefined rules and responds accordingly. The intents are predefined categories of user input, each associated with a set of example messages and possible responses. Here's how it works:

- Intent Recognition:
The chatbot processes the user's question and tries to match it with the predefined intents. It checks if any of the intents' example user messages match the question.

- Matching Intent:
The chatbot might recognize that the user is seeking a greeting or expressing gratitude.

- Response Generation:
Based on the recognized intent, the chatbot selects an appropriate response associated with that intent. It would generate a response that responds with a warm greeting or an acknowledgement of the user's thanks.

2. NLTK-Based "Smart" Chatbot using TF-IDF:

In the "smart" chatbot mode, the application uses Natural Language Processing (NLP) techniques, specifically TF-IDF (Term Frequency-Inverse Document Frequency), to derive context from the user's question and generate a more contextually relevant response. Here's how it works for the question:

- Intent Recognition (Context Derivation):
The chatbot analyzes the user's question using NLTK (Natural Language Toolkit) to understand the context and meaning. It may utilize techniques like tokenization and lemmatization to process the input.

- TF-IDF and Context Comparison:
The chatbot uses TF-IDF on a pre-defined text corpus (e.g., fruit.txt) to calculate the importance of words in the user's question compared to the text corpus. This helps in understanding the context and extracting relevant information.

###
A version of this app is deployed on an ec2 instance at ip: 44.202.134.5 but the results can be unpredictable. In my experiments, I was able to reliably connect to this instance on a phone but not using my PC.
###
- Matching Context and Generating Response:
By comparing the TF-IDF vectors of the user's question with the pre-defined text corpus, the chatbot identifies the most relevant information and generates a response that provides a brief explanation of how intent recognition and response generation work.

In summary, the rule-based mode relies on predefined intents and rules to recognize and respond to user input, while the NLTK-based "smart" mode uses NLP techniques like TF-IDF to derive context from the question and generate responses based on the analyzed context and a pre-defined text corpus.
