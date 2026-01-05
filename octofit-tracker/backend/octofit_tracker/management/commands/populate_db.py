from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Sample superhero and team data
SUPERHEROES = [
    {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
    {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
    {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'Marvel'},
    {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
    {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'DC'},
    {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
]
TEAMS = [
    {'name': 'Marvel', 'members': ['Spider-Man', 'Iron Man', 'Captain America']},
    {'name': 'DC', 'members': ['Batman', 'Superman', 'Wonder Woman']},
]
ACTIVITIES = [
    {'user': 'Spider-Man', 'activity': 'Web Swinging', 'duration': 60},
    {'user': 'Batman', 'activity': 'Martial Arts', 'duration': 45},
]
LEADERBOARD = [
    {'user': 'Superman', 'score': 1000},
    {'user': 'Iron Man', 'score': 900},
]
WORKOUTS = [
    {'name': 'Strength Training', 'suggested_for': 'Marvel'},
    {'name': 'Flight Training', 'suggested_for': 'DC'},
]

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        # Insert test data
        db.users.insert_many(SUPERHEROES)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        # Ensure unique index on email
        db.users.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
