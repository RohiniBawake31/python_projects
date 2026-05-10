# Movie Booking system
class MOVIEBOOKING:
    def __init__(self):
        self.movies=["shershah","sanam teri kasam","border2","diwaniyat"]
        self.available_seats=[1,2,3,4,5,6,8,9,10]
        self.booked_seats=[]


    # Show available movie list
    def available_movies(self):
        print("Available Movies:")
        for movie in self.movies:
            print(movie)

    # For ticket booking
    def book_ticket(self,seat_no):
        print("Available seats:", self.available_seats)
        if seat_no in self.available_seats:
            self.available_seats.remove(seat_no)
            self.booked_seats.append(seat_no)
            print(f"Seat {seat_no} booked successfully")
        else:
            print("Seat not available")
        print("Updated available seats:", self.available_seats)
        
    # Booking cancel
    def cancel_ticket(self,seat_cancel):
        print("Booked seats:", self.booked_seats)
        if seat_cancel in self.booked_seats:
            self.booked_seats.remove(seat_cancel)
            self.available_seats.append(seat_cancel)
            print("Seat cancelled successfully")
        else:
            print("Invalid seat number")
        print("Booked seats:", self.booked_seats)

 
if __name__ == "__main__":
    menu=MOVIEBOOKING()
    menu.available_movies()
    menu.book_ticket(10)
    menu.cancel_ticket(10)
    


