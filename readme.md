# Aviate API

**Aviate API** is a Django-based RESTful API for managing candidates. It provides endpoints to create, retrieve, update, and delete candidate records, as well as a search functionality to find candidates based on their names.

## Requirements

### Candidate Endpoints

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| GET    | /candidates/      | List all candidates    |
| POST   | /candidates/      | Create a new candidate |
| GET    | /candidates/{id}/ | Retrieve a candidate   |
| PUT    | /candidates/{id}/ | Update a candidate     |
| DELETE | /candidates/{id}/ | Delete a candidate     |

### Search Endpoint

| Method | Endpoint                      | Description                                                                             |
| ------ | ----------------------------- | --------------------------------------------------------------------------------------- |
| GET    | /candidates/search/?q={query} | Search for candidates based on the provided query. The results are sorted by relevancy. |

Example:
If the search query is "Ajay Kumar Yadav", the order of results will be:
["Ajay Kumar Yadav", "Ajay Kumar", "Ajay Yadav", "Kumar Yadav", "Ramesh Yadav", "Ajay Singh"]

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/PragatiVerma18/aviate.git
   cd aviate
   ```

2. Create and activate a virtual environment:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply the migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser:

   ```sh
   python manage.py createsuperuser
   ```

6. Create test users (optional):

   ```sh
   python manage.py create_test_candidates
   ```

7. Run the development server:

   ```sh
   python manage.py runserver
   ```

## Search API

### How It Works

The search API allows you to search for candidates based on their names.

- The search query is split into individual words, and candidates whose names contain any of the words are filtered.
- The results are then annotated with a match score based on the number of words in the search query that can be found in the candidate's name.
- The results are sorted by the match score in descending order.

### Example

If the search query is "Ajay Kumar Yadav", the order of results will be:

| Candidate Name   | Matching Words     | Relevancy Score |
| ---------------- | ------------------ | --------------- |
| Ajay Kumar Yadav | Ajay, Kumar, Yadav | 3               |
| Ajay Kumar       | Ajay, Kumar        | 2               |
| Ajay Yadav       | Ajay, Yadav        | 2               |
| Kumar Yadav      | Kumar, Yadav       | 2               |
| Ramesh Yadav     | Yadav              | 1               |
| Ajay Singh       | Ajay               | 1               |

Hence the sorting order would be:

1. "Ajay Kumar Yadav"
2. "Ajay Kumar"
3. "Ajay Yadav"
4. "Kumar Yadav"
5. "Ramesh Yadav"
6. "Ajay Singh"
