# repo-share

RepoShare is a proof-of-concept for a website where users can share and discuss Open-Source projects.

It acts as a proxy to the Github API that connects their data and RepoShare's additional features to a custom frontend.

## Development

To create a development environment follow the steps below (work in progress):

1. Create a virtual environment:
   `python -m venv .venv`
1. Activate the environment and install necessary packages
   E.g. in bash
   `./.venv/bin/activate`
   In Windows Command Prompt
   `.\.venv\Scripts\activate.bat`
   Installing:
   `pip install -r requirements.txt`
1. Go into the `reposhare` directory and migrate the database
   `python .\manage.py migrate`
1. Set up a [github app](https://github.com/settings/apps)

   - Create a .env file (see `.env.example`)
   - Generate a client secret
   - Fill out the app information
   - Set the callback url to `http://127.0.0.1:8000/accounts/github/login/callback/`
   - Check `Request user authorization (OAuth) during installation`
   - Generate a private key if it hasn't been done automatically
   - Save changes
   - Fill out the environment variables accordingly

1. Create an admin account with `python .\manage.py createsuperuser`
1. Start the app with `python .\manage.py runserver`
1. Go to `127.0.0.1:8000/admin` and log in
1. In the social applications view create a GitHub social app
1. Go to `127.0.0.1:8000`
1. The app should work now
