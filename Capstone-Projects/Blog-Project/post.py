from datetime import datetime

class Post:

    def __init__(self, id, title, subtitle, author, body, published_date, img_url) -> None:
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.body = body
        pub_date = datetime.strptime(published_date, '%m/%d/%Y')
        self.published_at_date = pub_date.strftime('%B %d, %Y')
        self.img = img_url