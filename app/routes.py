import os, re
from flask import render_template, redirect, url_for, request, send_from_directory, abort

from app import app, db
from app.forms import URLConverterForm
from app.models import Url
from app.utils import encode_id, decode_id


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLConverterForm()
    if form.validate_on_submit():
        url = Url.query.filter_by(long_url=form.url.data).first()
        if url is None:
            url = Url(long_url=form.url.data)
            db.session.add(url)
            db.session.flush()
            url.short_url = encode_id(url.id)
            db.session.add(url)
            db.session.commit()
        form.url.data = request.base_url + url.short_url
    return render_template('index.html', form=form)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/<short_url>')
def go_to_short_url(short_url):
    if re.match('^[A-za-z2-9]*$', short_url) is None:
        abort(404)
    id = decode_id(short_url)
    url = Url.query.get(id)
    if url is None:
        abort(404)

    return redirect(url.long_url)
