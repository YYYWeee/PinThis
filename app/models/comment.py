from .db import db, environment, SCHEMA, add_prefix_for_prod

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    pin_id =db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("pins.id")),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("user.id")),nullable=False)
    message = db.Column(db.String,nullable=False)
    created_at =db.Column(db.Date,nullable=False)
    updated_at =db.Column(db.Date,nullable=False)

    pins = db.relationship("Pin",back_populates="comments")
    user = db.relationship("User",back_populates="comments")

    def to_dict(self):
        return {
            'id': self.id,
            'pin_id': self.pin_id,
            'user_id': self.user_id,
            'message':self.message,
        }
