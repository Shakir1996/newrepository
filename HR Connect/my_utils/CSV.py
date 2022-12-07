class HandleCSV:
    filename = "https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784.js"
    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            return foo.readlines()
    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()
obj=HandleCSV()
print(obj.filename)
#TODO - ADD MORE SUCH METHODS HERE
#TODO - UNDERSTAND USAGE OF `classmethod` HERE