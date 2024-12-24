import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from modules.flashcards import FlashcardsProcessor
from modules.mcqs import MCQsProcessor
from modules.vocabulary import VocabularyProcessor
from modules.definitions import DefinitionsProcessor

class AnkiGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anki Generator App")
        self.root.geometry("500x500")
        
        self.file_path = None

        # Base output directory
        self.base_output_dir = "output/generated_files"

        # Create UI sections
        self.create_sections()

    def create_sections(self):
        # Flashcards Section
        tk.Label(root, text="Flashcards").pack(pady=10)
        tk.Button(root, text="Upload Flashcards File", command=self.upload_flashcards_file).pack(pady=5)
        tk.Button(root, text="Generate Flashcards .apkg", command=self.generate_flashcards).pack(pady=5)

        # MCQs Section
        tk.Label(root, text="MCQs").pack(pady=10)
        tk.Button(root, text="Upload MCQs File", command=self.upload_mcqs_file).pack(pady=5)
        tk.Button(root, text="Generate MCQs .apkg", command=self.generate_mcqs).pack(pady=5)

        # Vocabulary Section
        tk.Label(root, text="Vocabulary").pack(pady=10)
        tk.Button(root, text="Upload Vocabulary File", command=self.upload_vocabulary_file).pack(pady=5)
        tk.Button(root, text="Generate Vocabulary .apkg", command=self.generate_vocabulary).pack(pady=5)

        # Definitions Section
        tk.Label(root, text="Definitions").pack(pady=10)
        tk.Button(root, text="Upload Definitions File", command=self.upload_definitions_file).pack(pady=5)
        tk.Button(root, text="Generate Definitions .apkg", command=self.generate_definitions).pack(pady=5)

    # Utility to create unique file paths
    def get_unique_file_path(self, folder_name, base_name):
        folder_path = os.path.join(self.base_output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f"{base_name}_{timestamp}.apkg"
        return os.path.join(folder_path, file_name)

    # Flashcards Methods
    def upload_flashcards_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            messagebox.showinfo("File Uploaded", f"File successfully uploaded: {self.file_path}")

    def generate_flashcards(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload a Flashcards file first.")
            return
        processor = FlashcardsProcessor(self.file_path)
        processor.parse_file()
        output_path = self.get_unique_file_path("Flashcards", "flashcards")
        processor.generate_apkg(output_path)
        messagebox.showinfo("Success", f"Flashcards .apkg generated at: {output_path}")

    # MCQs Methods
    def upload_mcqs_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            messagebox.showinfo("File Uploaded", f"File successfully uploaded: {self.file_path}")

    def generate_mcqs(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload an MCQs file first.")
            return
        processor = MCQsProcessor(self.file_path)
        processor.parse_file()
        output_path = self.get_unique_file_path("MCQs", "mcqs")
        processor.generate_apkg(output_path)
        messagebox.showinfo("Success", f"MCQs .apkg generated at: {output_path}")

    # Vocabulary Methods
    def upload_vocabulary_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            messagebox.showinfo("File Uploaded", f"File successfully uploaded: {self.file_path}")

    def generate_vocabulary(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload a Vocabulary file first.")
            return
        processor = VocabularyProcessor(self.file_path)
        processor.parse_file()
        output_path = self.get_unique_file_path("Vocabulary", "vocabulary")
        processor.generate_apkg(output_path)
        messagebox.showinfo("Success", f"Vocabulary .apkg generated at: {output_path}")

    # Definitions Methods
    def upload_definitions_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            messagebox.showinfo("File Uploaded", f"File successfully uploaded: {self.file_path}")

    def generate_definitions(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload a Definitions file first.")
            return
        processor = DefinitionsProcessor(self.file_path)
        processor.parse_file()
        output_path = self.get_unique_file_path("Definitions", "definitions")
        processor.generate_apkg(output_path)
        messagebox.showinfo("Success", f"Definitions .apkg generated at: {output_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AnkiGeneratorApp(root)
    root.mainloop()