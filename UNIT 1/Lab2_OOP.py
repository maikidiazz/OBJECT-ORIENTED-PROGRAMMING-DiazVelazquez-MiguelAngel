class name:
    def _init_(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.__password = password
    
def login(self):
    print(f"el usuario se conecto correctamente ({self.email}) y la contraseña ({self.__password})")

class post:
    def _init_(self, author, comments, text):
        self.author = author
        self.comments = comments
        self.text = text
    def create_post(self):
        print(f"{self.author} posts {self.text}")
class comments:
    def _init_(self, author, comments, post):
        self.author = author
        self.comments = comments
        self.post = post
    def create_comment(self):
        print(f"{self.author} makes a comment under {self.post}")
class message:
    def _init_(self, author, receipient, text):
        self.author = author
        self.receipient = receipient
        self.text = text
    def send_message(self):
        print(f"{self.author} sends {self.text} to {self.receipient}")


post1 = post("Pelon123", "1", "yesyesyes")
comments1 = comments("diegogogo", "01234", "lololol")
message1 = message("jadelonjas", "caca de burro", "hello, how are you?")

post1.create_post( )
comments1.create_comment( )
message1.send_message( )