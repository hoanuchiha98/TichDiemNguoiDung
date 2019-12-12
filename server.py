from flask import Flask, redirect
from config import connex_app
from swagger_config import swagger_file

app = connex_app
app.add_api(swagger_file)

@app.route('/')
def home():
    return redirect("api/ui", code=302)


if __name__ == '__main__':
    print('Run API')
    app.run(port=5000, debug=True)
