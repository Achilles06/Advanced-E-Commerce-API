from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class CustomerAccount(db.Model):
    __tablename__ = 'customer_accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), unique=True, nullable=False)
    
    # Establish one-to-one relationship with Customer
    customer = db.relationship("Customer", back_populates="account")
    
    def __init__(self, username, password, customer_id):
        self.username = username
        self.set_password(password)
        self.customer_id = customer_id

    def set_password(self, password):
        """Hashes and sets the password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the password hash against the provided password."""
        return check_password_hash(self.password_hash, password)
