import pytest
from app import create_app, db, User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

def test_register_user(client):
    response = client.post('/register', data={'username': 'test', 'password': 'pass'})
    assert response.status_code == 302  # Redirect after register
    user = User.query.filter_by(username='test').first()
    assert user is not None
