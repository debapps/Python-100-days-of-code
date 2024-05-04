import requests

class Post:
    
    def __init__(self) -> None:
        self.url = 'https://api.npoint.io/18649ca2016ca15e42cf'
        response = requests.get(self.url)
        response.raise_for_status()
        self.data = response.json()

    def get_all_posts(self):
        return self.data['posts']
    
    def get_post(self, post_id):
        for post in self.get_all_posts():
            if post['id'] == post_id:
                return post

            
    

# p = Post()
# print(p.get_post(3))
