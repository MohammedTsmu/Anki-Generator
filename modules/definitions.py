import genanki

class DefinitionsProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.definitions = []

    # def parse_file(self):
    #     with open(self.file_path, 'r') as file:
    #         lines = file.readlines()
    #         term, definition = None, None
    #         for line in lines:
    #             if line.startswith("Term:"):
    #                 term = line.split(":", 1)[1].strip()
    #             elif line.startswith("Definition:"):
    #                 definition = line.split(":", 1)[1].strip()
    #             if term and definition:
    #                 self.definitions.append((term, definition))
    #                 term, definition = None, None

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
            'Definitions Model',
            fields=[
                {'name': 'Term'},
                {'name': 'Definition'},
            ],
            templates=[
                {
                    'name': 'Definition Card',
                    'qfmt': '{{Term}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Definition}}',
                },
            ],
        )
        deck = genanki.Deck(2059400140, 'Definitions Deck')
        for term, definition in self.definitions:
            note = genanki.Note(
                model=model,
                fields=[term, definition]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
