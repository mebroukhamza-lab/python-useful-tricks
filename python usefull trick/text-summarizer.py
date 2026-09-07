# pip install sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
text = "Put your long text here. It can be several sentences long. The summarizer will pick the most important ones."
parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 2)
for sentence in summary:
    print(sentence)
