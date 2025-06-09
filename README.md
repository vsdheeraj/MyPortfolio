# Dheeraj Portfolio

This is a Django project named "Dheeraj Portfolio". It serves as a personal portfolio website showcasing projects and skills.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/dheerajportfolio.git
   cd dheerajportfolio
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your_secret_key
   MY_EMAIL=your_email@example.com
   MY_PASSWORD=your_email_password
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

## Usage

To run the development server, use the following command:
```
python manage.py runserver
```
You can then access the application at `http://127.0.0.1:8000/`.

## Deployment

For deployment on Vercel, ensure you have a `vercel.json` file configured properly. You can deploy your project by running:
```
vercel --prod
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.