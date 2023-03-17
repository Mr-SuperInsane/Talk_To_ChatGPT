import speech_recognition as sr
import openai
import pyttsx3

openai.api_key = 'openai_api_key'

r = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print('--speak to chatgpt')
    audio = r.listen(source)
try:
    user_message = r.recognize_google(audio, language='ja-JP')
    print(' < YOU > ')
    print(user_message)
    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {'role': 'user', 'content': user_message}],
                    temperature=0.0,
    )
    response = response['choices'][0]['message']['content']
    print(' < ChatGPT > ')
    print(response)
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

except:
    print('--sorry, inaudible--')
