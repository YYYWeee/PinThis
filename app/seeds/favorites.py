from app.models import db, Favorite, environment, SCHEMA
from sqlalchemy.sql import text


def seed_favorites():
    favorites = [{"user_id": 1, "pin_id": 3, "board_id": 3},
                 {"user_id": 2, "pin_id": 4, "board_id": 1},
                 {"user_id": 3, "pin_id": 5, "board_id": 4},
                 {"user_id": 3, "pin_id": 2, "board_id": 4},
                 {"user_id": 1, "pin_id": 15, "board_id": 8},
                 {"user_id": 1, "pin_id": 16, "board_id": 8},
                 {"user_id": 1, "pin_id": 1, "board_id": 7},
                 {"user_id": 1, "pin_id": 3, "board_id": 7},
                 {"user_id": 1, "pin_id": 10, "board_id": 7},
                 {"user_id": 1, "pin_id": 13, "board_id": 7},
                 {"user_id": 1, "pin_id": 4, "board_id": 7},
                 {"user_id": 1, "pin_id": 18, "board_id": 9},
                 {"user_id": 3, "pin_id": 22, "board_id": 12},
                 {"user_id": 3, "pin_id": 23, "board_id": 12},
                 {"user_id": 2, "pin_id": 27, "board_id": 15},
                 {"user_id": 4, "pin_id": 29, "board_id": 15},
                 {"user_id": 6, "pin_id": 31, "board_id": 16},
                 ]

    seed_favorites = [db.session.add(Favorite(**favorite))
                      for favorite in favorites]
    db.session.commit()


def undo_favorites():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))

    db.session.commit()
