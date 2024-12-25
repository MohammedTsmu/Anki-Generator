import genanki

class FlashcardsProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.flashcards = []

    def parse_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            question, answer = None, None
            for line in lines:
                if line.startswith("Question:"):
                    question = line.split(":", 1)[1].strip()
                elif line.startswith("Answer:"):
                    answer = line.split(":", 1)[1].strip()
                if question and answer:
                    self.flashcards.append((question, answer))
                    question, answer = None, None

    def generate_apkg(self, output_path):
        model = genanki.Model(
            1607392319,
            'Dr.Mohammed_Flashcards',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '''
                        <div class="card">
                            <div class="question">{{Question}}</div>
                        </div>
                    ''',
                    'afmt': '''
                        <div class="card">
                            <div class="question">{{Question}}</div>
                            <hr>
                            <div class="answer">{{Answer}}</div>
                        </div>
                    ''',
                },
            ],
            css='''
                .card {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: #e0e0e0; /* Light gray text */
                    background-color: #121212; /* Dark background */
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
                }
                .question {
                    font-size: 1.6em;
                    font-weight: bold;
                    color: #ffffff; /* White for the main question */
                }
                .answer {
                    font-size: 1.4em;
                    color: #76c7c0; /* Soft teal for answers */
                }
                hr {
                    border: none;
                    border-top: 1px solid #444; /* Subtle gray divider */
                    margin: 20px 0;
                }
                @media (max-width: 600px) {
                    .card {
                        font-size: 1em;
                        padding: 10px;
                    }
                    .question, .answer {
                        font-size: 1.2em;
                    }
                }
            ''',
        )

        deck = genanki.Deck(2059400110, 'Dr.Mohammed_Flashcards Deck')
        for question, answer in self.flashcards:
            note = genanki.Note(
                model=model,
                fields=[question, answer]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
