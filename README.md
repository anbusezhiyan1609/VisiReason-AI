VisionReason AI: Multimodal Smart Assistant

VisionReason AI is an on-device visual intelligence tool designed to transform static images of retail environments—such as grocery shelves, fridges, or meal plates—into actionable insights. By leveraging state-of-the-art vision-language models, it provides deep scene understanding, moving beyond simple object detection to answer complex nutritional and inventory queries.
🚀 Core Features

Deep Scene Understanding: Moves beyond basic labels to answer complex questions like "Is this meal healthy?" or "What recipes can I make with these ingredients?".

Nutritional Analysis: Identifies food items from images and calculates estimated calorie intake in a structured format.


Retail Intelligence: Capable of expiration tracking, inventory summaries, and OCR-based fine-print reading.



Optimized Performance: Designed for high-speed inference on consumer-grade hardware using 4-bit quantization.
Technical Stack
AI Model: Google Gemini 2.5 Flash (Multimodal)


Framework: Streamlit (Web UI) 

Language: Python


Key Libraries: google-generativeai, Pillow (Image Processing), python-dotenv
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.10 or higher

A Google Gemini API Key (obtainable from Google AI Studio)

Installation
Clone the Repository:

Bash

git clone https://github.com/anbusezhiyan1609/VisiReason-AI.git
cd VisiReason-AI
Install Dependencies:

Bash

pip install -r requirements.txt
Environment Setup: Create a .env file in the root directory and add your API key:

Plaintext

GOOGLE_API_KEY=your_api_key_here
🖥️ Usage
To launch the application, run:

Bash

streamlit run nutri1.py
Upload an image of your food or retail products.

Enter a custom prompt or use the default nutritional analysis.

Click "Tell me the total calories" to receive a structured breakdown of items and their nutritional value.

📅 Development Roadmap
This project was developed over a 7-day intensive sprint:


Day 1-2: Setup inference and defined retail logic for domain-specific prompts.


Day 3-4: Built the data pipeline for OCR testing and developed the Streamlit UI.


Day 5-7: Implemented memory optimization (4-bit quantization) and refined prompt engineering for structured outputs.

👤 Author

Name: ANBUSEZIYAN S 


Course: BE-CSE (AIML), III Year 




Roll No: 2336120002 

Connect: LinkedIn | Email
Screenshots
