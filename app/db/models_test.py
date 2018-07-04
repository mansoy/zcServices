from app.db.dbhelp import MsDbHelp

if __name__ == '__main__':
    sOdds = '0.700↑'
    if sOdds[-1:] == '↓':
        print('下箭头')
    elif sOdds[-1:] == '↑':
        print('上箭头')
    else:
        print('没有箭头')

    # ins = MsDbHelp.getInstance()
    # rets = ins.selectall('select * from b_lmatch where name=%(name)s', ({'name': '英超'}))
    # for ret in rets:
    #     print(ret)
