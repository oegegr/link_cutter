import argparse
from app import app, db
from app.models import Url
from app.utils import encode_id

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--generate-test-data', action='store_true', help='if present, generate test data for db')
    parser.add_argument('-d', '--drop-tables', action='store_true', help='drop all exited tables')
    args = parser.parse_args()
    print(args)
    if args.drop_tables:
        db.drop_all()
        db.create_all()
    if args.generate_test_data:
        habr_urls = ['https://habrahabr.ru/all/page{}/'.format(i) for i in range(1,100)]
        for url in habr_urls:
            url = Url(long_url=url)
            db.session.add(url)
            db.session.flush()
            url.short_url = encode_id(url.id)
            db.session.add(url)
            db.session.commit()
    app.run(debug=True)




