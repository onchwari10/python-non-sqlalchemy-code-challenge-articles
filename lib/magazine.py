class Magazine:
    def __init__(self, name, category):
        if not 2 <= len(name) <= 16:
            raise ValueError("Magazine name must be between 2 and 16 characters, inclusive.")
        if len(category) == 0:
            raise ValueError("Magazine category must have length greater than 0.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def contributors(self):
        authors = {}
        for article in self._articles:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        return [author for author, count in authors.items() if count > 2] or None

