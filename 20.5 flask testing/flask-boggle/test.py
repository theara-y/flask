from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def test_render_board(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<div class="tile"><span class="text">', html)
            self.assertNotEqual(session['board'], [])

    def test_submit_word_ok(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                ]

            resp = client.get('/submit_word?word=test')
            json = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('ok', json)

    def test_submit_word_not_on_board(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                ]

            resp = client.get('/submit_word?word=word')
            json = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('not-on-board', json)

    def test_submit_word_not_word(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                    ['T', 'E', 'S', 'T', 'S'],
                ]

            resp = client.get('/submit_word?word=tsts')
            json = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('not-word', json)

    def test_submit_best_score_beaten(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['best_score'] = 0

            resp = client.get('/submit_best_score?best_score=100')
            json = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(session['best_score'], 100)
            self.assertIn('100', json)

    def test_submit_best_score_unbeaten(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['best_score'] = 100

            resp = client.get('/submit_best_score?best_score=99')
            json = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(session['best_score'], 100)
            self.assertIn('100', json)