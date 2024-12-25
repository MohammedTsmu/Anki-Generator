import genanki

class MCQsProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.mcqs = []

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
            'Dr.Mohammed_MCQs',
            fields=[
                {'name': 'Question'},
                {'name': 'Options'},
                {'name': 'Correct Answer'},
            ],
            templates=[
                {
                    'name': 'MCQ Card',
                    'qfmt': '''
                        <div class="card">
                            <div class="question">{{Question}}</div>
                            <div class="options">
                                {{Options}}
                            </div>
                        </div>
                    ''',
                    'afmt': '''
                        <div class="card">
                            <div class="question">{{Question}}</div>
                            <div class="options">{{Options}}</div>
                            <hr>
                            <div class="correct-answer">Correct Answer: {{Correct Answer}}</div>
                        </div>
                    ''',
                },
            ],
            css='''
                .card {
                    font-family: Arial, sans-serif;
                    text-align: left;
                    color: #d0d0d0; /* Light gray text */
                    background-color: #1e1e1e; /* Darker gray background */
                    padding: 15px;
                    border-radius: 8px;
                }
                .question {
                    font-size: 1.4em;
                    font-weight: bold;
                    color: #ffffff;
                    margin-bottom: 15px;
                }
                .options {
                    font-size: 1.2em;
                    margin-left: 20px;
                    color: #bbbbbb; /* Lighter gray for options */
                }
                .correct-answer {
                    font-size: 1.1em;
                    color: #8ac926; /* Soft green for correct answer */
                }
                hr {
                    border: none;
                    border-top: 1px solid #444;
                    margin: 20px 0;
                }
                @media (max-width: 600px) {
                    .card {
                        font-size: 0.9em;
                    }
                    .question, .options, .correct-answer {
                        font-size: 1em;
                    }
                }
            ''',
        )

        deck = genanki.Deck(2059400120, 'Dr.Mohammed_MCQs Deck')
        for question, options, correct_option in self.mcqs:
            options_formatted = "<br>".join([f"{key}) {value}" for key, value in options.items()])
            note = genanki.Note(
                model=model,
                fields=[question, options_formatted, correct_option]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
