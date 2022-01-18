"""
This file have the routes
for the validation of the user
for enter to the blog
"""

from flask import Blueprint, request, render_template, flash, url_for, redirect
from models.users import Users
from bcrypt import checkpw
from utils.passwords import encrypt_password
from models.password import Password
from utils.db import db

# routes for the users
users = Blueprint("users", __name__)


# routes
@users.route("/validate-password-for-name/<username>", methods=["GET", "POST"])
def validate_password_for_name(username):
    """
    Route for validate the user in the database
    """

    if request.method == "GET":
        return render_template("validations/validate-for-name.html", username=username)

    else:
        user = Users.query.filter_by(name=username).first()

        password = request.form["password"]
        password = Password(password.encode())

        if checkpw(password.value, user.password.encode()):
            return redirect(
                url_for("users.change_name", username=user.name, validated="1")
            )

        else:
            flash("The password is incorrect")

            return redirect(
                url_for("users.validate_password_for_name", username=username)
            )


@users.route("/validate-password-for-password/<username>", methods=["GET", "POST"])
def validate_password_for_password(username):
    """
    Route for validate the user in the database
    """

    if request.method == "GET":
        return render_template(
            "validations/validate-for-password.html", username=username
        )

    else:

        # getting values
        password = request.form["password"]

        user = Users.query.filter_by(name=username).first()
        password = Password(password.encode())

        if checkpw(password.value, user.password.encode()):
            return redirect(
                url_for("users.change_password", username=username, validated="1")
            )

        else:
            flash("The password is incorrect")

            return redirect(
                url_for("users.validate_password_for_password", username=username)
            )


@users.route("/change-password/<username>/<validated>", methods=["GET", "POST"])
def change_password(username, validated):
    """
    Render the page for change the password
    """

    # validating if the user already validated with the password
    if validated == "1":

        # validating the method
        if request.method == "GET":
            return render_template("accounts/change-password.html", username=username)

        else:
            # new password for set
            new_password = request.form["new-password"]

            if len(new_password) < 6:
                flash("The password is less that 6. Try again.")

                return redirect(
                    url_for("users.change_password", username=username, validated="1")
                )

            else:
                # gettings values for change
                user = Users.query.filter_by(name=username).first()
                password = Password(new_password.encode())

                password = encrypt_password(password.value)
                user.password = password.decode()  # change

                db.session.add(user)
                db.session.commit()

                flash("Password Updated Successfully")

                return redirect(url_for("themes.home", username=user.name))

    else:
        # return render_template('accounts/change-password.html')
        return redirect(
            url_for("users.validate_password_for_password", username=username)
        )


@users.route("/change-name/<username>/<validated>", methods=["GET", "POST"])
def change_name(username, validated):
    """
    Render the page for change the password
    """

    if validated == "1":
        # validating the method
        if request.method == "GET":
            return render_template("accounts/change-name.html", username=username)

        else:
            # getting the new values
            new_name = request.form["new-name"]

            user = Users.query.filter_by(name=username).first()
            user.name = new_name  # change

            db.session.add(user)
            db.session.commit()

            flash("Name Updated Successfully")

            return redirect(url_for("themes.home", username=user.name))

    else:
        # return render_template('accounts/change-name.html')
        return redirect(url_for("users.validate_password_for_name", username=username))
