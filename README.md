# ALX Travel App

This is a Django-based travel application that allows users to browse, book, and review property listings. It's a comprehensive solution for managing travel-related services, built with a robust backend and a clear structure for scalability.

## Features

-   **User Authentication**: Secure user registration and login.
-   **Property Listings**: Browse available properties with details.
-   **Booking System**: Book properties for specific dates.
-   **Reviews and Ratings**: Users can leave feedback on listings.
-   **Database Seeding**: A management command to populate the database with initial data.

## Technologies Used

-   **Backend**: Django, Django REST Framework
-   **Database**: SQLite3 (for development)
-   **Tooling**: Faker (for data generation)

## Project Structure

The project is organized into a main project directory `alx_travel_app` and a `listings` app that contains the core functionality.

```
alx_travel_app_0x00/
├── alx_travel_app/         # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── listings/               # Django app for listings
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── seed.py
├── requirements.txt
└── README.md
```

## Models

### `Listing`
Represents a property listing available for booking.
- `title` (CharField)
- `description` (TextField)
- `price` (DecimalField)
- `created_at` (DateTimeField)
- `updated_at` (DateTimeField)

### `Booking`
Represents a booking made by a user for a listing.
- `user` (ForeignKey to User)
- `listing` (ForeignKey to Listing)
- `check_in` (DateField)
- `check_out` (DateField)
- `guests` (PositiveIntegerField)
- `created_at` (DateTimeField)

### `Review`
Represents a review left by a user for a listing.
- `user` (ForeignKey to User)
- `listing` (ForeignKey to Listing)
- `rating` (PositiveIntegerField)
- `comment` (TextField)
- `created_at` (DateTimeField)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Jehoiada1/alx_travel_app_0x00.git
    cd alx_travel_app_0x00
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Seed the database:**
    ```bash
    python manage.py seed
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- `/api/listings/` - View all listings
- `/api/bookings/` - View all bookings
- `/api/reviews/` - View all reviews
