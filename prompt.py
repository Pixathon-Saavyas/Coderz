import os
import google.generativeai as genai


def generate_summary(story):
    # Set your API key
    os.environ['YOUR_API_KEY'] = "AIzaSyCCgV_4zM-zQQfui-vs8QNZ8LKyVVD5k4Y"

    # Configure Gemini AI
    genai.configure(api_key=os.environ['YOUR_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')

    # Concatenate static text with the story
    static_text = "i want to break this story into multiple parts so tht i can make photo give prompts such that it gives each disciption of photo how it should be ,each prompts ending with [&&&] and say last prompt as last prompt"
    content = static_text + story

    # Generate content using Gemini AI with the concatenated text
    response = model.generate_content(content)

    # Return the generated content
    return response.text