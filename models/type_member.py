from config import db, ma

class TypeMemberModel(db.Model):
    __tablename__ = 'type_member'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('type_member_id_seq'::regclass)"))
    name_member = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.Date, nullable=False)
    status = db.Column(db.Integer, nullable=True)

class TypeMemberSchema():
    class Meta:
        model = TypeMemberModel
        sqla_session = db.session
        fields = (
            'id',
            'name_member',
            'price',
            'date_created',
            'status',
        )

    def make(self, data, **kwargs):
        return TypeMemberModel(**data)