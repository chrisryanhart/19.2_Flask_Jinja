"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def __repr__(self):
        return f"Words: = {self.prompts}, Template = {self.template}"

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)
        text = text.strip('\n')
        # what is type of text? str
        print(type(text))
        type(text)
        

        return text.strip('\n')
    def get_words(self):
        words = self.prompts
        return words

    def get_text(self):
        text = self.template
        return text

# what does items do?

# what does replace do?

# Here's a story to get you started
# need to get place, adjective, noun, verb, and plural_noun
# use dict for answers param in generate?

# need to remove "\n" from 

my_dict = {"place": "Lexington", "adjective":"green", "noun": "ball", "verb": "walk", "plural_noun": "houses"}
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "adverb"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

