import tkinter as tk

from scraper import get_phrase


def handle_click() -> None:
    input_phrases = (input_text.get('1.0', tk.END))
    replaced_input_phrase = input_phrases.replace('\n', ' ')
    wanted_tuple = tuple(replaced_input_phrases.split())
    get_phrase(*wanted_tuple)


def clear_input() -> None:
    input_text.delete("1.0", tk.END)
    input_text.update()


window = tk.Tk()
window.title("SEO Phrases Tool")
entry = tk.Entry()
check_button = tk.Button(master=window, text="Sprawdź frazy", command=handle_click, height=2, width=20)
delete_button = tk.Button(master=window, text="Wyczyść frazy", command=clear_input, height=2, width=20)
input_text = tk.Text()
input_text.pack()
main_label = tk.Label(master=window, text="Wpisz szukane frazy jedna pod drugą a następnie kliknij poniżej. \n"
                                 "Szukanie chwilę potrwa a gdy przycisk będzie ponownie aktywny wygenerowany plik .txt znajdziesz w folderze (nazwa to 'fraza + data').\n"
                                 "Teraz możesz zamknąć program lub wyczyść okno i sprawdź kolejne frazy")
main_label.pack()
check_button.pack()
delete_button.pack()
window.mainloop()
