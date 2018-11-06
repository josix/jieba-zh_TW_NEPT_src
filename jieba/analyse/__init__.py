from __future__ import absolute_import
from .tfidf import TFIDF
from .textrank import TextRank
from .textrank_similarity import TextRankSimilarity
from .textrank_vsm import TextRankVSM
try:
    from .analyzer import ChineseAnalyzer
except ImportError:
    pass

default_tfidf = TFIDF()
default_textrank = TextRank()
default_textrank_similarity = TextRankSimilarity()
default_textrank_vsm = TextRankVSM()

extract_tags = tfidf = default_tfidf.extract_tags
set_idf_path = default_tfidf.set_idf_path
textrank = default_textrank.extract_tags
textrank_similarity = default_textrank_similarity.extract_tags
textrank_vsm = default_textrank_vsm.extract_tags

def set_stop_words(stop_words_path):
    default_tfidf.set_stop_words(stop_words_path)
    default_textrank.set_stop_words(stop_words_path)
