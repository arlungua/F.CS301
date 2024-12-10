import tkinter as tk
from tkinter import filedialog, messagebox
from hunspell import Hunspell
from collections import Counter
import tensorflow as tf

# Hunspell тохиргоо (Hunspell-ийн үгийн санг зааж өгөх)
hunspell = Hunspell('mn_MN', hunspell_data_dir='/path/to/hunspell-dictionaries')

# Монгол текстийн нийтлэг үгс (stop words)
STOP_WORDS = {"юм", "ба", "болон", "байна", "гэх", "гээд", "тэгээд", "гээ", "нь", "буюу", "гээч"}

def process_text(text):
    """Текстийг боловсруулж алдаатай үгсийг тэмдэглэх, зөв үг санал болгох."""
    words = text.split()
    errors = {}
    stemmed_words = []

    for word in words:
        clean_word = word.strip(",.!?-\"'")  # Тэмдэгтүүдийг арилгах
        if not hunspell.spell(clean_word):
            errors[clean_word] = hunspell.suggest(clean_word)
        stemmed_words.append(hunspell.stem(clean_word)[0] if hunspell.stem(clean_word) else clean_word)

    return stemmed_words, errors

def count_top_words(words, exclude=set()):
    """Хамгийн түгээмэл үгсийг тоолох."""
    filtered_words = [word for word in words if word not in exclude]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(10)

def classify_text(text):
    """Текстийн ерөнхий агуулгыг тодорхойлох (жишээ TensorFlow загвар)."""
    # Жишээ загвар (боломжтой бол өөрийн загварыг энд ашиглах)
    categories = ["Эдийн засаг", "Спорт", "Шинжлэх ухаан", "Улс төр"]
    model = tf.keras.models.load_model("path/to/your/classification_model")
    prediction = model.predict([text])
    return categories[prediction.argmax()]

def open_file():
    """Текст файлыг сонгож унших."""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            input_text.delete(1.0, tk.END)
            input_text.insert(tk.END, file.read())

def process_input():
    """Хэрэглэгчийн текстийг боловсруулж үр дүнг харуулах."""
    text = input_text.get(1.0, tk.END).strip()
    if not text:
        messagebox.showerror("Алдаа", "Текст хоосон байна!")
        return

    stemmed_words, errors = process_text(text)
    top_words = count_top_words(stemmed_words, exclude=STOP_WORDS)
    category = classify_text(text)

    # Үр дүнг харуулах
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "=== Алдаатай үгс ба зөв хувилбарууд ===\n")
    for word, suggestions in errors.items():
        result_text.insert(tk.END, f"{word} -> {', '.join(suggestions)}\n")
    
    result_text.insert(tk.END, "\n=== Хамгийн их давтагдсан үгс ===\n")
    for word, count in top_words:
        result_text.insert(tk.END, f"{word}: {count}\n")
    
    result_text.insert(tk.END, f"\n=== Агуулгын ангилал ===\n{category}\n")

# График интерфейс (GUI) үүсгэх
app = tk.Tk()
app.title("Монгол Текст Боловсруулах Програм")
app.geometry("800x600")

# Хэрэглэгчийн текст оруулах талбар
tk.Label(app, text="Текст оруулах:").pack()
input_text = tk.Text(app, height=10, wrap=tk.WORD)
input_text.pack(fill=tk.BOTH, padx=10, pady=5)

# Файл унших товч
tk.Button(app, text="Файл сонгох", command=open_file).pack(pady=5)

# Текст боловсруулалт хийх товч
tk.Button(app, text="Боловсруулах", command=process_input).pack(pady=5)

# Үр дүн харуулах талбар
tk.Label(app, text="Үр дүн:").pack()
result_text = tk.Text(app, height=15, wrap=tk.WORD, bg="#f0f0f0")
result_text.pack(fill=tk.BOTH, padx=10, pady=5)

# Програм ажиллуулах
app.mainloop()
