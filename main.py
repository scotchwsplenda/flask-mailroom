import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

# query = Tweet.select().join(User).where(User.username == 'huey')

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        donorid = Donor.select().where(Donor.name == request.form['name']).get()
        funky = Donation(value=request.form['don_amt'], donor=donorid.id)
        funky.save()
        return redirect(url_for('all'))
    else:
        return render_template('create_donation.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
