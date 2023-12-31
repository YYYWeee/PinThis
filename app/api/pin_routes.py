from datetime import datetime
from random import randint
from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import login_required, current_user
from .AWS_helpers import upload_file_to_s3, get_unique_filename
from .auth_routes import validation_errors_to_error_messages

from app.models import db, Pin, Comment, Favorite, User, Board, BoardUser, PinBoard
from app.forms.comment_form import CommentForm
from app.forms.edit_comment_form import EditCommentForm
from ..forms.pin_post_forms import PinForm
from ..forms.pin_update_forms import EditPinForm
from sqlalchemy import and_, case
from sqlalchemy.sql import func


pin_routes = Blueprint('pins', __name__)


@pin_routes.route('')
def get_all_pins():
    """
    Query for all pins and returns them in a list of pin dictionaries
    """
    pins = Pin.query.order_by(Pin.updated_at.desc()).all()
    return {"pins": [pin.to_dict() for pin in pins]}


@pin_routes.route('/<int:pinId>')
def get_one_pin(pinId):
    """
    Query for all pins and returns them in a list of pin dictionaries
    """
    pin = Pin.query.get(pinId)
    if not pin:
        return jsonify({"message": "Pin not found"}), 404
    response = pin.to_dict()

    # get all boards the session user have
    if current_user.is_authenticated:
        # all_boards = Board.query \
        #     .join(BoardUser) \
        #     .filter(and_(BoardUser.user_id == current_user.id, BoardUser.role.in_(['owner', 'collaborator']))) \
        #     .order_by(BoardUser.updated_at).all()

        # sessionUserBoards = [board.to_dict_simple() for board in all_boards]
        # response["sessionUserBoards"] = sessionUserBoards

        all_boards = Board.query \
            .join(BoardUser) \
            .filter(and_(BoardUser.user_id == current_user.id, BoardUser.role.in_(['owner', 'collaborator']))) \
            .all()

        subquery = PinBoard.query.with_entities(
            PinBoard.board_id).filter_by(pin_id=pinId).subquery()
        sessionUserBoards = []
        for board in all_boards:
            singleBoard = board.to_dict_simple()
            singleBoard["is_pin_existing"] = board.id in [row[0]
                                                          for row in db.session.query(subquery)]
            sessionUserBoards.append(singleBoard)
        response["sessionUserBoards"] = sessionUserBoards
    return response
    # response["creator"] = pin.user.to_dict()
    # comments_list = []
    # for comment in pin.comments:
    #     comment_dict = comment.to_dict()
    #     comment_dict["commenter"] = {
    #         "photo_url": comment.user.photo_url, "first_name": comment.user.first_name}
    #     comments_list.append(comment_dict)
    # response["comments"] = sorted(
    #     comments_list, key=lambda x: x["updated_at"], reverse=True)
    return response

# Create a new pin


@pin_routes.route('', methods=["POST"])
@login_required
def new_pin():
    print('Backend now!!!!!!!', current_user)

    form = PinForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    # count = Pin.query.all().count
    print('Backend now!!!!!!!', current_user)

    if form.validate_on_submit():

        image_file = form.data["image"]
        image_file.filename = get_unique_filename(image_file.filename)
        upload = upload_file_to_s3(image_file)

        new_pin = Pin(
            owner_id=current_user.to_dict()['id'],
            image_url=upload["url"],
            title=form.data['title'],
            description=form.data['description'],
            alt_text=form.data['alt_text'],
            link=form.data['link']
        )

        db.session.add(new_pin)

        # now we only allow new pin created in default board
        # add new pin to default board of session user
        default_board = Board.query.filter(and_(
            Board.owner_id == current_user.id, Board.is_default == True)).first()
        new_pin_in_board = PinBoard(
            pin_id=new_pin.id,
            board_id=default_board.id,
        )
        db.session.add(new_pin_in_board)
        default_board.updated_at = func.now()
        db.session.commit()
        return new_pin.to_dict()

    print(form.errors)
    return {"errors": validation_errors_to_error_messages(form.errors)}


# Update pin


@pin_routes.route('/<int:pinId>', methods=['PUT'])
@login_required
def edit_pin(pinId):
    print("in update route@@@@@@@@@@@@@@@@@@@@@@@, before form data collecting")
    form = EditPinForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print("in update route@@@@@@@@@@@@@@@@@@@@@@@", form.data)
    target_pin = Pin.query.get(pinId)
    if form.validate_on_submit():
        print("we pass validation!!!!!!!!!!!!!!!!!!!")
        target_pin.title = form.data['title']
        target_pin.description = form.data['description']
        target_pin.alt_text = form.data['alt_text']
        target_pin.link = form.data['link']
        # target_pin.note_to_self = form.data['note_to_self']
        target_pin.allow_comment = form.data['allow_comment']
        # target_pin.show_shopping_recommendations = form.data['show_shopping_recommendations']

        db.session.commit()
        response = target_pin.to_dict()

        if current_user.is_authenticated:
            all_boards = Board.query \
                .join(BoardUser) \
                .filter(and_(BoardUser.user_id == current_user.id, BoardUser.role.in_(['owner', 'collaborator']))) \
                .all()

            subquery = PinBoard.query.with_entities(
                PinBoard.board_id).filter_by(pin_id=pinId).subquery()
            sessionUserBoards = []
            for board in all_boards:
                singleBoard = board.to_dict_simple()
                singleBoard["is_pin_existing"] = board.id in [row[0]
                                                              for row in db.session.query(subquery)]
                sessionUserBoards.append(singleBoard)
            response["sessionUserBoards"] = sessionUserBoards
        return response
    if form.errors:
        print(form.errors)
        return form.errors


# Delete pin
@pin_routes.route('/<int:pinId>', methods=["DELETE"])
@login_required
def delete_pin(pinId):
    targetPin = Pin.query.get(pinId)
    db.session.delete(targetPin)
    db.session.commit()
    return {"id": targetPin.id}


@pin_routes.route('/<int:pinId>/comments')
def get_pin_comments_by_pinId(pinId):
    pin = Pin.query.get(pinId)
    if not pin:
        return jsonify({"message": "Pin not found"}), 404
    comments = Comment.query.join(Pin).filter(Pin.id == pinId)
    comments_list = []
    for comment in comments:
        comment_dict = comment.to_dict()
        comment_dict["commenter"] = {
            "photo_url": comment.user.photo_url, "first_name": comment.user.first_name, "username": comment.user.username}
        comments_list.append(comment_dict)
    return comments_list


@pin_routes.route('/<int:pinId>/comments', methods=['POST'])
@login_required
def add_comment_to_pin(pinId):
    pin = Pin.query.get(pinId)
    if not pin:
        return jsonify({"message": "Pin not found"}), 404
    form = CommentForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_comment = Comment(
            pin_id=pinId,
            user_id=current_user.id,
            message=form.data["message"]
        )
        db.session.add(new_comment)
        db.session.commit()
        response = new_comment.to_dict()
        response["commenter"] = {
            "photo_url": new_comment.user.photo_url, "first_name": new_comment.user.first_name}
        return response
    if form.errors:
        print(form.errors)
        # both works
        return form.errors
# form.errors returns:
# {
#     "message": [
#         "This field is required."
#     ]
# }
        # return {"errors": validation_errors_to_error_messages(form.errors)}
# {
#     "errors": [
#         "message : This field is required."
#     ]
# }
