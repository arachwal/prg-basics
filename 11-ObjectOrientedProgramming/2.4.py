class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'username: {self.username}')
        for i in range(len(self.posts)):
            for j in range(len(self.posts[i])):
                print(f'post: {self.posts[i][j]}')

timeline=SocialMediaProfile('johndoe')
content='Hello, world!','Had a great day at the park!','Whats up, Natalie? How are you?'
timeline.add_post(content)

timeline.display_timeline()