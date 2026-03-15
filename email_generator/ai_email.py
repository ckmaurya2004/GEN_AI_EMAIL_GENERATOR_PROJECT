import os
from google import genai
from django.conf import settings
# from .config import GEMINI_API_KEY
from .models import GeneratedEmail
from datetime import datetime

# AIzaSyCesIz0ZW3D8Zb3EwR-MHO_emd-CASDl7s
client = genai.Client(api_key=settings.GEMINI_API_KEY)

def generate_email(email_type, receiver, purpose, sender):

    prompt = f"""
    Write a professional email.

    Email Type: {email_type}
    Receiver: {receiver}
    Purpose: {purpose}
    Sender: {sender}

    Instructions:
    - Generate a clean professional email.
    - Include Subject line.
    - Write the email in 2–3 proper paragraphs.
    - Do NOT write every sentence on a new line.
    - Use proper email format (Greeting, Body, Closing).
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    email_data = GeneratedEmail(user=sender,email_type = email_type,receiver= receiver,purpose = purpose,generated_email =response.text,created_at =datetime.now() )
    email_data.save()
    return response.text