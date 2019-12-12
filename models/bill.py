from config import db, ma

class BillModel(db.Model):
    __tablename__ = 'bill'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('bill_id_seq'::regclass)"))
    user_id = db.Column(db.Integer, nullable=False)
    money_bill = db.Column(db.Float(53), nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    conversion_point = db.Column(db.Integer, nullable=True)
    conversion_point_last = db.Column(db.Integer, nullable=True)
    ship_money = db.Column(db.Float(53), nullable=True)

class BillSchema(ma.ModelSchema):
    class Meta:
        model = BillModel
        sqla_session = db.session
        fields = (
            'id',
            'user_id',
            'money_bill',
            'date_created',
            'conversion_point',
            'conversion_point_last',
            'ship_money'
        )

    def make(self, data, **kwargs):
        return BillModel(**data)