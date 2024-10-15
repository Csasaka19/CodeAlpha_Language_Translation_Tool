import tkinter as tk
from tkinter import ttk, Frame, Label, Text, Button, RAISED
from googletrans import Translator

translator = Translator()

def translate_text():
    input_lang_code = language_codes[input_language.get()]
    output_lang_code = language_codes[output_language.get()]
    text_to_translate = text_input.get("1.0", tk.END).strip()

    if text_to_translate:
        try:
            # Use Google Translator to translate the text
            translated = translator.translate(text_to_translate, src=input_lang_code, dest=output_lang_code)
            text_output.delete("1.0", tk.END) 
            text_output.insert(tk.END, translated.text)
        except Exception as e:
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, f"Error: {str(e)}")
    else:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "No text entered for translation.")

def clear_text():
    text_input.delete("1.0", tk.END)
    text_output.delete("1.0", tk.END)

root = tk.Tk()
root.title('Language Translation Tool')
root.geometry('990x570')
root.configure(bg='grey')

frame = Frame(root, width=990, height=570, relief='solid', borderwidth=2, bg='lightgrey')
frame.place(x=0, y=0)

Label(root, text='Language Translation Tool', font=("Segoe UI", 18, "bold"), fg="black", background='lightgrey').pack(pady=20)


languages = [
    "English", "Spanish", "French", "German", "Chinese", "Japanese", "Korean", 
    "Arabic", "Hindi", "Russian", "Portuguese", "Italian", "Dutch", "Turkish", 
    "Polish", "Swedish", "Greek", "Vietnamese", "Hebrew", "Indonesian", "Bengali",
    "Thai", "Filipino", "Malay", "Czech", "Danish", "Finnish", "Hungarian",
    "Norwegian", "Romanian", "Ukrainian"
]

language_codes = {
    "English": "en", "Spanish": "es", "French": "fr", "German": "de",
    "Chinese": "zh-cn", "Japanese": "ja", "Korean": "ko", "Arabic": "ar", 
    "Hindi": "hi", "Russian": "ru", "Portuguese": "pt", "Italian": "it", 
    "Dutch": "nl", "Turkish": "tr", "Polish": "pl", "Swedish": "sv", 
    "Greek": "el", "Vietnamese": "vi", "Hebrew": "he", "Indonesian": "id", 
    "Bengali": "bn", "Thai": "th", "Filipino": "tl", "Malay": "ms", 
    "Czech": "cs", "Danish": "da", "Finnish": "fi", "Hungarian": "hu", 
    "Norwegian": "no", "Romanian": "ro", "Ukrainian": "uk"
}


# Input language selection
input_language = ttk.Combobox(frame, values=languages, font=('verdana', 12), state="readonly", width=40)
input_language.set("Select Input Language")
input_language.place(x=50, y=50)

# Output language selection
output_language = ttk.Combobox(frame, values=languages, font=('verdana', 12), state="readonly", width=40)
output_language.set("Select Output Language")
output_language.place(x=500, y=50)

# Text input and output fields
text_input = Text(frame, width=45, height=5, borderwidth=2, relief='solid', font=('verdana', 12))
text_input.place(x=50, y=100)

text_output = Text(frame, width=45, height=5, borderwidth=2, relief='solid', font=('verdana', 12))
text_output.place(x=500, y=100)

# Translate button
button = Button(frame, text='Translate', relief=RAISED, borderwidth=3, font=('verdana', 12, 'bold'), bg='blue', fg='white', cursor='hand2', command=translate_text)
button.place(x=350, y=400)

# Clear button
btn = Button(frame, text='Clear', relief=RAISED, borderwidth=3, font=('verdana', 12, 'bold'), bg='blue', fg='white', cursor='hand2', command=clear_text)
btn.place(x=500, y=400)

# Start the Tkinter event loop
root.mainloop()
