from . import data
from flask import request, jsonify
from .. import models
import arrow
import json


@data.route('/match', methods=['GET'])
def match():
    sdate = request.args.get('date', '', type=str)
    pageindex = request.args.get('pageindex', 1, type=int)
    num = request.args.get('num', 30, type=int)
    if sdate == '':
        sdate = arrow.now().format('YYYY-MM-DD')
    rets = models.DbModel.getMatchData(sdate, pageindex, num)
    return jsonify(rets)


# 亚赔数据
@data.route('/yapei', methods=['GET'])
def yapei():
    smid = request.args.get('mid', -1, type=int)
    itype = request.args.get('type', 0, type=int)
    pageindex = request.args.get('pageindex', 1, type=int)
    num = request.args.get('num', 30, type=int)
    if smid == -1:
        return '参数错误'
    else:
        rets = models.DbModel.getYaOddsData(itype, smid, pageindex, num)
        return jsonify(rets)


# 欧赔数据
@data.route('/oupei')
def oupei():
    smid = request.args.get('mid', -1, type=int)
    itype = request.args.get('type', 0, type=int)
    pageindex = request.args.get('pageindex', 1, type=int)
    num = request.args.get('num', 30, type=int)
    if smid == -1:
        return '参数错误'
    else:
        rets = models.DbModel.getOuOddsData(itype, smid, pageindex, num)
        return jsonify(rets)


# 大小指数路由
@data.route('/exponent')
def exponent():
    smid = request.args.get('mid', -1, type=int)
    itype = request.args.get('type', 0, type=int)
    pageindex = request.args.get('pageindex', 1, type=int)
    num = request.args.get('num', 30, type=int)
    if smid == -1:
        return '参数错误'
    else:
        rets = models.DbModel.getSizeOddsData(itype, smid, pageindex, num)
        return jsonify(rets)


# 获取球队数据
@data.route('/team', methods=['GET'])
def getteamdata():
    rets = models.DbModel.getTeamData()
    return jsonify(rets)


# 国家
@data.route('/coun', methods=['GET'])
def getCountry():
    cous = models.DbModel.getCountrys()
    return jsonify(cous)


# 获取联赛数据
@data.route('/lmatch', methods=['GET'])
def getlmatchdata():
    cid = request.args.get('cid', -1, type=int)
    if cid == -1:
        return '参数错误'
    else:
        lms = models.DbModel.getLMatchData(cid)
        return jsonify(lms)
    # cous = models.DbModel.getCountrys()
    # lms = models.DbModel.getLMatchData()

    # for cou in cous:
    #     __json = json.loads('{}')
    #     cid = cou['id']
    #     __json['id'] = cid
    #     __json['name'] = cou['name']
    #
    #     # __jsLms = json.loads('[]')
    #     # for lm in lms:
    #     #     __jsLm = json.loads('{}')
    #     #     if lm['cid'] == cid:
    #     #         __jsLm['id'] = lm['id']
    #     #         __jsLm['name'] = lm['name']
    #     #         __jsLm['fullname'] = lm['fullname']
    #     #         __jsLms.append(__jsLm)
    #     # __json['lmatch'] = __jsLms
    #     retJson.append(__json)
    # return jsonify(cous)


# 获取球队排名
@data.route('score', methods=['GET'])
def getScore():
    lsName = request.args.get('lsname', '', type=str)
    if lsName == '':
        return '参数错误'
    else:
        rets = models.DbModel.getScore(lsName)
        return jsonify(rets)


# 获取世界杯数据
@data.route('wc', methods=['GET'])
def getWcData():
    rets = models.DbModel.getInterMatch('世界杯')
    return jsonify(rets)



