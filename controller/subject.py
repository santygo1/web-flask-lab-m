from flask import render_template

import constants
from app import app


@app.get("/subjects/<sub>")
def subject(sub):
    return render_template(
        'subject.html',
        sub=sub,
        discription=constants.subject_dict[sub]
    )
