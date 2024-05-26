from flask import Blueprint, render_template

page_route = Blueprint('page', __name__)


@page_route.route('/Page')
def page():
    return render_template('page.html')
