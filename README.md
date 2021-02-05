# This is my Personal Website, you can visit at JohnShearin.com
I use this to be a home for my Resume, Blog, and Notes. The Notes are only visible to me/a superuser. I created the notes section so that I can create notes or a journal that is visible to me and me only, and will allow me to have a home for notes so that I don't have writings spread across multiple hard drives or note taking apps such as Evernote or Notion.  

The blog also has functionality to add Personas for writing about products and the personas that may use them, a common techique for product management. You can also embed a Powerpoint by adding the microsoft onedrive.live embeddable html text into the Powerpoint field.  

The text on the site listed on the Home and About pages are both created via their own Django model.

## Markdown
The folliwing fields use [Markdown](https://www.markdownguide.org/basic-syntax/):
- HomePage.content
- AboutPage.content
- BlogPost.content
- Persona.content
- Notes.content

### Markdown Implementation
- The markdown field & admin editor are created using an MDTextField. See docs [here](https://developpaper.com/implementation-of-beautiful-django-markdown-rich-text-app-plug-in/)
- The markdown is rendered using the markdown_extras.py template tag. See docs [here](#https://learndjango.com/tutorials/django-markdown-tutorial).


# Clone this project
You can clone this site, but to do so you will need to clone and operate as a standard Django project, see [Django Docs](https://docs.djangoproject.com/en/3.1/), then do the following:
- Set up an Amazon AWS S3 bucket to store media files. You will need to store your bucket's access key and secret access key as environment variables
    - AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    - AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
- Set up a new secret key for the django project (google search "generate secret key for django project" for instructions)  

## This project is hosted on Heroku. To run locally, activate the env (On Windows: `.\env\Scripts\activate`), and call the follwing from the terminal:  
- On Mac/Linux: `heroku local`
- On Windows: `heroku local -f .\Procfile.windows`