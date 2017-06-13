import json
from converter import convert

def test_converter():
    usn_article_json = open('tests/sample_article.json')
    article_json = convert(usn_article_json)
    article = json.loads(article_json)
    assert type(article) == dict
