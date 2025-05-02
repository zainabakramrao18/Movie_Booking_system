# ----- User Login System -----
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.booking_history = []  # New: Stores instances of Booking
        


class UserSystem:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def register(self):
        username = input("Enter a new username: ")
        if username in self.users:
            print("Username already exists. Try a different one.")
            return
        password = input("Enter a password: ")
        self.users[username] = User(username, password)
        print("Registration successful!")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        user = self.users.get(username)
        if user and user.password == password:
            self.logged_in_user = user
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password.")

    def logout(self):
        if self.logged_in_user:
            print(f"Logged out {self.logged_in_user.username}")
            self.logged_in_user = None
        else:
            print("No user is logged in.")

    def is_logged_in(self):
        return self.logged_in_user is not None


# ----- Booking System -----

class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def cancel(self):  # Added for canceling a booking
        if self.is_booked:
            self.is_booked = False
            return True
        return False

    def __str__(self):
        return f"{self.seat_number}{' (Booked)' if self.is_booked else ''}"


class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration} mins)"


class Theater:
    def __init__(self, name, seats_count):
        self.name = name
        self.seats = [Seat(i + 1) for i in range(seats_count)]
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\nAvailable Movies:")
        for idx, movie in enumerate(self.movies, 1):
            print(f"{idx}. {movie}")

    def show_available_seats(self):
        print("\nAvailable Seats:")
        for seat in self.seats:
            print(seat, end='  ')
        print()

    def book_seat(self, seat_number):
        if 0 < seat_number <= len(self.seats):
            seat = self.seats[seat_number - 1]
            if seat.book():
                print(f"Seat {seat_number} booked successfully!")
            else:
                print(f"Seat {seat_number} is already booked.")
        else:
            print("Invalid seat number.")
    def cancel_seat(self, seat_number, user):  # Added for canceling a seat
        if 0 < seat_number <= len(self.seats):
            seat = self.seats[seat_number - 1]
            if seat.cancel():
                print(f"Seat {seat_number} booking canceled successfully!")
                user.booking_history.remove(seat_number)  # Remove from user's booking history
            else:
                print(f"Seat {seat_number} is not booked.")
        else:
            print("Invalid seat number.")

    def search_movie(self, title):  # Added for searching a movie
        for movie in self.movies:
            if title.lower() in movie.title.lower():
                print(f"Found: {movie}")
                return
        print("Movie not found.")

class BookingSystem:
    def __init__(self):
        self.user_system = UserSystem()
        self.theater = Theater("CineMax", 10)

    def setup(self):
        self.theater.add_movie(Movie("Inception", 148))
        self.theater.add_movie(Movie("The Matrix", 136))
        self.theater.add_movie(Movie("Interstellar", 169))

    def display_menu(self):
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. View Movies")
        print("4. View Available Seats")
        print("5. Book a Seat")
        print("6. Cancel a Booking")  # Added
        print("7. Search for a Movie")  # Added
        print("8. Admin Panel") #Added
        print("6. Logout")
        print("7. Exit")

    def start(self):
        self.setup()
        print("\n🎬 Welcome to the Movie Ticket Booking System 🎬")

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.user_system.register()

            elif choice == '2':
                self.user_system.login()

            elif choice == '3':
                if self.check_login():
                    self.theater.display_movies()

            elif choice == '4':
                if self.check_login():
                    self.theater.show_available_seats()

            elif choice == '5':
                if self.check_login():
                    self.handle_seat_booking()
            
            elif choice == '6':  # Added
                if self.check_login():
                    self.handle_seat_cancellation()

            elif choice == '7':  # Added
                if self.check_login():
                    self.search_movie()

            elif choice == '8':  # Added
                self.admin_panel()

            elif choice == '9':
                self.user_system.logout()

            elif choice == '10':
                print("Thank you for using the system! Goodbye! 👋")
                break

            else:
                print("Invalid choice. Please try again.")

    def check_login(self):
        if not self.user_system.is_logged_in():
            print("Please login first.")
            return False
        return True

    def handle_seat_booking(self):
        try:
            seat_num = int(input("Enter seat number to book: "))
            movie_title = input("Enter movie title for the booking: ")
            if self.theater.book_seat(seat_num):
                booking = booking(
                    user=self.user_system.logged_in_user,
                    seat_number=seat_num,
                    movie_title=movie_title
            )
                self.user_system.logged_in_user.booking_history.append(booking)
        except ValueError:
            print("Please enter a valid number.")
    def view_booking_history(self):
        user = self.user_system.logged_in_user
        if user.booking_history:
            print("\nYour Booking History:")
            for booking in user.booking_history:
                print(booking)
        else:
            print("You have no bookings.")
        

    def search_movie(self):  # Added
        title = input("Enter movie title to search: ")
        self.theater.search_movie(title)

    def admin_panel(self):  # Added
        admin_password = "admin123"  # Example password
        password = input("Enter admin password: ")
        if password == admin_password:
            print("\nAdmin Menu:")
            print("1. Add Movie")
            print("2. Exit Admin Panel")
            choice = input("Enter your choice: ")
            if choice == '1':
                title = input("Enter movie title: ")
                duration = int(input("Enter movie duration (in minutes): "))
                self.theater.add_movie(Movie(title, duration))
                print(f"Movie '{title}' added successfully!")
            elif choice == '2':
                print("Exiting admin panel.")
            else:
                print("Invalid choice.")
        else:
            print("Incorrect password.")

# ----- Run the system -----

if __name__ == "__main__":
    system = BookingSystem()
    system.start()
