# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  # Encapsulated attribute (protected)

    def read(self):
        print(f"Reading '{self.title}' by {self.author}. Total pages: {self._pages}")

    def get_pages(self):
        return self._pages

    def set_pages(self, new_page_count):
        if new_page_count > 0:
            self._pages = new_page_count
        else:
            print("Page count must be positive.")

# Subclass
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # In megabytes

    # Polymorphism: override read method
    def read(self):
        print(f"Opening eBook '{self.title}' on your device. Size: {self.file_size}MB")

    def download(self):
        print(f"Downloading '{self.title}'... Done!")

# Example usage
book1 = Book("Sapiens", "Yuval Noah Harari", 498)
ebook1 = EBook("Atomic Habits", "James Clear", 320, 2.8)

book1.read()
print("Pages:", book1.get_pages())
book1.set_pages(500)
print("Updated Pages:", book1.get_pages())

print()

ebook1.read()
ebook1.download()

#Polymorphism
class Vehicle:
    def move(self):
        print("This vehicle moves in a general way.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water. 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
