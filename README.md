# Anki Generator Application

This is a Python-based GUI application that allows users to generate Anki-compatible `.apkg` files for various types of study notes, such as:

- Flashcards
- Multiple Choice Questions (MCQs)
- Vocabulary
- Definitions
- Cloze Notes

The application supports merging multiple files, viewing prompts, and previewing generated files in a user-friendly interface.

---

## Features

- **Note Types**: Supports Flashcards, MCQs, Vocabulary, Definitions, and Cloze Notes.
- **Prompt Viewer**: Displays customizable prompts for generating input files.
- **File Merging**: Combine multiple files into a single `.apkg` file.
- **Preview Generated Files**: View all generated files directly within the application.
- **Cross-Platform Executable**: Works as a standalone executable for easy distribution.

---

## Installation

### Running the Application

1. **Download the Executable**
   - Locate the pre-built executable from the `dist` folder or download it from the release section.
   - No installation of Python is required.

2. **Run the Application**
   - Double-click on the `main.exe` file to launch the application.

### Building from Source (For Developers)

1. **Prerequisites**
   - Python 3.13 or higher
   - Required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

2. **Clone the Repository**
   ```bash
   git clone https://github.com/MohammedTsmu/Anki-Generator.git
   cd anki-generator
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```

4. **Build the Executable**
   ```bash
   pyinstaller --onefile --windowed main.py
   ```
   The standalone executable will be available in the `dist` folder.

---

## Usage

### Input File Structure
Each note type has its specific structure for input files. Use the "View Prompt" button in the application for guidance on formatting input files.

#### Example: Flashcards
```
Question: What is the capital of France?
Answer: Paris

Question: What is the square root of 16?
Answer: 4
```

### Generated Files
- Files are stored in the `output/generated_files/<note-type>` folder.
- File previews are available within the application.

---

## Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)

### Generated Files Preview
![Generated Files Preview](screenshots/generated_files_preview.png)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## Project Reference

### App Description for Recreation

If you wish to recreate the **Anki Generator Application**, use the following guidelines:

**Prompt:**

"Generate a Python application called **Anki Generator App**. The application should be a GUI tool for generating `.apkg` files compatible with Anki. It must support the following features:

#### Features:
1. **Note Types**: Generate notes for:
   - Flashcards
   - Multiple Choice Questions (MCQs)
   - Vocabulary
   - Definitions
   - Cloze Notes

2. **Prompt Viewer**: Display customizable prompts for each note type to help users generate content files with the correct structure. Users should have options to copy prompts to their clipboard, toggle between editable and read-only modes, and make changes before copying.

3. **File Merging**: Allow users to merge multiple text files for each note type into a single `.apkg` file.

4. **Preview Section**: Provide a section that dynamically lists all generated `.apkg` files. Users should be able to:
   - Open files directly.
   - Open the folder containing the file.

5. **Dynamic Folder Structure**: Organize generated files in subfolders (e.g., `Flashcards`, `MCQs`) under a root folder (`output/generated_files`).

6. **Cross-Platform Executable**: Package the application into a standalone executable that works on any Windows machine.

#### Implementation Details:
- Use **Tkinter** for the GUI.
- Include dynamic styles with a dark theme using grays and whites for better visual comfort.
- Use `genanki` to generate `.apkg` files for each note type, and ensure all templates include styled HTML and CSS for a polished appearance.
- Automatically maximize the window on startup.
- Allow users to copy prompts with a button click.
- Provide buttons for uploading files, generating `.apkg` files, and merging files for each note type.

#### Code Structure:
1. **`main.py`**: The main script to run the application.
2. **`modules` folder**:
   - Contains processors for each note type: `flashcards.py`, `mcqs.py`, `vocabulary.py`, `definitions.py`, and `cloze.py`.
   - Each processor should include methods to parse input text files, validate content, and generate `.apkg` files.
3. **`templates` folder**:
   - Contains text files with prompts for each note type (e.g., `flashcards_prompt.txt`).
4. **`output/generated_files` folder**:
   - Stores generated `.apkg` files.

#### Example of Input File Structure:
##### Flashcards:
```
Question: What is the capital of France?
Answer: Paris

Question: What is the square root of 16?
Answer: 4
```

##### Cloze:
```
Cloze: The capital of France is Paris.
Answer: Paris
```

Include comments in the code explaining the purpose of each function and class."

---

## Contact

For questions or feedback, please reach out via [GitHub Issues](https://github.com/MohammedTsmu/Anki-Generator/issues).
