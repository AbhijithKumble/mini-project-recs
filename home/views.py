from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup Firebase
cred = credentials.Certificate("mini-project-recs-firebase-adminsdk-qdod9-c216b774aa.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Create your views here.
def index(request):
    collections = db.collection('studentInfo')
    docs = collections.get()

    students = []  # Initialize an empty list to hold student data

    for doc in docs:
        student_data = doc.to_dict()
        revised_doc = {
            'RollNo': student_data.get('RollNo', ''),  # Using get() to avoid KeyErrors
            'Name': student_data.get('Name', ''),
            'Semester': student_data.get('Semester', ''),
        }  
        students.append(revised_doc)  # Append each student's data to the list

    # Pass the students list to the template
    return render(request, 'index.html', {'students': students})
