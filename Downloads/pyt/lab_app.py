from flask import Flask, request, session, redirect, url_for, render_template_string

app = Flask(__name__)
app.secret_key = "cybernerddd_secret"

LOGIN_PAGE = """
<form method="POST">
  <input name="username" />
  <input name="password" type="password" />
  <button>Login</button>
</form>
"""

DASHBOARD = """
<h1>Welcome Admin</h1>
<a href="/logout">Logout</a>
"""

FAKE_404 = "<h1>Nothing here</h1>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            session["auth"] = True
            return redirect("/dashboard")
        return "Invalid credentials"
    return LOGIN_PAGE

@app.route("/dashboard")
def dashboard():
    if not session.get("auth"):
        return redirect("/login")
    return DASHBOARD

@app.route("/admin")
def admin():
    if not session.get("auth"):
        return redirect("/login")
    return "<h1>Admin Panel</h1>"

@app.route("/uploads")
def uploads():
    if not session.get("auth"):
        return redirect("/login")
    return "<h1>Uploads Directory</h1>"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/<path:path>")
def catch_all(path):
    return FAKE_404

app.run(debug=False)
