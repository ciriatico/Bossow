from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
import datetime
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models.image_dao import Image, ImageDAO

images = Blueprint('images', __name__)

@images.route('/image/<int:id>')
def get_image(id):
    cursor = mysql.connection.cursor()
    image = ImageDAO().find_by_id(cursor, id)
    if not image:
        return redirect(url_for('views.home'))

    return Response(image.data, mimetype=image.mime_type)

@images.route('/uploads/manage')
@is_authenticated
@has_permission('admin')
def manage_uploads():
    cursor = mysql.connection.cursor()
    uploads = ImageDAO().get_all(cursor)

    return render_template("manage-uploads.html", session=session, uploads=uploads)

@images.route('/delete-screenshot', methods=['POST'])
@is_authenticated
def delete_screenshot():
    data = json.loads(request.data)
    uploadId = data['uploadId']

    cursor = mysql.connection.cursor()
    ImageDAO().delete(cursor, uploadId)
    mysql.connection.commit()

    flash('Captura de tela deletada com sucesso!', category='success')
    
    return jsonify({})

@images.route('/delete-upload', methods=['POST'])
@is_authenticated
def delete_upload():
    data = json.loads(request.data)
    uploadId = data['uploadId']

    cursor = mysql.connection.cursor()
    ImageDAO().delete(cursor, uploadId)
    mysql.connection.commit()
    
    return jsonify({})