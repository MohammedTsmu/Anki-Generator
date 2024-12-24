import genanki

class FlashcardsProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.flashcards = []

    # def parse_file(self):
    #     with open(self.file_path, 'r') as file:
    #         lines = file.readlines()
    #         question, answer = None, None
    #         for line in lines:
    #             if line.startswith("Question:"):
    #                 question = line.split(":", 1)[1].strip()
    #             elif line.startswith("Answer:"):
    #                 answer = line.split(":", 1)[1].strip()
    #             if question and answer:
    #                 self.flashcards.append((question, answer))
    #                 question, answer = None, None

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
            'Flashcards Model',
            fields=[{'name': 'Question'}, {'name': 'Answer'}],
            templates=[{
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            }],
        )
        deck = genanki.Deck(2059400110, 'Flashcards Deck')
        for question, answer in self.flashcards:
            note = genanki.Note(
                model=model,
                fields=[question, answer]
            )
            deck.add_note(note)
        genanki.Package(deck).write_to_file(output_path)
