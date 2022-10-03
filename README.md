# DSA Buddy
Your DSA Buddy, one to share your progress with, one to help you practice and one to help you combine your effort accross different coding platforms.
## Setup for development
- Clone the repository
   `git clone https://github.com/helloGit9541/dsa-buddy.git`
- Start the virtual environment using virtualenv
  `virtualenv env`
- Activate the environment with `source env/bin/activate`
- Install tailwind with `npm install -D tailwindcss`
- To keep tailwind upto date with changes run  `npm run watch`
- Now install the requirements with  `pip install requirements.txt`
- Run migrations to setup the database `python manage.py migrate`
- Run server with `python manage.py runserver`
- Now server is available at [link](http://127.0.0.1:8000/)