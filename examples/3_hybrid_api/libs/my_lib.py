class MyLib:
    def get_keyword_names(self):
        return ['my_keyword', 'external_keyword']

    def my_keyword(self, arg):
        print("My Keyword called with '%s'" % arg)

    def __getattr__(self, name):
        if name == 'external_keyword':
            return self.my_keyword
        raise AttributeError("Non-existing attribute '%s'" % name)