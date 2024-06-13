import tkinter as tk
from tkinter import font, Label

class TextManager:

    def adjust_label_font(label, text, min_font_size=15, max_font_size=20, availablewidth=1280):
        # Dimensions disponibles pour le label
        available_width = availablewidth
        available_height = 100

        # Crée une police de test
        test_font_size = max_font_size  # Commence par une taille de police grande
        test_font = font.Font(family="Helvetica", size=test_font_size)

        # Réduit la taille de la police jusqu'à ce que le texte tienne dans l'espace disponible
        while test_font_size > min_font_size:
            test_font.config(size=test_font_size)
            text_width = test_font.measure(text)
            text_height = test_font.metrics("linespace")

            if text_width <= available_width and text_height <= available_height:
                break
            
            test_font_size -= 1

        if test_font_size <= min_font_size:
            # Si la taille de police est inférieure à min_font_size, ajouter des sauts de ligne
            words = text.split()
            new_text = ""
            current_line = ""
            
            test_font.config(size=min_font_size)
            
            for word in words:
                if test_font.measure(current_line + " " + word) <= available_width:
                    current_line += ("" if current_line == "" else " ") + word
                else:
                    new_text += ("" if new_text == "" else "\n") + current_line
                    current_line = word

            new_text += ("" if new_text == "" else "\n") + current_line
            text = new_text
            test_font_size = min_font_size
        
        # Appliquer la taille de police ajustée et le texte au label
        label.config(text=text, font=("Helvetica", test_font_size))
