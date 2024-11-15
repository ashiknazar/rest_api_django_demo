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
│       └── index.html   # HTML page with button to call the API
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




