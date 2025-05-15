# My Portfolio

Welcome to my personal portfolio website! This project showcases my skills, projects, and experience as a web developer. It’s built with modern web technologies and deployed on AWS for hosting and storage.

## Features

- **Project Showcase**: A section dedicated to displaying my key projects, including links, descriptions, and GitHub repositories for each project.
- **Responsive Design**: Optimized for both desktop and mobile devices, ensuring a smooth user experience across all screen sizes.
- **Contact Form**: An integrated contact form to allow visitors to get in touch with me directly through the site.
- **Technologies Used**: Built with Django (Python), HTML/CSS, and JavaScript. Deployed on AWS S3 for static file storage.
- **Interactive UI**: Features animations and smooth transitions for better engagement.
- **Blog Section**: A place for sharing updates, tutorials, and thoughts on web development and technology.

## Technologies & Tools
### Frontend
- HTML
- CSS (with SCSS)
- JavaScript
### Backend
- Django (Python)
### Database
- PostgreSQL
### Hosting & Deployment
- AWS S3 (for static file storage)
- AWS EC2 (for deployment)
- AWS RDS 
### Version Control
- Git
- GitHub
  
Feel free to explore and get inspired!

## Setup & Installation

To run this project locally:

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/.git](https://github.com/vsdheeraj/MyPortfolio.git)
   
   cd dheerajportfolio

2. create a virtual environment
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Set up your environment variables: Create a .env file in the root directory with the necessary environment variables, example:
   ```bash
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=your-database-url
   AWS_ACCESS_KEY_ID=your-aws-access-key-id
   AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
   
5. Run database migrations:
   ```bash
   python manage.py migrate

6. Start the development server:
   ```bash
   python manage.py runserver


## Features

- Custom user authentication (login/register)
- Blog post creation/editing with CKEditor 5
- Theme switcher (light/dark modes)
- Contact form with email sending
- Responsive design

## Technologies

- Django 4.2
- PostgreSQL (production)
- AWS S3 (for media storage)
- CKEditor 5
- Crispy Forms
- Whitenoise

## Setup

1. Clone the repository
2. Create and activate virtual environment
3. Install requirements: `pip install -r requirements.txt`
4. Create `.env` file with your credentials (see `.env.example`)
5. Run migrations: `python manage.py migrate`
6. Start development server: `python manage.py runserver`

## Environment Variables

Required variables are:
- `SECRET_KEY`
- `DB_*` (for database connection)
- `MY_EMAIL` and `MY_PASSWORD` (for email sending)
- `AWS_*` (for S3 storage)

## Deployment

Configured for AWS deployment with:
- RDS PostgreSQL
- S3 Bucket for media storage
- Elastic Beanstalk (optional)


