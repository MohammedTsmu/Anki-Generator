import genanki

class DefinitionsProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.definitions = []

    def parse_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            term, definition = None, None
            for line in lines:
                if line.startswith("Term:"):
                    term = line.split(":", 1)[1].strip()
                elif line.startswith("Definition:"):
                    definition = line.split(":", 1)[1].strip()
                if term and definition:
                    self.definitions.append((term, definition))
                    term, definition = None, None

    def generate_apkg(self, output_path):
        model = genanki.Model(
            1607392322,
            'Dr.Mohammed_Definitions',
            fields=[
                {'name': 'Term'},
                {'name': 'Definition'},
            ],
            templates=[
                {
                    'name': 'Definition Card',
                    'qfmt': '''
                        <div class="card">
                            <div class="term">{{Term}}</div>
                        </div>
                    ''',
                    'afmt': '''
                        <div class="card">
                            <div class="term">{{Term}}</div>
                            <hr>
                            <div class="definition">{{Definition}}</div>
                        </div>
                    ''',
                },
            ],
            css='''
                .card {
                    font-family: Georgia, serif;
                    text-align: left;
                    color: #cfcfcf;
                    background-color: #202020;
                    padding: 20px;
                    border-radius: 8px;
                }
                .term {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #ffffff;
                }
                .definition {
                    font-size: 1.2em;
                    margin-top: 10px;
                    color: #b0b0b0;
                }
                hr {
                    border: none;
                    border-top: 1px solid #444;
                    margin: 20px 0;
                }
                @media (max-width: 600px) {
                    .card {
                        padding: 10px;
                    }
                    .term {
                        font-size: 1.2em;
                    }
                    .definition {
                        font-size: 1em;
                    }
                }
            ''',
        )

        deck = genanki.Deck(2059400140, 'Dr.Mohammed_Definitions Deck')
        for term, definition in self.definitions:
            note = genanki.Note(
                model=model,
                fields=[term, definition]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
