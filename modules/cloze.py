import genanki

class ClozeProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cloze_notes = []

    def parse_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cloze, answer = None, None
            for line in lines:
                if line.startswith("Cloze:"):
                    cloze = line.split(":", 1)[1].strip()
                elif line.startswith("Answer:"):
                    answer = line.split(":", 1)[1].strip()
                if cloze and answer:
                    # Add curly braces to indicate the cloze deletion
                    cloze_with_deletion = cloze.replace(answer, f"{{{{c1::{answer}}}}}")
                    self.cloze_notes.append((cloze_with_deletion, answer))
                    cloze, answer = None, None

    def generate_apkg(self, output_path):
        model = genanki.Model(
            1607392323,
            'Dr.Mohammed_Cloze',
            fields=[
                {'name': 'Text'},
                {'name': 'Extra'},
            ],
            templates=[
                {
                    'name': 'Cloze Card',
                    'qfmt': '''
                        <div class="card">
                            <div class="text">{{cloze:Text}}</div>
                        </div>
                    ''',
                    'afmt': '''
                        <div class="card">
                            <div class="text">{{cloze:Text}}</div>
                            <hr>
                            <div class="extra">{{Extra}}</div>
                        </div>
                    ''',
                },
            ],
            css=''' 
                .card {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: #e0e0e0;
                    background-color: #1e1e1e; /* Dark gray background */
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.6);
                }
                .text {
                    font-size: 1.6em;
                    font-weight: bold;
                    color: #ffffff; /* Bright text for visibility */
                    margin-bottom: 20px;
                }
                .extra {
                    font-size: 1.2em;
                    color: #76c7c0; /* Soft teal for extra info */
                    margin-top: 15px;
                }
                hr {
                    border: none;
                    border-top: 2px solid #444; /* Subtle divider for sections */
                    margin: 20px 0;
                }
                .cloze {
                    font-weight: bold;
                    background-color: #ffa500; /* Highlighted orange for cloze deletion */
                    color: #000000;
                    padding: 0 4px;
                    border-radius: 3px;
                }
                @media (max-width: 600px) {
                    .card {
                        font-size: 1em;
                        padding: 15px;
                    }
                    .text, .extra {
                        font-size: 1.2em;
                    }
                }
            ''',
            model_type=genanki.Model.CLOZE,  # Cloze note type
        )

        deck = genanki.Deck(2059400150, 'Dr.Mohammed_Cloze Deck')
        for cloze, answer in self.cloze_notes:
            note = genanki.Note(
                model=model,
                fields=[cloze, answer]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
