import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from DaviesBlog import mail


#The below function is used in account rout for dealing with image file data
def save_picture(form_picture):

    #here we modify the name and the path of the image
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # here is when we resize(shrink) our image
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='amedeusedgar@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
If you did not make this request please ignore this message and no chages will be done
    '''
    mail.send(msg)