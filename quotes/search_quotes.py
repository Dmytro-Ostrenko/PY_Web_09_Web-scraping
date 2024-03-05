from mongoengine import connect
from models import Quote, Author

# Підключення до MongoDB Atlas
connect('PYHW9', host='mongodb+srv://dmytroostrenko:DRZ105T6tvRVV0Sh@cluster0.gjov9oo.mongodb.net/PYHW9')



def search_quotes(command):
    if command.startswith('name:'):
        author_name = command.split(':')[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(f"{quote.author.fullname}: {quote.quote}")
        else:
            print(f"Для автора '{author_name}' цитат не знайдено .")
    elif command.startswith('tag:'):
        tag = command.split(':')[1].strip()
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(f"{quote.author.fullname}: {quote.quote}")
    elif command.startswith('tags:'):
        tags = command.split(':')[1].strip().split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(f"{quote.author.fullname}: {quote.quote}")
    else:
        print("Невірна команда")


if __name__ == "__main__":
    while True:
        command = input("Оберіть вашу команду (Можливі варіанти: name: author_name, tag: tag_name, tags: tag1,tag2, exit для завершення): ").strip()
        if command.lower() == 'exit':
            break
        search_quotes(command)