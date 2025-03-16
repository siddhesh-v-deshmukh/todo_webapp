# Flask To-Do App

This is a simple To-Do web application built using Flask and SQLAlchemy. It allows users to add, update, delete, and search tasks.

## Features

- Add new tasks with a title and description.
- View all tasks in a table format.
- Update existing tasks.
- Delete tasks.
- Search tasks by title or description.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/flask-todo-app.git
   cd flask-todo-app
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:

   ```
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. Run the application:

   ```
   python app.py
   ```

6. Open your browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

## Usage

- Add a Task: Enter a title and description, then click submit.
- Update a Task: Click the "Update" button next to a task.
- Delete a Task: Click the "Delete" button next to a task.
- Search for Tasks: Use the search bar to find tasks by title or description.

## Technologies Used

- Flask
- Flask-SQLAlchemy
- SQLite
- HTML, CSS, Bootstrap (for UI)

## Contributing

Feel free to fork this repository and make improvements. If you have any suggestions, create a pull request.

## License

This project is open-source and available under the MIT License.

---

Replace `your-username` in the GitHub link with your actual GitHub username before publishing. Let me know if you need any modifications! 🚀
