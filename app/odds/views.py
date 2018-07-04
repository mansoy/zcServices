from . import odds
from flask import render_template, request, g as msGlobal


@odds.route('/analys')
def dataAnalys():
    msGlobal.daclass = 'Appoint'
    return render_template('shujufenxi.html')


@odds.route('/yapei')
def yaOdds():
    sMid = request.args.get('mid')
    if sMid == None:
        return '参数错误'
    else:
        msGlobal.yaclass = 'Appoint'
        return render_template('yapanduibi.html')


@odds.route('/')
@odds.route('/oupei')
def ouOdds():
    sMid = request.args.get('mid')
    if sMid == None:
        return '参数错误'
    else:
        msGlobal.ouclass = 'Appoint'
        return render_template('baijiaoupei.html')


@odds.route('/bf')
def bfOdds():
    sMid = request.args.get('mid')
    if sMid == None:
        return '参数错误'
    else:
        msGlobal.bfclass = 'Appoint'
        return render_template('bifenzhishu.html')

@odds.route('/rq')
def rqOdds():
    sMid = request.args.get('mid')
    if sMid == None:
        return '参数错误'
    else:
        msGlobal.rqclass = 'Appoint'
        return render_template('rangqiuzhishu.html')

@odds.route('/size')
def sizeOdds():
    sMid = request.args.get('mid')
    if sMid == None:
        return '参数错误'
    else:
        msGlobal.dxclass = 'Appoint'
        return render_template('daxiaozhishu.html')  # , datas=rets)
