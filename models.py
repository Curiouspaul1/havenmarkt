from core import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(80))
    password = db.Column(db.String(200))
    is_client = db.Column(db.Boolean)
    address = db.Column(db.String(250))
    telephone = db.Column(db.String(20))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users = db.relationship('User', backref='service')

    @staticmethod
    def addjobs():
        jobs = [
            "Hairdressing","Plumbing",
            "Barbing", "Farming",
            "Tailoring", "Chef"
        ]
        for i in jobs:
            if not Services.query.filter_by(name=i).first():
                service = Services(name=i)
                db.session.add(service)
        db.session.commit()
