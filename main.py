import speech_recognition as sr
import pyttsx3
import time
import keyboard

engine = pyttsx3.init()

def speak(text):
    engine.setProperty('rate', 130)  # настройка скорости речи
    engine.setProperty('volume', 1)  # настройка громкости речи
    voices = engine.getProperty('voices')
    male_voice = None
    for voice in voices:
        if "male" in voice.name.lower() and "low" in voice.name.lower():
            male_voice = voice
            break
    if male_voice:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def classify_response(response):
    # Удаляем ключевое слово "напиши" из ответа
    if "напиши" in response.lower():
        new_sss = response.lower().replace("напиши", "").strip()
        keyboard.write(new_sss, 0.1)
        time.sleep(0.1)
        print(response.lower())
        return "хорошо"

def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Говорите:")
        audio = r.listen(source)
    try:
        # Преобразуем голосовую команду в текст
        response = r.recognize_google(audio, language='ru-RU')
        return response
    except sr.UnknownValueError:
        print("Я не могу распознать вашу речь")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи: {0}".format(e))

# Запуск программы
while True:
    response = recognize_speech()

    if response:
        reply = classify_response(response)
        speak(reply)
        time.sleep(1)
