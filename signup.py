#ユーザー登録に差し替える用
# from werkzeug.security import generate_password_hash, check_password_hash

# #サインアップページ
# @app.route("/signup", methods=["GET","POST"])
# def signup():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         user = User.query.filter_by(username=username).first()
#         if user:
#             flash("ユーザー名は既に使用されています。別のユーザー名を選択してください。")
#             return redirect(url_for("signup"))
    
#         hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
#         new_user = User(username=username, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         flash("サインアップが成功しました。ログインしてください。")
#         return redirect(url_for("login"))
    
#     return render_template("signup.html")

# #ログインページ
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         user = User.query.filter(User.username == username).first()
#         if user and check_password_hash(user.password, password):
#             session["user_id"] = user.id
#             flash("ログインに成功しました")
#             return redirect(url_for("create_dict"))
#         else:
#             flash("ユーザー名またはパスワードが間違っています。")
    
#     return render_template("login.html")


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
