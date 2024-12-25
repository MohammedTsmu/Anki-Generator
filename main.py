import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # For styled widgets
from modules.flashcards import FlashcardsProcessor
from modules.mcqs import MCQsProcessor
from modules.vocabulary import VocabularyProcessor
from modules.definitions import DefinitionsProcessor
from modules.cloze import ClozeProcessor


class AnkiGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anki Generator App")
        self.root.geometry("600x700")  # Increased dimensions for better layout
        self.root.resizable(True, True)

        self.base_output_dir = "output/generated_files"
        os.makedirs(self.base_output_dir, exist_ok=True)

        self.create_styles()  # Initialize styles
        self.create_main_layout()  # Build the main UI layout

    # def create_styles(self):
    #     """Create styles for widgets."""
    #     self.style = ttk.Style()
    #     self.style.configure("TFrame", background="#2e2e2e")  # Dark gray background
    #     self.style.configure("TLabel", background="#2e2e2e", foreground="#ffffff", font=("Arial", 12))
    #     self.style.configure("TButton", background="#444444", foreground="#ffffff", font=("Arial", 10))
    #     self.style.map("TButton", background=[("active", "#5e5e5e")], foreground=[("active", "#ffffff")])
    def create_styles(self):
        """Create styles for widgets."""
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#3a3a3a")  # Slightly lighter gray background
        self.style.configure("TLabel", background="#3a3a3a", foreground="#ffffff", font=("Arial", 14, "bold"))
        self.style.configure(
            "TButton",
            background="#444444",
            foreground="#000000",
            font=("Arial", 12),
            padding=6,
            relief="flat",
        )
        self.style.map("TButton", background=[("active", "#5e5e5e")], foreground=[("active", "green")])


    def create_main_layout(self):
        """Create the main layout with sections."""
        # Create a main frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        # Add sections
        self.add_section(main_frame, "Flashcards", self.upload_flashcards_file, self.generate_flashcards, self.merge_flashcards_files)
        self.add_section(main_frame, "MCQs", self.upload_mcqs_file, self.generate_mcqs, self.merge_mcqs_files)
        self.add_section(main_frame, "Vocabulary", self.upload_vocabulary_file, self.generate_vocabulary, self.merge_vocabulary_files)
        self.add_section(main_frame, "Definitions", self.upload_definitions_file, self.generate_definitions, self.merge_definitions_files)
        self.add_section(main_frame, "Cloze Notes", self.upload_cloze_file, self.generate_cloze, self.merge_cloze_files)

    # def add_section(self, parent, section_title, upload_cmd, generate_cmd, merge_cmd):
    #     """Add a section with upload, generate, and merge buttons."""
    #     frame = ttk.Frame(parent, padding=10)
    #     frame.pack(fill="x", pady=10)

    #     ttk.Label(frame, text=section_title, font=("Arial", 14, "bold")).pack(anchor="w", pady=5)

    #     button_frame = ttk.Frame(frame)
    #     button_frame.pack(fill="x", padx=10, pady=5)

    #     ttk.Button(button_frame, text="Upload File", command=upload_cmd).pack(side="left", padx=5)
    #     ttk.Button(button_frame, text="Generate .apkg", command=generate_cmd).pack(side="left", padx=5)
    #     ttk.Button(button_frame, text="Merge Files", command=merge_cmd).pack(side="left", padx=5)
    def add_section(self, parent, section_title, upload_cmd, generate_cmd, merge_cmd):
        """Add a section with upload, generate, and merge buttons."""
        frame = ttk.Frame(parent, padding=10)
        frame.pack(fill="x", pady=15)  # More padding for spacing

        ttk.Label(frame, text=section_title, font=("Arial", 16, "bold")).pack(anchor="w", pady=5)

        button_frame = ttk.Frame(frame)
        button_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(button_frame, text="Upload File", command=upload_cmd).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Generate .apkg", command=generate_cmd).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Merge Files", command=merge_cmd).pack(side="left", padx=10)


    def get_unique_file_path(self, folder_name, base_name):
        folder_path = os.path.join(self.base_output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f"Dr.Mohammed_{base_name}_{timestamp}.apkg"
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

    def merge_flashcards_files(self):
        self.merge_files("Flashcards", FlashcardsProcessor, "flashcards")

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

    def merge_mcqs_files(self):
        self.merge_files("MCQs", MCQsProcessor, "mcqs")

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

    def merge_vocabulary_files(self):
        self.merge_files("Vocabulary", VocabularyProcessor, "vocabulary")

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

    def merge_definitions_files(self):
        self.merge_files("Definitions", DefinitionsProcessor, "definitions")

    # Cloze Methods
    def upload_cloze_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            messagebox.showinfo("File Uploaded", f"File successfully uploaded: {self.file_path}")

    def generate_cloze(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload a Cloze file first.")
            return
        processor = ClozeProcessor(self.file_path)
        processor.parse_file()
        output_path = self.get_unique_file_path("Cloze", "cloze")
        processor.generate_apkg(output_path)
        messagebox.showinfo("Success", f"Cloze .apkg generated at: {output_path}")

    def merge_cloze_files(self):
        self.merge_files("Cloze", ClozeProcessor, "cloze")

    def merge_files(self, folder_name, processor_class, base_name):
        file_paths = filedialog.askopenfilenames(filetypes=[("Text Files", "*.txt")])
        if not file_paths:
            messagebox.showerror("Error", "No files selected for merging.")
            return

        merged_notes = []
        for file_path in file_paths:
            processor = processor_class(file_path)
            processor.parse_file()
            merged_notes.extend(getattr(processor, base_name))

        processor = processor_class("")
        setattr(processor, base_name, merged_notes)

        output_path = self.get_unique_file_path(folder_name, f"merged_{base_name}")
        processor.generate_apkg(output_path)
        messagebox.showinfo("Success", f"Merged {folder_name} .apkg generated at: {output_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AnkiGeneratorApp(root)
    root.mainloop()
