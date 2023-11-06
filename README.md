# Weather App using Django python Framework
This application developed using the Python Django framework. This app provides users with current weather information for a specific city, utilizing the Open Weather API. Here's how you can set up and use the Weather App.

## Requirements
To run the Weather App, you need to have the following installed on your system:
- Python (>=3.6)
- Django (>=4.2.7)
- django-environ (0.11.2)
- python-decouple (3.8)
- requests (2.31.0)

You can install these dependencies using the following command:
```
pip install Django django-environ python-decouple requests
```
## Clone the Repository
```
git clone https://github.com/ImeshaDilshani/weatherpro.git
```

## Setup Environment Variables
- Create a .env file in the project root directory.
- Add your Open Weather API key and Django secret key in the .env file:
```
OPEN_WEATHER_API_KEY=your_open_weather_api_key
```
```
SECRET_KEY=your_django_secret_key
```
Make sure to add .env to your .gitignore file to avoid exposing sensitive information.

To activate a Python virtual environment, you need to use the appropriate command based on your operating system.

## For Windows:
Navigate to the directory containing your virtual environment
```
python -m venv myenv  
```
Activate the virtual environment
```
myenv\Scripts\activate
```
```
cd weatherpro
```
## Run the Application
``
python manage.py runserver
``

The application will be Starting development server at ```http://127.0.0.1:8000/```

## Using the Weather App
- Access the Weather App in your web browser.
- Enter the name of the city for which you want to check the weather.
- Click on the "Submit" button to view the current weather conditions for the specified city.
  
## Features
- Current Weather: Get real-time weather information for any city.
- Customization: Easily customizable to add more features and weather-related data.

## Dependencies
The Weather App uses the following Python packages:
```
asgiref==3.7.2
certifi==2023.7.22
charset-normalizer==3.3.2
Django==4.2.7
django-environ==0.11.2
idna==3.4
python-decouple==3.8
python-dotenv==1.0.0
requests==2.31.0
sqlparse==0.4.4
tzdata==2023.3
urllib3==2.0.7
```
These packages are automatically installed when you run ```pip install -r requirements.txt``` to install dependencies.

Feel free to modify and enhance the Weather App according to your requirements!




