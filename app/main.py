from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = []
    for person in customers:
        customer = Customer(person["name"], person["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(movie, customer_instances, cleaning_staff)
