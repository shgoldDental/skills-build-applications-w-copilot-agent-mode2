from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='testteam')
        self.assertEqual(team.name, 'testteam')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(activity_type='running', duration='00:30:00')
        self.assertEqual(activity.activity_type, 'running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='testworkout', description='test description')
        self.assertEqual(workout.name, 'testworkout')
