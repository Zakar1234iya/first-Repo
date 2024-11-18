from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users, Authors, Books, Reviews
import bcrypt

# Display the home page with login and registration options
def home(request):
    # Context to pass to the template. Here, 'page_title' is a key, and 'DojoReads || Login or Register!' is its value.
    context = {
        'page_title': 'DojoReads || Login or Register!'
    }
    # Render the 'register_and_login.html' template with the given context.
    return render(request, 'html/register_and_login.html', context)

# Handle the registration of a new user
def register_new_user(request):
    if request.method == 'POST':  # Check if the request method is POST.
        # Validate user input using basic_validation method of Users model manager.
        errors = Users.objects.basic_validation(request.POST)
        if len(errors) > 0:  # If there are any validation errors.
            # Loop through each error and add it to messages.
            for key, value in errors.items():
                messages.error(request, value, extra_tags='danger')
            # Redirect back to the home page if there are errors.
            return redirect('home')

        # Extract and hash the password using bcrypt.
        prehash_pw = request.POST['password']
        hashed_pw = bcrypt.hashpw(prehash_pw.encode(), bcrypt.gensalt()).decode()

        # Create a new user with the provided data.
        newuser = Users.objects.create_user(
            name=request.POST['name'],
            alias=request.POST['alias'],
            email=request.POST['email'],
            password=hashed_pw
        )

        # Print a debug message for the newly created user.
        print(f'USER NUMBER {newuser.id} CREATED.')
        # Set session variables for the new user.
        request.session['userid'] = newuser.id
        request.session['loggedin'] = True
        # Add a success message.
        messages.success(request, f"User {request.POST['alias']} has been created successfully!")
        # Redirect to the book reviews page.
        return redirect('book_reviews')
    else:
        # If the request method is not POST, add an error message.
        messages.error(request, 'Invalid request. Please register or log in.', extra_tags='danger')
        return redirect('home')

# Handle user login
def login(request):
    if request.method == 'POST':  # Check if the request method is POST.
        # Filter the Users model by the provided email.
        user = Users.objects.filter(email=request.POST['email']).first()
        # If a user is found and the password matches.
        if user and bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            # Set session variables for the logged-in user.
            request.session['userid'] = user.id
            request.session['loggedin'] = True
            # Print a debug message.
            print(f'USER ID {user.id} LOCATED, PASSWORD VERIFIED.')
            # Add a success message.
            messages.success(request, f"Congrats! User {user.alias} has logged in!")
            # Redirect to the book reviews page.
            return redirect('book_reviews')
        else:
            # If login fails, add an error message.
            messages.error(request, 'Unable to log in. Check email and password.', extra_tags='danger')
            return redirect('home')
    else:
        # If the request method is not POST, add an error message.
        messages.error(request, 'Invalid request. Please register or log in.', extra_tags='danger')
        return redirect('home')

# Handle user logout
def logout(request):
    # Clear the session.
    request.session.flush()
    request.session['loggedin'] = False
    return redirect('home')

# Display book reviews
def book_reviews(request):
    if request.session.get('loggedin'):  # Check if the user is logged in.
        context = {
            'page_title': 'Recent Book Reviews!',
            'current_user': Users.objects.get(id=request.session['userid']),
            'reviews': Reviews.objects.all().order_by("-created_at"),  # Fetch all reviews, ordered by creation date.
            'books': Books.objects.all(),  # Fetch all books.
        }
    else:
        context = {'page_title': 'Recent Book Reviews!'}
    return render(request, 'html/book_reviews.html', context)

# Display the form to add a book review
def add_book_review(request):
    if not request.session.get('loggedin'):  # Check if the user is not logged in.
        # Add an error message if the user is not logged in.
        messages.error(request, 'You must be logged in to add book reviews. Please log in!', extra_tags='danger')
        return redirect('home')
    else:
        context = {
            'page_title': 'Add A Book & Review!',
            'current_user': Users.objects.get(id=request.session['userid']),  # Fetch the current user.
            'authors': Authors.objects.all()  # Fetch all authors.
        }
        return render(request, 'html/new_book.html', context)

# Display the reviews of a specific book
def view_book(request, bookid):
    # Fetch the book information.
    book_info = Books.objects.get(id=bookid)
    context = {
        'page_title': f'{book_info.title} | Reviews!',
        'book_info': book_info,
        'user_info': Users.objects.get(id=request.session['userid'])  # Fetch the current user.
    }
    return render(request, 'html/view_reviews.html', context)

# Display the profile of a specific user
def view_profile(request, userid):
    # Fetch user data and their reviews.
    user_data = Users.objects.get(id=userid)
    reviews = user_data.reviews.all()
    context = {
        'page_title': f'{user_data.alias} | Profile!',
        'user': user_data,
        'reviews': reviews,
    }
    return render(request, 'html/user_profile.html', context)

# Display a confirmation page before deleting a review
def confirm_delete(request, reviewid):
    context = {'review_id': reviewid}
    return render(request, 'html/confirm_delete.html', context)

# Handle the addition of a review for an existing book
def review_existing_book(request, bookid):
    if request.method == 'POST':
        # Validate review data.
        review_errors = Reviews.objects.basic_validation(request.POST)
        if len(review_errors) > 0:
            # If there are validation errors, display them to the user.
            for key, value in review_errors.items():
                messages.error(request, value, extra_tags='danger')
            return redirect('view_book', bookid)
        
        # Create review.
        Reviews.objects.create_review(
            review=request.POST['bookreview'],
            rating=request.POST['bookrating'],
            user_id=request.session['userid'],
            book_id=bookid
        )
        # Add a success message.
        messages.success(request, f"Woot! You have reviewed the book!")
        return redirect('view_book', bookid)
    else:
        # If the request method is not POST, add an error message.
        messages.error(request, 'Invalid request. Returning you to the main page.', extra_tags='danger')
        return redirect('book_reviews')


# Handle the process of adding a new book and its review
def process_new_book_review(request):
    if request.method == 'POST':
        # Validate book data.
        book_errors = Books.objects.basic_validation(request.POST)
        # Validate review data.
        review_errors = Reviews.objects.basic_validation(request.POST)
        # Validate author data if adding a new author.
        author_errors = Authors.objects.basic_validation(request.POST) if request.POST['bookauthorselect'] == '-1' else {}
        
        # Check for any validation errors.
        if book_errors or review_errors or author_errors:
            errors = {**book_errors, **review_errors, **author_errors}
            # If there are validation errors, display them to the user.
            for key, value in errors.items():
                messages.error(request, value, extra_tags='danger')
            return redirect('add_book_review')
        
        # Create new author if needed.
        if request.POST['bookauthorselect'] == '-1':
            author = Authors.objects.create_author(name=request.POST['bookauthoradd'])
        else:
            author = Authors.objects.get(id=request.POST['bookauthorselect'])
        
        # Get the user adding the book.
        user = Users.objects.get(id=request.session['userid'])
        # Create the book.
        book = Books.objects.create_book(title=request.POST['booktitle'], author=author)
        # Create the review for the book.
        Reviews.objects.create_review(
            review=request.POST['bookreview'],
            rating=request.POST['bookrating'],
            user_id=user.id,
            book_id=book.id
        )
        # Add a success message.
        messages.success(request, f"Woot! You have reviewed {book.title}!")
        return redirect('view_book', book.id)
    else:
        # If the request method is not POST, add an error message.
        messages.error(request, 'Invalid request. Returning you to the main page.', extra_tags='danger')
        return redirect('book_reviews')

# Handle the deletion of a review
def delete_review(request, reviewid):
    # Fetch the review to be deleted.
    Reviews.objects.get(id=reviewid).delete()
    # Add a success message.
    messages.success(request, 'Welp, that review has successfully sent to the ether. Ja ni.')
    return redirect('book_reviews')



