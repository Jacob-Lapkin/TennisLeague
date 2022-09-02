from flask import Flask, render_template, url_for, Blueprint, flash, session, redirect
from database import mongo

leagues = Blueprint("leagues", __name__, url_prefix='')


@leagues.route('/leagues', methods=['GET', 'POST'])
def leagues_home():
    return render_template('leagues.html')