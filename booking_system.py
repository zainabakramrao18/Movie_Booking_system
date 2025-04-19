class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def __str__(self):
        return f"{self.seat_number}{' (Booked)' if self.is_booked else ''}"


class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration  # in minutes

    def __str__(self):
        return f"{self.title} ({self.duration} mins)"


class Theater:
    def __init__(self, name, seats_count):
        self.name = name
        self.seats = [Seat(i+1) for i in range(seats_count)]
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        for idx, movie in enumerate(self.movies, 1):
            print(f"{idx}. {movie}")

    def show_available_seats(self):
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


class BookingSystem:
    def __init__(self):
        self.theater = Theater("CineMax", 10)  # Simple 10-seat theater

    def setup(self):
        # Add sample movies
        self.theater.add_movie(Movie("Inception", 148))
        self.theater.add_movie(Movie("The Matrix", 136))
        self.theater.add_movie(Movie("Interstellar", 169))

    def start(self):
        self.setup()
        print("Welcome to the Movie Ticket Booking System\n")
        while True:
            print("\n1. View Movies\n2. View Available Seats\n3. Book a Seat\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.theater.display_movies()
            elif choice == '2':
                self.theater.show_available_seats()
            elif choice == '3':
                try:
                    seat_num = int(input("Enter seat number to book: "))
                    self.theater.book_seat(seat_num)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                print("Thank you for using the booking system!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the system
if __name__ == "__main__":
    system = BookingSystem()
    system.start()
