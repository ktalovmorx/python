import os

def save(function):
    def wrapper(content, message):
        with open('topics.html', 'wt') as wt:
            wt.write(function(content,message))
    return wrapper

def layout(function):
    def wrapper(content, message):
        with open('layout.txt', 'rt') as rt:
            return rt.read().format(function(content,message))
    return wrapper

def hTag(function):
    def wrapper(content, message):
        return f"<h1 style='color:red' title='{message}'>{content}</h1>"
    return wrapper

@save
@layout
@hTag
def createHTML(content, message):
    return content,message

createHTML('Programming Topics New','Hello World')
os.system('start topics.html')
#save(layout(hTag(createHTML())))
