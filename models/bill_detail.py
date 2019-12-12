from config import db, ma

class BillDetailModel(db.Model):
    __tablename__ = 'bill_detail'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('bill_detail_id_seq'::regclass)"))
    bill_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)

class BillDetailSchema(ma.ModelSchema):
    class Meta:
        model = BillDetailModel
        sqla_session = db.session
        fields = (
            'id',
            'bill_id',
            'product_id',
            'count'
        )

    def make(self, data, **kwargs):
        return BillDetailModel(**data)