
# Museum Mapping

Museum Mapping is a project that maps and visualizes museums in Nepal using spatial data, powered by Django and PostGIS. The project stores the longitude and latitude of museums and provides a list of the top 10 museums closest to the user's location. The user's location is extracted from their browser, making it easy to find nearby museums.

## Features

- **Interactive Maps**: Visualize the location of museums across Nepal.
- **Proximity Search**: Find the top 10 closest museums based on the user's current location.
- **User-Friendly**: The user's location is automatically detected via their browser.
- **PostGIS Integration**: Advanced spatial queries are supported via PostGIS.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: Ensure that Python is installed on your system.
- **Poetry**: A tool for dependency management in Python.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **PostGIS**: A spatial database extender for PostgreSQL.

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/samikshakhadka/Museum_Mapping.git
cd Museum_Mapping
```

### 2. Install Dependencies with Poetry

Ensure that Poetry is installed on your machine. If not, you can install it using the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Now, use Poetry to install the project dependencies:

```bash
poetry install
```

### 3. Set Up PostgreSQL and PostGIS

#### Install PostgreSQL and PostGIS

- **Ubuntu/Debian**:

  ```bash
  sudo apt-get install postgresql postgresql-contrib postgis
  ```

- **CentOS/RHEL**:

  ```bash
  sudo yum install postgresql-server postgis
  ```

- **macOS (using Homebrew)**:

  ```bash
  brew install postgresql postgis
  ```

#### Create PostgreSQL Database and Enable PostGIS

1. Log in to the PostgreSQL prompt as a superuser (e.g., `postgres`):

    ```bash
    sudo -u postgres psql
    ```

2. Create a new database for your project:

    ```sql
    CREATE DATABASE museum_mapping;
    ```

3. Connect to the new database:

    ```sql
    \c museum_mapping;
    ```

4. Enable the PostGIS extension:

    ```sql
    CREATE EXTENSION postgis;
    ```

5. Exit the PostgreSQL prompt:

    ```sql
    \q
    ```

### 4. Configure Django Settings

Update the `DATABASES` setting in your `settings.py` file with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'museum_mapping',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### 5. Apply Migrations

Use Django's migration system to set up your database schema:

```bash
poetry run python manage.py migrate
```

### 6. Run the Development Server

Start the Django development server:

```bash
poetry run python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to see the project in action.

### 7. Test Location-Based Features

The project uses the browser's geolocation API to determine the user's location. Ensure your browser allows location access for the best experience.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you'd like to change.

