import genanki

class MCQsProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.mcqs = []

    # def parse_file(self):
    #     with open(self.file_path, 'r') as file:
    #         lines = file.readlines()
    #         question, options, correct_option = None, {}, None
    #         for line in lines:
    #             if line.startswith("Question:"):
    #                 question = line.split(":", 1)[1].strip()
    #             elif line.startswith("Option A:"):
    #                 options['A'] = line.split(":", 1)[1].strip()
    #             elif line.startswith("Option B:"):
    #                 options['B'] = line.split(":", 1)[1].strip()
    #             elif line.startswith("Option C:"):
    #                 options['C'] = line.split(":", 1)[1].strip()
    #             elif line.startswith("Option D:"):
    #                 options['D'] = line.split(":", 1)[1].strip()
    #             elif line.startswith("Correct Option:"):
    #                 correct_option = line.split(":", 1)[1].strip()
                
    #             if question and options and correct_option:
    #                 self.mcqs.append((question, options, correct_option))
    #                 question, options, correct_option = None, {}, None

    def parse_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            question, options, correct_option = None, {}, None
            for line in lines:
                if line.startswith("Question:"):
                    question = line.split(":", 1)[1].strip()
                elif line.startswith("Option A:"):
                    options['A'] = line.split(":", 1)[1].strip()
                elif line.startswith("Option B:"):
                    options['B'] = line.split(":", 1)[1].strip()
                elif line.startswith("Option C:"):
                    options['C'] = line.split(":", 1)[1].strip()
                elif line.startswith("Option D:"):
                    options['D'] = line.split(":", 1)[1].strip()
                elif line.startswith("Correct Option:"):
                    correct_option = line.split(":", 1)[1].strip()
                if question and options and correct_option:
                    self.mcqs.append((question, options, correct_option))
                    question, options, correct_option = None, {}, None


    def generate_apkg(self, output_path):
        model = genanki.Model(
            1607392320,
            'MCQs Model',
            fields=[
                {'name': 'Question'},
                {'name': 'Options'},
                {'name': 'Correct Answer'},
            ],
            templates=[
                {
                    'name': 'MCQ Card',
                    'qfmt': '{{Question}}<br>{{Options}}',
                    'afmt': '{{FrontSide}}<hr id="answer">Correct Answer: {{Correct Answer}}',
                },
            ],
        )
        deck = genanki.Deck(2059400120, 'MCQs Deck')
        for question, options, correct_option in self.mcqs:
            options_formatted = "<br>".join([f"{key}) {value}" for key, value in options.items()])
            note = genanki.Note(
                model=model,
                fields=[question, options_formatted, correct_option]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
