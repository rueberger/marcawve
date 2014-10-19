import numpy as np
import scipy


class Markov(object):
    """A class implementing a markov chain
    """

    #TO DO:
    #Warnings for integer overflow for higher order transition matrices

    def __init__(self, corpi, order):
        """corpi is a list (a really big one) of words
        corpi presumed to be preprocessed correctly (no spaces, special characters, etc)
        order specifies how many words to condition the probability distribution on
        """
        #array of transition matrices, indexed by order 
        self.transitions = [None for _ in xrange(order)]
        self.words_to_ind = dict()
        self.ind_to_words = dict()
        self.word_count = 0
        #file objects
        self.corpi = corpi
        self.order

    def preprocess(self):
        """Finds unique words, gives them indices
        Could be done in the same step as calculating first order
          transitions but simplifies code
        """
        cnt = 0
        for word in self.corpi:
            if word in self.words_to_ind:
                pass
            else:
                self.words_to_ind[word] = cnt
                self.ind_to_words[ind] = word
                cnt += 1
        self.word_count = cnt

    def build_transition_mat(self, n):
        """Builds the transition matrix (T) of order n
        T[i,j] = probability of transitioning from symbol i to j
        Let W denote the set of symbols, then j is an index of W
        and i is an index of WxWx....xW = W^n
        
        """
        transitions = scipy.sparse.dok_matrix((self.word_count**n, n)
                                              dtype=float32)
        #normalizing factor
        total_transitions = len(self.corpi - n)
        last_words = []
        for word in self.corpi:
            if len(last_words) < n:
                last_words.append(word)
            else:
                i = self.calculate_index(n, last_words)
                j = self.words_to_ind[word]
                transitions[i, j] += float(1) / float(total_transitions)
        #initial debugging remove later 
        assert np.sum(transitions) == 1
                
                

    def calculate_index(self, n, word_list):
        """Returns the index of the word_list,
           calculated in a way such that there's no overlapping

        BROKEN: INTEGER OVERFLOW
        """
        assert len(word_list) == n
        ind = 0
        for (i, word) in enumerate(word_lists):
            