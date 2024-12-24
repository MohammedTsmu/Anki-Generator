import genanki

class VocabularyProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.vocabulary = []

    # def parse_file(self):
    #     with open(self.file_path, 'r') as file:
    #         lines = file.readlines()
    #         term, translation = None, None
    #         for line in lines:
    #             if line.startswith("Term:"):
    #                 term = line.split(":", 1)[1].strip()
    #             elif line.startswith("Translation:"):
    #                 translation = line.split(":", 1)[1].strip()
    #             if term and translation:
    #                 self.vocabulary.append((term, translation))
    #                 term, translation = None, None

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
                    'qfmt': '{{Term}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Translation}}',
                },
            ],
        )
        deck = genanki.Deck(2059400130, 'Vocabulary Deck')
        for term, translation in self.vocabulary:
            note = genanki.Note(
                model=model,
                fields=[term, translation]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
