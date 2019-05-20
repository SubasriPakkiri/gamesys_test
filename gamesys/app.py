from flask import Flask, json, jsonify, make_response, g
from gamesys.resources.database import db_session, engine, init_db
import decimal, datetime


app = Flask(__name__)

init_db()


def alchemyEncoder(obj):
    if isinstance ( obj, datetime.date):
        return obj.isoformat()
    elif isinstance ( obj, decimal.Decimal):
        return float ( obj)

@app.teardown_appcontext
def shutdown_session(exception=None):
    g.db.close ( )
    db_session.remove()


@app.route('/members/total_wins/<int:member_id>', methods=['GET'])
@app.route('/members/total_wins/<int:member_id>/<int:activity_month>', methods=['GET'])
@app.route('/members/total_wins/<int:member_id>/<int:activity_month>/<int:game_id>', methods=['GET'])
def get_total_win_amount(member_id):
    connection = engine.connect()
    g.db = connection
    result_set = g.db.execute ('select member_id, sum(win_amount) as total_win_amounts from Revenue_Analysis where member_id = :member_id group by member_id',{'member_id': member_id})
    return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)


@app.route('/members/total_wagers/<int:member_id>', methods=['GET'])
@app.route('/members/total_wagers/<int:member_id>/<int:activity_month>', methods=['GET'])
@app.route('/members/total_wagers/<int:member_id>/<int:activity_month>/<int:game_id>', methods=['GET'])
def get_total_wager_amount(member_id):
    connection = engine.connect()
    g.db = connection
    result_set = g.db.execute ('select member_id, sum(wager_amount) as total_wager_amounts from Revenue_Analysis where member_id = :member_id group by member_id',{'member_id': member_id})
    return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)


@app.route('/members/wagers_placed/<int:member_id>', methods=['GET'])
@app.route('/members/wagers_placed/<int:member_id>/<int:activity_month>', methods=['GET'])
@app.route('/members/wagers_placed/<int:member_id>/<int:activity_month>/<int:game_id>', methods=['GET'])
def get_total_no_of_wagers(member_id):
    connection = engine.connect()
    g.db = connection
    result_set = g.db.execute ('select member_id, sum(number_of_wagers) as total_number_of_wagers from Revenue_Analysis where member_id = :member_id group by member_id',{'member_id': member_id})
    return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)





if __name__ == '__main__':
    app.run(debug=True)

