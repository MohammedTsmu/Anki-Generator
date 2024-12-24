import genanki

class VocabularyProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.vocabulary = []

    def parse_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            term, translation = None, None
            for line in lines:
                if line.startswith("Term:"):
                    term = line.split(":", 1)[1].strip()
                elif line.startswith("Translation:"):
                    translation = line.split(":", 1)[1].strip()
                if term and translation:
                    self.vocabulary.append((term, translation))
                    term, translation = None, None

    def generate_apkg(self, output_path):
        model = genanki.Model(
            1607392321,
            'Vocabulary Model',
            fields=[
                {'name': 'Term'},
                {'name': 'Translation'},
            ],
            templates=[
                {
                    'name': 'Vocabulary Card',
                    'qfmt': '''
                        <div class="card">
                            <div class="term">{{Term}}</div>
                        </div>
                    ''',
                    'afmt': '''
                        <div class="card">
                            <div class="term">{{Term}}</div>
                            <hr>
                            <div class="translation">{{Translation}}</div>
                        </div>
                    ''',
                },
            ],
            css='''
                .card {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: #e0e0e0;
                    background-color: #181818;
                    padding: 20px;
                    border-radius: 10px;
                }
                .term {
                    font-size: 1.6em;
                    font-weight: bold;
                    color: #ffffff;
                    margin-bottom: 10px;
                }
                .translation {
                    font-size: 1.3em;
                    color: #ffa500; /* Soft orange for translation */
                }
                hr {
                    border: none;
                    border-top: 1px solid #444;
                    margin: 20px 0;
                }
                @media (max-width: 600px) {
                    .card {
                        font-size: 1em;
                    }
                    .term, .translation {
                        font-size: 1.2em;
                    }
                }
            ''',
        )

        deck = genanki.Deck(2059400130, 'Vocabulary Deck')
        for term, translation in self.vocabulary:
            note = genanki.Note(
                model=model,
                fields=[term, translation]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)