import os
import google.generativeai as genai


def generate_summary(story, static_text):
    # Set your API key
    os.environ['YOUR_API_KEY'] = "AIzaSyCCgV_4zM-zQQfui-vs8QNZ8LKyVVD5k4Y"

    # Configure Gemini AI
    genai.configure(api_key=os.environ['YOUR_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')

    # Concatenate static text with the story
    content = static_text + story

    # Generate content using Gemini AI with the concatenated text
    response = model.generate_content(content)

    # Return the generated content
    return response.text

# Take user input for static_text
static_text = input("Enter the static text: ")

# Example usage
story = "Once upon a time..."
summary = generate_summary(story, static_text)
print(summary)