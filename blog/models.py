from django.db.models import Model, CharField

class Post(Model):
    title = CharField(max_length=225)
    #review
    # body = model здесь поле для заполнения
    def __str__(self):
        return self.title


class Case(Model):
    title = CharField(max_length=225)
    link = CharField(max_length=325)

    def __str__(self):
        return self.title
