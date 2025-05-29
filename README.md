# Topic NEST

**Topic NEST** is a real-time discussion platform built with Django, enabling users to join topic-specific rooms for seamless conversations.

## Features

- **Real-Time Messaging**: Engage in live discussions within dedicated topic rooms.
- **User Authentication**: Secure login and registration system for personalized experiences.
- **Room Management**: Create and manage rooms tailored to various topics.
- **Responsive Design**: Optimized UI for both desktop and mobile devices.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tanooj13/TopicNest.git
   cd TopicNest
Set up a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Access the application at http://127.0.0.1:8000/.

Usage
Admin Panel: Access the admin panel at http://127.0.0.1:8000/admin/ to manage users and rooms.

User Interaction: Register or log in to participate in discussions.

Contributing
Feel free to fork the repository, submit issues, and create pull requests. Contributions are welcome!
