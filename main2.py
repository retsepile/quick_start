from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/validate/<name>')
def check_user(name):
    if name == 'Thandokazi':
        return redirect(url_for('admin_page', name=name))
    elif name == 'Zoe':
        return redirect(url_for('user_page', name=name))
    else:
        if name == 'Visitor':
            return redirect(url_for('visitor_page', name=name))


@app.route('/user/<name>')
def user_page(__name__):
    return 'hello user %s ' % __name__


@app.route('/admin/<name>')
def admin_page(__name__):
    return 'Welcome to the admin page %s ' % __name__


@app.route('/Guest/<name>')
def guest_page(__name__):
    return 'Welcome to the guest page'


if __name__ == 'main':
    app.debug = True

@app.route('/pament/<name>')
def pay_check(__name__):
    
    app.run()
