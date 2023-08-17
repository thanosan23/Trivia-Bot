import wikipediaapi


def get_summary(topic : str):
    wiki_data = wikipediaapi.Wikipedia('<Enter user agent here>', 'en')
    page = wiki_data.page(topic)
    return page.summary