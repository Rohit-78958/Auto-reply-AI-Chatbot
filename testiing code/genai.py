import google.generativeai as genai
import chat_history

genai.configure(api_key="-4")

        # Create a model (e.g., 'gemini-1.0-pro-latest')
model = genai.GenerativeModel('gemini-1.0-pro-latest')
# model = genai.GenerativeModel('gemini-1.5-flash')

content = "You are Rohit who has just passed out of btech and soon going to join his job as a software engineer, you talk in hindi and english mix and you are jolly kind of person. Analyse this chat history and give the response to the sender as Rohit. Give reply to last message" + chat_history.chat_history

response = model.generate_content(content)
# speak(response.text)
print(response.text)