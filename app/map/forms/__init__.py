from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class location_edit_form(FlaskForm):
    title = TextAreaField('title', [validators.length(min=6, max=300)],
                          description="Add title")
    longitude = TextAreaField('longitude', [validators.length(min=6, max=300)],
                              description="Add longitude")
    latitude = TextAreaField('latitude', [validators.length(min=6, max=300)],
                             description="Add latitude")
    population = IntegerField('population', [validators.DataRequired()], description="Add population")

    submit = SubmitField()

class location_add_form(FlaskForm):
    title = TextAreaField('Add title', [
        validators.length(min=6, max=300),

    ], description="Title")

    longitude = TextAreaField('Add longitude', [
        validators.length(min=6, max=300),

    ], description="Longitude")

    latitude = TextAreaField('Add latitude', [
        validators.length(min=6, max=300),

    ], description="Latitude")

    population = IntegerField('Add population', [
        validators.DataRequired(),

    ], description="Population")

    submit = SubmitField()

class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()
