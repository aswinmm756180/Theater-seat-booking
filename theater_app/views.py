from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    return render(request,"index.html")


####useruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruseruser####
def user_reg(request): 
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("password")
        passw2 = request.POST.get("password1")
        email = request.POST.get("email")
    
        
        if passw1 == passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'user/register.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    email=email,
                    is_user=True 
                )
                user.save()
                
                # Add a success message
                messages.success(request, 'Registration successful.')
                return redirect('user_login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('user_reg')
    else:
            return render(request, 'user/register.html')
    




def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username=uname, password=passw)
        if user is not None and user.is_user:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "user/login.html")
    


def home(request):
    return render (request,"user/user_home.html")


def logout_view(request):
    logout(request)
    return redirect('index')



def view_all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'user/view_all_movies.html', {'movies': movies})



from django.shortcuts import render, get_object_or_404
from .models import Movie

def theaters_by_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    theaters = movie.theaters.all()
    return render(request, 'user/theaters_by_movie.html', {'movie': movie, 'theaters': theaters})


from django.shortcuts import render, get_object_or_404
from .models import Movie, Theater

from django.shortcuts import render, get_object_or_404
from .models import Movie, Theater, Seat

def theater_seat_booking(request, movie_id, theater_id, time_slot):
    movie = get_object_or_404(Movie, pk=movie_id)
    theater = get_object_or_404(Theater, pk=theater_id)
    # Assuming you have a Seat model representing each seat in the theater
    seats = Seat.objects.filter(theater=theater, time_slot=time_slot)
    return render(request, 'user/seat_booking.html', {'movie': movie, 'theater': theater, 'time_slot': time_slot, 'seats': seats})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Theater, Seat, Booking
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal

@login_required
def theater_seat_booking(request, movie_id, theater_id, time_slot):
    movie = get_object_or_404(Movie, pk=movie_id)
    theater = get_object_or_404(Theater, pk=theater_id)
    
    # Retrieve the actual time for the specified time slot
    if time_slot == 'time_slot_1':
        time = theater.time_slot_1
    elif time_slot == 'time_slot_2':
        time = theater.time_slot_2
    elif time_slot == 'time_slot_3':
        time = theater.time_slot_3
    elif time_slot == 'time_slot_4':
        time = theater.time_slot_4
    else:
        time = None
    
    seats = Seat.objects.filter(theater=theater, time_slot=time_slot)
    context = {
        'movie': movie,
        'theater': theater,
        'time_slot': time,  # Pass the actual time instead of slot name
        'seats': seats
    }
    return render(request, 'user/seat_booking.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Booking, Seat
from decimal import Decimal

@login_required
def book_seat(request):
    if request.method == 'POST':
        selected_seat_numbers_str = request.POST.get('selected_seats', '')
        selected_seat_numbers = selected_seat_numbers_str.split(',')
        theater_id = request.POST.get('theater_id')
        movie_id = request.POST.get('movie_id')
        time_slot = request.POST.get('time_slot')
        total_amount = request.POST.get('total_amount', 0)  # Default to 0 if not found
        
        # Create a booking instance and save to the database
        booking = Booking.objects.create(user=request.user, total_amount=total_amount, theater_id=theater_id, movie_id=movie_id, time_slot=time_slot)
        booking.booked_seat_numbers = selected_seat_numbers_str
        booking.save()
        
        # Redirect to booking confirmation with the booking ID
        return redirect('booking_confirmation', booking_id=booking.id)
    else:
        # Retrieve booked seats from the database
        booked_seats = Booking.objects.values_list('booked_seat_numbers', flat=True).filter(
            theater_id=request.POST.get('theater_id'),
            movie_id=request.POST.get('movie_id'),
            time_slot=request.POST.get('time_slot')
        ).first()
        
        # Pass booked seats to the template
        context = {
            'booked_seats': booked_seats.split(',') if booked_seats else None
        }
        return render(request, 'user/seat_booking.html', context)




def calculate_total_amount(selected_seat_numbers):
    total_amount = 0
    for seat_number in selected_seat_numbers:
        if seat_number.strip():
            try:
                seat = Seat.objects.get(pk=int(seat_number))
                if int(seat.seat_number) <= 60:
                    total_amount += 100
                else:
                    total_amount += 200
            except (ValueError, ObjectDoesNotExist):
                pass
    return Decimal(total_amount)

def get_total_amount(selected_seat_numbers):
    return calculate_total_amount(selected_seat_numbers)



from django.shortcuts import render, get_object_or_404
from .models import Booking

def view_booking_details(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(Booking, id=booking_id)
        return render(request, 'user/view_booking_details.html', {'booking': booking})
    return render(request, 'user/view_booking_details.html')





@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    # You may need to calculate the total amount for seats separately if it's not stored in the Booking model
    seat_total_amount = calculate_total_amount(booking.booked_seat_numbers)
    context = {
        'booking': booking,
        'seat_total_amount': seat_total_amount,
    }
    return render(request, 'user/booking_confirmation.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'user/user_bookings.html', context)

def delete_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, pk=booking_id)
        # Check if the booking belongs to the logged-in user
        if booking.user == request.user:
            # Delete the booking
            booking.delete()
            return redirect('user_bookings')
        else:
            # Unauthorized access
            return redirect('user_bookings')
    else:
        # Handle GET request method
        return redirect('user_bookings')


from django.shortcuts import render
from .models import Theater

def all_theaters(request):
    theaters = Theater.objects.all()
    context = {
        'theaters': theaters
    }
    return render(request, 'user/all_theaters.html', context)


def payment(request):
    return render (request,"user/payment.html")

####managermanagermanagermanagermanagermanagermanagermanagermanagermanagermanagermanagerrmanagermanagermanager####


def manager_reg(request): 
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("password")
        passw2 = request.POST.get("password1")
        email = request.POST.get("email")
    
        
        if passw1 == passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'manager/register.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    email=email,
                    is_manager=True 
                )
                user.save()
                
                # Add a success message
                messages.success(request, 'Registration successful.')
                return redirect('manager_login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('manager_reg')
    else:
            return render(request, 'manager/register.html')
    
def manager_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username=uname, password=passw)
        if user is not None and user.is_manager:
            login(request, user)
            return redirect('manager_home') 
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "manager/login.html")
 

def manager_home(request):
    return render(request,"manager/manager_home.html")


def manager_logout(request):
    logout(request)
    return redirect('index')






from django.shortcuts import render, redirect
from .models import Movie  # Assuming you have a Category model defined



def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('view_movie')

# def add_theater(request):
#     return render(request,"manager/add_theater.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie, Theater

def add_theater(request):
    if request.method == 'POST':
        theater_name = request.POST.get('name')
        movie_id = request.POST.get('movie')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        time_slot_1 = request.POST.get('time_slot_1')
        time_slot_2 = request.POST.get('time_slot_2')
        time_slot_3 = request.POST.get('time_slot_3')
        time_slot_4 = request.POST.get('time_slot_4')
        
        admin = request.user if request.user.is_authenticated else None
        if admin:
            try:
                movie = Movie.objects.get(pk=movie_id)
            except Movie.DoesNotExist:
                messages.error(request, 'Selected movie does not exist.')
                return redirect('add_theater')
            
            theater = Theater.objects.create(
                theater_name=theater_name,
                movie=movie,
                location=location,
                image=image,
                manager_theater=admin,
                time_slot_1=time_slot_1,
                time_slot_2=time_slot_2,
                time_slot_3=time_slot_3,
                time_slot_4=time_slot_4,
            )
            theater.save()
            messages.success(request, 'Theater added successfully.')
            return redirect('view_theater')
        else:
            messages.error(request, 'Please log in to add theaters.')
            return redirect('manager_home')
    
    if request.user.is_authenticated:
        films = Movie.objects.all()
        return render(request, 'manager/add_theater.html', {'films': films})
    else:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('manager_home')


def view_theater(request):
    # Get the current logged-in user's ID
    manager_id = request.user.id
    # Filter events by manager ID
    theaters = Theater.objects.filter(manager_theater_id=manager_id)

    return render(request, 'manager/view_theater.html', {'theaters': theaters})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Theater

def edit_theater(request, theater_id):
    theater = get_object_or_404(Theater, pk=theater_id)
    if request.method == 'POST':
        theater_name = request.POST.get('name')
        location = request.POST.get('location')
        time_slot_1 = request.POST.get('time_slot_1')
        time_slot_2 = request.POST.get('time_slot_2')
        time_slot_3 = request.POST.get('time_slot_3')
        time_slot_4 = request.POST.get('time_slot_4')
        
        theater.theater_name = theater_name
        theater.location = location
        theater.time_slot_1 = time_slot_1
        theater.time_slot_2 = time_slot_2
        theater.time_slot_3 = time_slot_3
        theater.time_slot_4 = time_slot_4
        theater.save()
        messages.success(request, 'Theater updated successfully.')
        return redirect('view_theater')
    
    return render(request, 'manager/edit_theater.html', {'theater': theater})


def delete_theater(request, id):
    theater = Theater.objects.get(id=id)
    theater.delete()
    return redirect('view_theater')



from django.shortcuts import render
from .models import Booking, Theater

def manager_booking_page(request):
    theaters = Theater.objects.filter(manager_theater=request.user)
    return render(request, 'manager/manager_booking_page.html', {'theaters': theaters})

# def theater_booking_page(request, theater_id):
#     theater = Theater.objects.get(id=theater_id)
#     bookings = Booking.objects.filter(theater=theater).order_by('time_slot')
#     return render(request, 'manager/theater_booking_page.html', {'theater': theater, 'bookings': bookings})
from django.shortcuts import render
from .models import Booking

def theater_booking_page(request, theater_id):
    theater = Theater.objects.get(id=theater_id)
    query = request.GET.get('search_query')
    if query:
        bookings = Booking.objects.filter(theater=theater, id__icontains=query)
    else:
        bookings = Booking.objects.filter(theater=theater)
    return render(request, 'manager/theater_booking_page.html', {'theater': theater, 'bookings': bookings})


from django.shortcuts import render, get_object_or_404
from .models import Booking

def view_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'manager/view_booking.html', {'booking': booking})


####adminadminadminadminadminadminadminadminadminadminadminadminadminadminadminadminadminadminadminadminadminadmin####

def admin_reg(request): 
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    email=email,
                    is_admin=True 
                )
        user.save()
        messages.success(request, 'Registration successful.')
        return redirect('admin_login')
       
    else:
            return render(request, 'admin/register.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_admin:
            login(request, user)
            return redirect('admin_panel')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, "admin/login.html")


def admin_panel(request):
    return render(request,"admin/admin_panel.html")





def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('movie_name')
        description = request.POST.get('movie_Description')
        image = request.FILES.get('movie_image')
        admin_id = request.user.id if request.user.is_authenticated else None
        
        movie = Movie(
            name=name,
            Description=description,
            image=image, 
            admin_id=admin_id,
        )
        movie.save()
        return redirect('view_movie')  # Redirect to another view after saving the movie

    # Fetch movies added by the admin
    films = Movie.objects.filter(admin_id=request.user.id) if request.user.is_authenticated else []
    
    return render(request, 'admin/add_movie.html', {'films': films})

@login_required
def view_movie(request):
    films = Movie.objects.filter(admin =request.user)
    return render(request, 'admin/view_movie.html', {'films': films})

from django.shortcuts import render
from .models import User  # Import your custom User model

def view_all_users(request):
    users = User.objects.filter(is_user=True)
    return render(request, 'admin/view_all_users.html', {'users': users})

def view_all_managers(request):
    managers = User.objects.filter(is_manager=True)
    return render(request, 'admin/view_all_managers.html', {'managers': managers})


def view_all_theaters(request):
    theaters = Theater.objects.all()
    return render(request, 'admin/view_all_theaters.html', {'theaters': theaters})



def logout_admin(request):
    logout(request)
    return redirect('index')



from django.shortcuts import render, redirect
from .models import Booking

def view_all_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'admin/view_all_bookings.html', {'bookings': bookings})


from django.shortcuts import render, redirect
from .models import Userchat
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def user_chat(request):
    if request.method == 'POST':
        chat_text = request.POST.get('userchat')  
        user_instance = request.user
        chat = Userchat.objects.create(
            chat=chat_text,
            user=user_instance,
        )
        chat.save()
        # Redirect the user to another page after the chat is saved
        return redirect('user_chat')

    messages = Userchat.objects.all()
    return render(request, 'User/user_chat.html', {'messages': messages})

@login_required
def delete_message(request, message_id):
    message = Userchat.objects.get(id=message_id)
    if message.user == request.user:  # Check if the logged-in user owns the message
        message.delete()
    return redirect('user_chat')

@login_required
def delete_all_messages(request):
    Userchat.objects.filter(user=request.user).delete()
    return redirect('manager_chat')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Userchat
from django.contrib.auth import get_user_model

@login_required
def manager_chat(request):
    if request.method == 'POST':
        chat_text = request.POST.get('managerchat')
        # Assuming there's only one manager for simplicity
        manager_instance = get_user_model().objects.filter(is_manager=True).first()
        chat = Userchat.objects.create(
            chat=chat_text,
            user=manager_instance,
        )
        chat.save()
        # Redirect the user to another page after the chat is saved
        return redirect('manager_chat')

    messages = Userchat.objects.all()
    return render(request, 'manager/manager_chat.html', {'messages': messages})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Userchat

@login_required
def delete_chat(request, chat_id):
    chat = get_object_or_404(Userchat, pk=chat_id)
    # Check if the user has permission to delete the chat
    if request.user == chat.user:
        chat.delete()
    # Redirect the user to another page after deleting the chat
    return redirect('manager_chat')  # Or whichever page you want to redirect to
