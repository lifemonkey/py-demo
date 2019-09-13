from flashtext import KeywordProcessor


# Create an object of KeywordProcessor
keyword_processor = KeywordProcessor()
# add keywords
keyword_names = ['NY', 'new-york', 'SF']
clean_names = ['new york', 'new york', 'san francisco']
for keyword_name, clean_name in zip(keyword_names, clean_names):
    keyword_processor.add_keyword(keyword_name, clean_name)
keywords_found = keyword_processor.replace_keywords('I love SF and NY. new-york is the best.')
print(keywords_found)
