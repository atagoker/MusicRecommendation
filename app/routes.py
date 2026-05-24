try:
    from .server import app
except ImportError:
    from server import app


if __name__ == "__main__":
    app.run(debug=True)
