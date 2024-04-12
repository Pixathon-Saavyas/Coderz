from prompt2image import save_images_from_query
from prompt import generate_summary
import requests
import io
from PIL import Image
import os

story = "In a kingdom far away, there lived a wise wizard named Merlin. He possessed great magical powers and was revered by all who knew him. One day, a young adventurer named Arthur sought Merlin's help in his quest to become the rightful king of the land. Together, they embarked on a journey filled with challenges and trials, facing mythical creatures and dark sorcery. Through bravery, wisdom, and friendship, Arthur and Merlin overcame all obstacles, and Arthur eventually ascended to the throne, fulfilling his destiny as the legendary King Arthur."
generated_summary = generate_summary(story)
print(generated_summary)

parts = story.split("&&&")

for i, part in enumerate(parts, 1):
    try:
        generated_summary = generate_summary(part)
        save_images_from_query(generated_summary, folder='images', filename_prefix=f'part_{i}_image')
        
        # Check if it's the last prompt
        if i == len(parts):
            break
    except Exception as e:
        print(f"An error occurred while processing part {i}: {e}")
        break
