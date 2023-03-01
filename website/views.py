from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from gdscgetdata import getData

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def getValue():
    if request.method == 'POST':
        spotifyUsername = request.form.get('username')
        topArtists, topTracks = getData(spotifyUsername)
    # Return data to visualize in html
    return render_template('home.html', user=current_user, spotifyUsername=spotifyUsername, topArtists=topArtists, topTracks=topTracks)