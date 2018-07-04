from . import main
from flask import render_template, request, g as msGlobal


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/wc')
def worldcup():
    group = request.args.get('group', '', type=str)
    if group == '':
        return render_template('worldcup.html')
    else:
        return render_template('worldcup_{0}.html'.format(group))


@main.route('/yingchao')
def yingchao():
    return render_template('yingchao.html')


# @main.route('/da/')
# @main.route('/da/oupei')
# def daOupei():
#     sMid = request.args.get('mid')
#     if sMid == None:
#         return '参数错误'
#     else:
#         # rets = models.DbModel.getOuOddsData(sMid)
#         # for ret in rets:
#         #     print(ret)
#         msGlobal.ouclass = 'Appoint'
#         return render_template('baijiaoupei.html')
#
#
# @main.route('/da/yapei')
# def daYaPei():
#     # sDate = request.form.get('date')
#     # if sDate == None:
#     #     sDate = arrow.now().format('YYYY-MM-DD')
#     sMid = request.args.get('mid')
#     if sMid == None:
#         return '参数错误'
#     else:
#         # rets = models.DbModel.getYaOddsData(sMid)
#         # for ret in rets:
#         #     print(ret)
#         msGlobal.yaclass = 'Appoint'
#         return render_template('yapanduibi.html') # , datas=rets)
#
#
# @main.route('/da/analys')
# def daDataAnalys():
#     msGlobal.daclass = 'Appoint'
#     return render_template('shujufenxi.html')
#
#
# @main.route('/da/size')
# def daSize():
#     sMid = request.args.get('mid')
#     if sMid == None:
#         return '参数错误'
#     else:
#         # rets = models.DbModel.getYaOddsData(sMid)
#         # for ret in rets:
#         #     print(ret)
#         msGlobal.dxclass = 'Appoint'
#         return render_template('daxiaozhishu.html')  # , datas=rets)


