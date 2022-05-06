# Plate Provisions (Recipe Recommendations App)

## Intructions for Application Use on External Heroku Server

Copy the following link into your browser: https://plate-provisions-22.herokuapp.com/

## Instructions for Local Installation and Deployment 

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
### Spoonacular API Access

Create a local .env file in your editor for security purposes.

Go to https://spoonacular.com/food-api and sign up for an account, verifying your account through email. 

Once verified, go to 'My Console' < 'Profile < 'Show/Hide Api Key'

Copy over your API key into your .env file like the following: 
SPOONACULAR_API="____"


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
