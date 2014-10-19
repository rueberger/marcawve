import numpy as np
import scipy


class CorpusCleaner(object):
    """A class that does preprocessing on our corpii
    """

    def __init__(self, corpii):
        self.invalid_chars = {'/', '+', '*'}
        self.punctation = {'.', '!', ',', '?', ';', '"', '""'}
        self.eol_chars = {'-'}
        self.eol_buffer = None

    def corpus_cleaner(self):
        """Returns a generator over the all the corpuscles
        """
        eol_buffer = None
        for corpus in corpi:
            for line in corpus:
                tokens = line.split()
                for token in line[:-1]:                                

    def process_word(self, token, is_first, is_last):
        """Remove invalid characters, resolve eol word breaks,
           cast lowercase
        returns a tuple containing probably valid words
        """
        is_filet = not is_first and not is_last
        token_class = self.classify_token(token)
        if self.eol_buffer is not None:
            token = self.eol_buffer + token
            self.eol_buffer = None 
        if token_class == 0 and is_filet:
            return (token)
        if token_class == 1:
            return (token[1:])
        if token_class == 2:
            return (token[:-1])
        if token_class == 3:
            return None
        if token_class == 4:
            return (token[0], token[1:])
        if token_class == 5:
            return (token[:-1], token[:-1])
        if token_class == 6:
            return (token)
        if token_class == 7:
            #handle eol stuff 


    def classify_token(self, token):
        """Returns 0 if the token is a word
        Returns 1 if the token starts with an invalid character
        Returns 2 if the token ends with an invalid character
        Returns 3 if the token is an invalid character
        Returns 4 if the token starts with punctuation
        Returns 5 if the token ends with punctuation.
        Returns 6 if the token is punctuation
        Returns 7 if the token ends with an EOL character

        """
        #check is ascii
        max_ind = len(token) - 1
        is_char = max_ind == 0
        for ind, char in enumerate(token):
            if char in self.invalid_chars:
                if is_char:
                    return 3
                elif ind == 0:
                    return 1
                elif ind == max_ind:
                    return 2
            elif char in self.punctuation:
                if is_char:
                    return 6
                elif ind == 0:
                    return 4
                elif ind == max_ind:
                    return 5
            elif char in self.eol_chars and ind == max_ind:
                return 7
        return 0