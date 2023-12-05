import tkinter as tk
from googletrans import Translator
from gtts import gTTS
import pygame

pygame.mixer.init()

def translate_text():
    translator = Translator()
    source_text = source_text_entry.get()
    source_language = source_lang_entry.get().lower()
    target_languages = [lang.strip() for lang in target_lang_entry.get().split(',')]

    result_text.delete(1.0, "end")

    for target_language in target_languages:
        if target_language:
            translated = translator.translate(source_text, src=source_language, dest=target_language)
            result_text.insert("end", f"Speech ({target_language}): {translated.text}\n")

            tts = gTTS(text=translated.text, lang=target_language)
            tts.save("temp.mp3")
            pygame.mixer.music.load("temp.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(pygame.USEREVENT)

window = tk.Tk()
window.title("Text Translator with Text-to-Speech")
window.configure(bg='white')  # Set the background color to a minimal color like white

title_label = tk.Label(window, text="Text Translator with Text-to-Speech", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

input_frame = tk.Frame(window, bg='white')
input_frame.pack(padx=10, pady=10)

source_text_label = tk.Label(input_frame, text="Enter a word or sentence:")
source_text_label.pack()

source_text_entry = tk.Entry(input_frame, bg='white', fg='black')
source_text_entry.pack()

source_lang_label = tk.Label(input_frame, text="Enter the source language (e.g., 'en' for English):")
source_lang_label.pack()

source_lang_entry = tk.Entry(input_frame, bg='white', fg='black')
source_lang_entry.pack()

target_lang_label = tk.Label(input_frame, text="Enter the target languages (comma-separated):")
target_lang_label.pack()

target_lang_entry = tk.Entry(input_frame, bg='white', fg='black')
target_lang_entry.pack()

translate_button = tk.Button(window, text="Translate and Speak", command=translate_text, bg='blue', fg='white', font=("Arial", 12))
translate_button.pack(pady=10)

result_text = tk.Text(window, height=10, width=40, bg='white', fg='black', font=("Arial", 12))
result_text.pack()

window.mainloop()
