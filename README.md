

Running the Project (with Docker):

    docker-compose build
    docker-compose up
    #For creating superuser
    docker exec -it container-id bash
    python manage.py createsuperuser


Running th Project (without Docker):

    For backend:
        cd backend
        python3 -m venv env
        source env/bin/activate
        pip3 install -r requirements.txt
        python manage.py migrate
        python manage.py creatsuperuser
        python manage.py runserver

    For frontend:
        cd frontend/csv_uploader_frontend
        npm i
        npm start
