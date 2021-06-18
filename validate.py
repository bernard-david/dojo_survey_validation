from flask import flash
def validate(data):
    is_valid = True
    if len(data['name']) == 0 or len(data['name']) > 50:
        is_valid = False
        flash("Name must be greater than zero characters or less than 50.")

    if data['location'] == '':
        is_valid = False
        flash("Please select a location from list of options.")

    if data['language'] == '':
        is_valid = False
        flash("Please select a language from list of options.")

    if len(data['comment']) == 0 or len(data['comment']) > 300:
        is_valid = False
        flash("Comment must be greater than zero characters or less than 300.")

    return is_valid