# Hospital API for COVID-19 Patients and Doctors

This is a server-side API for a hospital's COVID-19 patient management system built using Django and MongoDB.

## Installation

1. Clone the repository: git clone https://github.com/Aman7818/Hospital_api.git
2. Create and activate a virtual environment: python -m venv env
source env/bin/activate.
3. Install the dependencies: pip install -r requirements.txt
4. Update the MongoDB configuration in `settings.py`:
- Open `hospital_api/settings.py`
- Update the `DATABASES` section with your MongoDB connection details (host, username, password).

5. Apply database migrations:python manage.py makemigrations
python manage.py migrate
6. Run the server: python manage.py runserver

## API Endpoints

- `POST /doctors/register`: Register a new doctor.
- `POST /doctors/login`: Authenticate the doctor and obtain a JWT token.
- `POST /patients/register`: Register a new patient.
- `POST /patients/{id}/create_report`: Create a patient report for a specific patient ID.
- `GET /patients/{id}/all_reports`: Retrieve all reports of a patient.
- `GET /reports/{status}`: Retrieve all reports of all patients filtered by status.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## Credits

This project was developed by [Aman Yadav](https://github.com/Aman7818).

## Contact

For any inquiries or issues, please contact [yadavaman4491@gmail.com](mailto:yadavaman4491@gmail.com).













