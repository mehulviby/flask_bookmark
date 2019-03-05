from bookmark import create_app, db
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('BOOKMARK_ENV') or 'dev')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


# @manager.command
# def insert_db():
#     mehul = User(username="mehul", email="mehul@gmail.com", password="test")
#     db.session.add(mehul)

#     def add_bookmark(url, description, tags):
#         db.session.add(Bookmark(url=url, description=description,
#                                 user=mehul, tags=tags))
#     for name in ["python", "flask", "webdev", "programming", "emacs", "go", "golang", "javascript", "dev", "angularjs", "django", "databases", "orm", "training"]:
#         db.session.add(Tag(name=name))
#     db.session.commit()
#     add_bookmark("http://www.pluralsight.com", "Pluralsight. Hardcore developer training.",
#                  "training,programming,python,flask,webdev")
#     add_bookmark("http://www.python.org",
#                  "Python - my favorite language", "python")
#     add_bookmark("http://flask.pocoo.org",
#                  "Flask: Web development one drop at a time.", "python,flask,webdev")
#     add_bookmark("http://www.reddit.com",
#                  "Reddit. Frontpage of the internet", "news,coolstuff,fun")
#     add_bookmark("http://www.sqlalchemyorg",
#                  "Nice ORM framework", "python,orm,databases")
#     add_bookmark("https://golang.org/doc/effective_go.html",
#                  "Effective Go: The Go programming language", "go,golang,programming,dev")
#     add_bookmark("https://angularjs.org/",
#                  "AngularJS: The Superhoic javascript MVW framework", "javascript,angularjs")
#     add_bookmark("https://emacswiki.org/",
#                  "Wiki for my favorite editor", "emacs")
#     test = User(username="test",
#                      email="test@test.com", password="test")
#     db.session.add(test)
#     db.session.commit()
#     print("Initialized the database")


# @manager.command
# def dropdb():
#     if prompt_bool("Are you sure you wnat to lose all the your data"):
#         db.drop_all()
#         print("Dropped the database")
