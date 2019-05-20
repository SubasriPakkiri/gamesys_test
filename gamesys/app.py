from flask import Flask, json, jsonify, make_response
from gamesys.Resources.database import db_session, engine, init_db
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
    db_session.remove()



@app.route('/members/total_wins/<int:member_id>', defaults={'activity_year_month': None, 'game_id': None}, methods=['GET'])
@app.route('/members/total_wins/<int:member_id>/<int:activity_year_month>', defaults={'game_id': None}, methods=['GET'])
@app.route('/members/total_wins/<int:member_id>/<int:activity_year_month>/<int:game_id>', methods=['GET'])
def get_total_win_amount(member_id, activity_year_month, game_id):
    connection = engine.connect()
    if activity_year_month==None and game_id==None:
        result_set =connection.execute('select member_id, sum(win_amount) as total_win_amounts from Revenue_Analysis where member_id = :member_id group by member_id',{'member_id': member_id})
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)
    elif activity_year_month!=None and game_id==None:
        result_set = connection.execute('select member_id,activity_year_month, sum(win_amount) as total_win_amounts_per_month from Revenue_Analysis where member_id = :member_id and activity_year_month = :activity_year_month group by member_id,activity_year_month' ,{'member_id' : member_id, 'activity_year_month' : activity_year_month} )
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)
    elif activity_year_month!=None and game_id!=None:
        result_set = connection.execute('select member_id, activity_year_month, game_id, sum(win_amount) as total_win_amounts_per_game_per_month from Revenue_Analysis where member_id = :member_id and activity_year_month = :activity_year_month and game_id = :game_id group by member_id,activity_year_month,game_id' ,{'member_id' : member_id, 'activity_year_month' : activity_year_month, 'game_id' : game_id} )
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)

@app.route('/members/total_wagers/<int:member_id>', defaults={'activity_year_month': None, 'game_id': None}, methods=['GET'])
@app.route('/members/total_wagers/<int:member_id>/<int:activity_year_month>', defaults={'game_id': None} ,methods=['GET'])
@app.route('/members/total_wagers/<int:member_id>/<int:activity_year_month>/<int:game_id>', methods=['GET'])
def get_total_wager_amount(member_id, activity_year_month, game_id):
    connection = engine.connect()
    if activity_year_month==None and game_id==None:
        result_set = connection.execute ('select member_id, sum(wager_amount) as total_wager_amounts from Revenue_Analysis where member_id = :member_id group by member_id',{'member_id': member_id})
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)
    elif activity_year_month!=None and game_id==None:
        result_set = connection.execute ('select member_id,activity_year_month, sum(wager_amount) as total_wager_amounts_per_month from Revenue_Analysis where member_id = :member_id and activity_year_month = :activity_year_month group by member_id,activity_year_month' ,{'member_id' : member_id, 'activity_year_month' : activity_year_month} )
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)
    elif activity_year_month!=None and game_id!=None:
        result_set = connection.execute ('select member_id,activity_year_month, game_id, sum(wager_amount) as total_wager_amounts_per_month_per_game from Revenue_Analysis where member_id = :member_id and activity_year_month = :activity_year_month and game_id = :game_id group by member_id,activity_year_month,game_id' ,{'member_id' : member_id,  'activity_year_month' : activity_year_month,'game_id' : game_id} )
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)


@app.route('/members/wagers_placed/<int:member_id>', defaults={'activity_year_month': None, 'game_id': None}, methods=['GET'])
@app.route('/members/wagers_placed/<int:member_id>/<int:activity_year_month>', defaults={'game_id': None} ,methods=['GET'])
@app.route('/members/wagers_placed/<int:member_id>/<int:activity_year_month>/<int:game_id>', methods=['GET'])
def get_total_no_of_wagers(member_id, activity_year_month, game_id):
    connection = engine.connect()
    if activity_year_month==None and game_id==None:
        result_set = connection.execute ('select member_id, sum(number_of_wagers) as total_wager_amounts from Revenue_Analysis where member_id = :member_id group by member_id',{'member_id': member_id})
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)
    elif activity_year_month!=None and game_id==None:
        result_set = connection.execute ('select member_id,activity_year_month, sum(number_of_wagers) as number_of_wagers_per_month from Revenue_Analysis where member_id = :member_id and activity_year_month = :activity_year_month group by member_id,activity_year_month' ,{'member_id' : member_id, 'activity_year_month' : activity_year_month} )
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)
    elif activity_year_month!=None and game_id!=None:
        result_set = connection.execute ('select member_id,activity_year_month, game_id, sum(number_of_wagers) as number_of_wagers_per_month_per_game from Revenue_Analysis where member_id = :member_id and activity_year_month = :activity_year_month and game_id = :game_id group by member_id,activity_year_month,game_id' ,{'member_id' : member_id,  'activity_year_month' : activity_year_month,'game_id' : game_id} )
        return json.dumps([dict(r) for r in result_set], default=alchemyEncoder)

if __name__ == '__main__':
    app.run(debug=True)

