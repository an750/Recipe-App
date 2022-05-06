# Plate Provisions (Recipe Recommendations App)

Sends you a customized email every morning, with information of interest, such as the upcoming weather forecast for your zip code.

![](https://user-images.githubusercontent.com/1328807/77860069-173ef580-71db-11ea-83c6-5897bb9f4f51.png)

## Installation

Create a copy of this [template repo](https://github.com/an750/Recipe-App), then clone or download your new repo onto your local computer (for example to the Desktop), and navigate there from the command-line:

```sh
cd ~/Desktop/Recipe-App/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "recipe-env":

```sh
conda create -n recipe-env python=3.8
conda activate recipe-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Background Jobs

Printing today's weather forecast (to test the Weather.gov API):

```sh
python -m app.weather_service

# in production mode:
APP_ENV="production" COUNTRY_CODE="US" ZIP_CODE="20057" python -m app.weather_service
```


### Web Application

Running the web app (then view localhost:5000 in the browser):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
export FLASK_APP=web_app
flask run
```




## [License](/LICENSE.md)
