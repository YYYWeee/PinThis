from flask import Blueprint, jsonify, session, request
from app.models import User, db, Board, BoardUser
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import and_

auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    print("in login backend")
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        print('user.to_dict()!!!!!!!!', user.to_dict()['id'])
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password'],
            first_name=form.data['first_name'],
            last_name=form.data['last_name']
        )
        db.session.add(user)
        created_user = User.query.filter(
            User.email == form.data['email']).first()

        # when user sign up, create a default board named "All pins"
        board = Board(
            owner_id=created_user.id,
            name="All pins",
            is_secret=False,
            is_default=True
        )
        db.session.add(board)

        created_default_board = Board.query.filter(
            and_(Board.owner_id == user.id, Board.is_default == True)).first()
        if not created_default_board:
            return {'errors': "Default board not created successfully for this user"}, 500
        new_board_user = BoardUser(
            user_id=created_default_board.owner_id,
            board_id=created_default_board.id,
            role='owner'
        )
        db.session.add(new_board_user)
        db.session.commit()

        login_user(user)

        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
