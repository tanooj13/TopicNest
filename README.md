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
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open the app at `http://127.0.0.1:8000/` in your browser.

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users and rooms.  
- Register or log in to participate in discussions.

## Contributing

Feel free to fork the repo, submit issues, and create pull requests. Contributions are welcome!

