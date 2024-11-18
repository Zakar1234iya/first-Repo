from django.db import models
import re

# Manager for additional methods related to Users model
class UsersManager(models.Manager):
    # Validate user registration data
    def basic_validation(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Name needs to be at least 5 characters'
        if len(postData['alias']) < 5:
            errors['alias'] = 'Your alias needs to be at least 5 characters.'
        
        # Check if alias is unique
        if Users.objects.filter(alias=postData['alias']).exists():
            errors['alias2'] = 'Your alias already exists. Alias needs to be unique.'
        
        # Regular expression to validate email format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        
        # Check if email is unique
        if Users.objects.filter(email=postData['email']).exists():
            errors['email2'] = 'That email address already exists. Did you forget your password?'
        
        # Validate password length and match
        if len(postData['password']) < 8:
            errors['password'] = 'Your password must be at least 8 characters long.'
        if postData['confirm_password'] != postData['password']:
            errors['confirm_password'] = 'Password mismatch. Did you make a typo?'
        
        return errors

    # Create a new user
    def create_user(self, name, alias, email, password):
        return self.create(name=name, alias=alias, email=email, password=password)

# User model representing a user in the application
class Users(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()  # Attach the UsersManager to add additional methods

# Manager for additional methods related to Authors model
class AuthorsManager(models.Manager):
    # Validate author input
    def basic_validation(self, postData):
        errors = {}
        if postData['bookauthoradd'] and len(postData['bookauthoradd']) < 5:
            errors['author'] = 'Author name must be at least 5 characters long.'
        return errors

    # Create a new author
    def create_author(self, name):
        return self.create(name=name)

# Author model representing an author in the application
class Authors(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorsManager()  # Attach the AuthorsManager to add additional methods

# Manager for additional methods related to Books model
class BooksManager(models.Manager):
    # Validate book input
    def basic_validation(self, postData):
        errors = {}
        if Books.objects.filter(title=postData['booktitle']).exists():
            errors['title'] = 'Book title already exists. If this is a different book with the same title, please add the year published to the end of the title (e.g. Babe (1999)).'
        if len(postData['booktitle']) < 5:
            errors['title'] = 'Title must be at least 5 characters long.'
        return errors

    # Create a new book
    def create_book(self, title, author):
        return self.create(title=title, author=author)

# Book model representing a book in the application
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Authors, related_name="books", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BooksManager()  # Attach the BooksManager to add additional methods

# Manager for additional methods related to Reviews model
class ReviewsManager(models.Manager):
    # Validate review input
    def basic_validation(self, postData):
        errors = {}
        if len(postData['bookreview']) < 10:
            errors['bookreview'] = 'Reviews must be at least 10 characters long.'
        try:
            rating = int(postData['bookrating'])
            if rating < 1 or rating > 5:
                errors['bookrating'] = 'Rating is required and it must be between 1 and 5 stars.'
        except (ValueError, TypeError):
            errors['bookrating'] = 'A valid rating is required.'
        return errors

    # Create a new review
    def create_review(self, review, rating, user_id, book_id):
        user = Users.objects.get(id=user_id)
        book = Books.objects.get(id=book_id)
        return self.create(review=review, rating=rating, user=user, book=book)


# Review model representing a review in the application
class Reviews(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(Users, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Books, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewsManager()  # Attach the ReviewsManager to add additional methods



