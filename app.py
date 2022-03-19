from __init__ import create_app, hello
from flask import Flask


app = create_app()
# hello()
# print(db_con)

if __name__ == '__main__':
    app.run(debug=True)
    
    