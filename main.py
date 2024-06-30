import pyautogui
import pyperclip
import time
import google.generativeai as genai

genai.configure(api_key="-4")

# Create a model (e.g., 'gemini-1.0-pro-latest')
# model = genai.GenerativeModel('gemini-1.5-flash')
model = genai.GenerativeModel('gemini-1.0-pro-latest')


def is_last_response_from_sender(chat_history, sender="Shalu"):
    # Split the chat history into individual messages
    messages = chat_history.split("/2024]")
    print(messages)
    # Extract the last message (assuming it's the most recent)
    last_message = messages[-1]
    
    # Check if the last message contains "R B Ashwin"
    return sender in last_message


pyautogui.click(459, 747)
time.sleep(2)

while True:
  # Move to position (419, 183) and drag the mouse to (1302, 675)
  # pyautogui.click(421, 189)
  pyautogui.moveTo(421, 189)
  pyautogui.dragTo(434, 714, duration=2)

  # Copy the selected text (you may need to adjust this based on your application)
  pyautogui.hotkey("ctrl", "c")
  time.sleep(1)

  # Get the copied text from the clipboard
  current_chat = pyperclip.paste()
  time.sleep(1)

  # print("Copied text:", current_chat)
  # print(current_chat)
  # print(is_last_response_from_sender(current_chat))

  if is_last_response_from_sender(current_chat):
    content = "You are Rohit who has just passed out of btech and soon going to join his job as a software engineer, you chat in hindi and english mix, that is 'hinglish' and you are jolly kind of person who loves to live with his family. Analyse this chat history and behave as Rohit and give the response to the sender as Rohit. Give reply to last message(Just give reply not the timings , date and name that are before colon in chat history)" + current_chat

    response = model.generate_content(content)
    # print(current_chat,"\n" ,response.text)

    # Click at position (567, 698)
    pyautogui.click(567, 698)

    # Paste the generated response
    pyperclip.copy(response.text)
    pyautogui.hotkey("ctrl", "v")

    # Press the Enter key
    pyautogui.press("enter")

    print("Response sent successfully!")

  #wait for sender to send message
  pyautogui.click(567, 698)
  time.sleep(8)  

  