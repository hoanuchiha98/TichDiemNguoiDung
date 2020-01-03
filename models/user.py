from config import db, ma


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('user_id_seq'::regclass)"))
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    fullname = db.Column(db.String, nullable=True)
    role = db.Column(db.Integer, nullable=True)
    danger = db.Column(db.Boolean, nullable=True)
    dob = db.Column(db.Date, nullable=True)
    address = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    point = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer, nullable=True)
    member_id = db.Column(db.Integer, nullable=True)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        sqla_session = db.session
        fields = (
            'id',
            'username',
            # 'password',
            'fullname',
            'role',
            'danger',
            'dob',
            'address',
            'phone_number',
            'email',
            'point',
            'status',
            'member_id'
        )

    def make(self, data, **kwargs):
        return UserModel(**data)


class UserSchemaDTO(ma.ModelSchema):
    class Meta:
        model = UserModel
        sqla_session = db.session
        fields = (
            'username',
            # 'password',
            'fullname',
            'dob',
            'address',
            'phone_number',
            'email',
            'role'
        )

    def make(self, data, **kwargs):
        return UserModel(**data)