from app.db.dbhelp import MsDbHelp


class DbModel:
    # 获取比赛数据
    @classmethod
    def getMatchData(cls, date, pageindex, num):
        sql = 'select A.*, B.name as lmname, C.name AS mtname, D.name AS dtname ' \
              'from matchdata AS A LEFT JOIN ' \
              '     b_lmatch AS B ON A.lsid = B.id LEFT JOIN ' \
              '     b_team AS C ON A.mteamid = C.id LEFT JOIN ' \
              '     b_team AS D ON A.dteamid = D.id '\
              'WHERE A.mdate = "{0}" ORDER BY A.id LIMIT {1}, {2}'.format(date, (pageindex - 1) * num, num)
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    # 获取亚赔数据
    @classmethod
    def getYaOddsData(cls, itype, mid, pageindex, num):
        sql = 'SELECT A.*, C.name AS lyname '\
              'FROM {0} AS A INNER JOIN  '\
              '	    {1} AS B ON A.mid = B.mid INNER JOIN '\
              '     b_lottery AS C ON A.lyid = C.id '\
              'WHERE B.id = {2} ORDER BY A.id LIMIT {3}, {4}'.format(
                'yaodds' if itype == 0 else 'interyaodds',
                'matchdata' if itype == 0 else 'intermatch',
                mid,
                (pageindex - 1) * num, num)
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    # 获取亚赔数据
    @classmethod
    def getOuOddsData(cls, itype, mid, pageindex, num):
        sql = 'SELECT A.*, C.name AS lyname ' \
              'FROM {0} AS A INNER JOIN  ' \
              '	    {1} AS B ON A.mid = B.mid INNER JOIN ' \
              '     b_lottery AS C ON A.lyid = C.id ' \
              'WHERE B.id = {2} ORDER BY A.id LIMIT {3}, {4}'.format(
                    'ouodds' if itype == 0 else 'interouodds',
                    'matchdata' if itype == 0 else 'intermatch',
                    mid,
                    (pageindex - 1) * num, num)
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    # 获取大小指数数据
    @classmethod
    def getSizeOddsData(cls, itype, mid, pageindex, num):
        sql = 'SELECT A.*, C.name AS lyname ' \
              'FROM {0} AS A INNER JOIN  ' \
              '	    {1} AS B ON A.mid = B.mid INNER JOIN ' \
              '     b_lottery AS C ON A.lyid = C.id ' \
              'WHERE B.id = {2} ORDER BY A.id LIMIT {3}, {4}'.format(
                    'sizeodds' if itype == 0 else 'intersizeodds',
                    'matchdata' if itype == 0 else 'intermatch',
                    mid, (pageindex - 1) * num, num)
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    @classmethod
    def getTeamData(cls):
        sql = 'SELECT id, name FROM b_team'
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    @classmethod
    def getLMatchData(cls, cid=None):
        sql = 'SELECT id, cid, name, fullname FROM b_lmatch'
        if cid != None:
            sql = '{0} WHERE cid={1}'.format(sql, cid)
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    @classmethod
    def getScore(cls, lsname):
        sql = 'SELECT A.*, B.name as lsname, C.name as teamname '\
              'from lsscore AS A INNER JOIN '\
              ' b_lmatch AS B ON A.lsid = B.id INNER JOIN '\
              ' b_team AS C on A.tid = C.id '\
              'where B.name = "{0}" order by A.score desc'.format(lsname)
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    @classmethod
    def getCountrys(cls):
        sql = 'SELECT id, name FROM b_country;'
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets

    @classmethod
    def getInterMatch(cls, lsName):
        sql = '''
            SELECT D.name AS lyname, E.name AS mtname, F.name AS dtname, A.*, B.avgodds11, B.avgodds12, B.avgodds13, C.odds11, C.odds12, C.odds13 
            FROM intermatch AS A LEFT JOIN
            (
                SELECT mid, format(avg(odds11),2) as avgodds11, format(avg(odds12),2) AS avgodds12, format(avg(odds13),2) AS avgodds13
                FROM interouodds
                WHERE mid IN (SELECT mid FROM intermatch)
                GROUP BY mid
            ) AS B ON A.mid = B.mid LEFT JOIN
            (
                SELECT mid, odds11, odds12, odds13
                FROM interouodds AS AA INNER JOIN
                    b_lottery AS BB ON AA.lyid = BB.id
                WHERE AA.mid IN (SELECT mid FROM intermatch WHERE BB.name='竞彩官方')
            ) AS C ON A.mid = C.mid LEFT JOIN
            b_lmatch AS D ON A.lsid = D.id LEFT JOIN
            b_team AS E on A.mtid = E.id LEFT JOIN
            b_team AS F ON A.dtid = F.id
            WHERE D.name = "{0}"
            ORDER BY mdate, mtime
            '''.format(lsName)
        __ins = MsDbHelp.getInstance()
        rets = __ins.selectall(sql)
        return rets
