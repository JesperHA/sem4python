import requests
import threading
import time

class NotFoundException(Exception):
    pass

class Bookdl():
    def __init__(self, url_list):
        self.url_list = url_list
        self.filelist = []
        self.filelist_generator(self.url_list)
        self.index = 0

    def download(self, url, filename):
        start_time = time.time()

        r = requests.get(url)
        if requests.status_codes == 404:
            raise NotFoundException()
        open(filename, 'wb').write(r.content)

        execution_time = time.time() - start_time

        print("downloaded in: ", execution_time, " seconds")

        


    def multi_download(self, url_list):
        start_time = time.time()
        books.filelist_generator(url_list)

        for i in range(len(url_list)):

            bookname = "book" + str(i) + ".txt"
            x = threading.Thread(target=books.download, args=(books.url_list[i], bookname))
            # self.filelist.append(bookname)
            x.start()
            
        
        execution_time = time.time() - start_time

        
        print("multi downloaded in: ", execution_time, " seconds")


    def __iter__(self):
        return self
    def __next__(self):

        try:
            filename = self.filelist[self.index]

            f = open(filename, "r")
            content = f.read()

        except IndexError:
            raise StopIteration
        self.index += 1
        return content


    def filelist_generator(self, url_list):
        for i in range(len(url_list)):

            bookname = "book" + str(i) + ".txt"
            
            self.filelist.append(bookname)


    def avg_vowels(self, text):

        vowel_count = 0
        word_count = len(text.split())

        vowels='aeiouAEIOU'
    
        for s in text:
            if s in vowels: vowel_count = vowel_count + 1

        avg_vowels = vowel_count / word_count

        return avg_vowels


    def hardest_read(self):
        filename = "x"
        return filename




urls = ["http://www.gutenberg.org/cache/epub/61526/pg61526.txt", "http://www.gutenberg.org/files/23471/23471-8.txt", "http://www.gutenberg.org/files/23541/23541.txt"]
books = Bookdl(urls)

books.multi_download(books.url_list)


myit = iter(books)

books.avg_vowels(next(myit))
books.avg_vowels(next(myit))
books.avg_vowels(next(myit))


