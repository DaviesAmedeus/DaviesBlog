# import os
# import secrets
# # this PIL specificall the class "Image"  will help to work and reduce the size of the image
# from PIL import Image
# from flask import render_template, url_for, flash, redirect, request, abort
# from DaviesBlog import app, db, bcrypt, login_manager, mail
# from DaviesBlog.forms import (RegistrationForm, LoginForm,
#                               UpdateAccountForm, PostForm,
#                               RequestResetForm, ResetPasswordForm)
# from DaviesBlog.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_mail import Message
#
#
#
# # @login_manager.user_loader
# # def load_user(user_id):
# #     return User.query.get(int(user_id))
#
#
#
