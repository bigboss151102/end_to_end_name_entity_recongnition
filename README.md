## Table of Contents
- [Description](#description)
- [Idea](#idea)
- [Design System](#design-system)
- [Installation](#installation)
- [Run Application](#run-application)
- [Contact](#contact)

# Description
In this project, we will develop a Customized Named Entity Recognizer. The main idea of this project is to extract entities from scanned documents such as invoices,business cards, shipping bills, bills of lading, etc. However, due to data privacy reasons, we will focus only on business cards. But we can use the explained framework to handle all types of financial documents. Below is the development process that we will follow in the project. Todevelop this project, we will use two main technologies in data science :
- Computer Vision: In Computer Vision module, we will scan the document, identify the location of text and finally extract text from the image.
- Natural Language Processing: Then in Natural language processing, we will extract the entitles from the text and do necessary text cleaning and parse the entities form the text.
# Idea
![Idea](./idea.png)
# Design System
![Desigin System](./design-system.jpg)

# Installation
### Create Virtual Environment
Then create new environment where contain nessessary packages to this project.
Ensure you have Python 3.9+ installed.
```cmd
python -m venv .venv
```
Activate new enviroment
```cmd
.venv\Scripts\activate
```
Then, install the required dependencies using pip:
```cmd
pip install -r requirements.txt
```

# Run Application
All done! To run the application, start the Django server and the React development server
In 2 separate terminals, make sure you’re in the root directory of your Django project, run:
```cmd
python manage.py runserver
```
and in the frontend directory, run:
```cmd
cd frontend
npm run dev
```
Visit the URL shown in your terminal (usually http://localhost:5173/) to view the app.

# Contact
For questions, contributions, or bug reports, please feel free to reach out:

- Email: [hoangcongtrong02.dut@gmail.com](hoangcongtrong02.dut@gmail.com)
- Linkedin: [https://www.linkedin.com/in/hoangtrong151102/](https://www.linkedin.com/in/hoangtrong151102/)
- Instagram: [https://www.instagram.com/h.c.trong_02/](https://www.instagram.com/h.c.trong_02/)

I appreciate your feedback and involvement!




