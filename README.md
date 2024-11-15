# REST API Django Demo

This project demonstrates a simple REST API setup in Django, featuring two Django projects: `frontend` and `newproject`.

- **`frontend`**: This project serves an HTML page with a button that, when clicked, calls an API to retrieve and display data.
- **`newproject`**: This project provides the API that returns the data consumed by `frontend`.

## Project Structure

```
rest_api_django_demo/
├── frontend/            # Django project to display HTML page and call API
│   ├── manage.py
│   ├── frontend_app/    # Your Django app files go here
│   └── templates/
│          # HTML page with button to call the API
├── newproject/          # Django project providing the API
│   ├── manage.py
│   ├── api_app/         # Your Django API app files
│   └── templates/
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the Repository**

   Clone this repository to your local machine.

   ```bash
   git clone <repository_url>
   cd rest_api_django_demo
   ```
2. **Install Dependencies**
    ```bash
   pip install django djangorestframework
   ```
3. **Run the newproject API**
    ```bash
   cd newproject
   python manage.py runserver
   ```
4. **Run the frontend Project**
    ```bash
   cd frontend
   python manage.py runserver 8001
   ```
## Notes

- Make sure both servers are running simultaneously in separate terminals.
- By default, Django will automatically reload changes when you save your files, so you do not need to restart the server every time.




