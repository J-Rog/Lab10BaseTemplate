class Book:
    def __init__(self,title,author,length,rating):
        self.title = title
        self.author = author
        self.length = length
        self.rating = rating


    def __add__(self,other):
        return self.length + other.length
    def __sub__(self, other):
        print("This behaivor is undefined")
    def __eq__(self,other):
        return self.rating == other.rating
    def __lt__(self,other):
        return self.length > other.length
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nLength: {self.length}\nRating: {self.rating}\n"
    def __repr__(self):
        return f"Book(title={self.title},author={self.author},length={self.length},rating={self.rating})"
