from flask import render_template, request

from app import app
import constants


@app.get("/")
def index():
    name = request.values.get('username') or ""
    gender = request.values.get('gender') or ""
    program_id = request.values.get('program') or 0
    subject_id = request.values.getlist('subject[]')
    subjects_select = [constants.subjects[int(i)] for i in subject_id]

    return render_template(
        'index.html',
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        program_list=constants.programs,
        subjects_select=subjects_select,
        subject_list=constants.subjects)
