class PaginatedResults:

    def __init__(self, pages):
        self.pages = pages
        self.currentIndex = 0
        self.ndx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current = self.pages[self.currentIndex]
            if not current:
                self.currentIndex += 1
                self.ndx = 0
                return next(self)
            currentServer = current[self.ndx]
            self.ndx += 1
            return currentServer
        except StopIteration:
            raise StopIteration
        except IndexError:
            if len(self.pages) > self.currentIndex:
                self.currentIndex += 1
                self.ndx = 0
                return next(self)
            else:
                raise StopIteration