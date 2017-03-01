class Duck:
    def __init__(self, string):
        self.string = string

    def title(self):
        print("Inside title of class")


d = Duck("aagam")
d.title()

print("aagam".title())
