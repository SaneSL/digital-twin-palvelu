# Run Server
if __name__ == '__main__':
    from app import create_app
    app = create_app(module=True)
    app.run(debug=True)