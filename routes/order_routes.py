from controllers.order_controller import order_bp

def register_order_routes(app):
    app.register_blueprint(order_bp, url_prefix="/api")
