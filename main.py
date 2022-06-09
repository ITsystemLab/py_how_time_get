# datetimeをインポート
import datetime

# タイムゾーンを設定(日本時間を取得するため)
timezone = datetime.timezone(datetime.timedelta(hours=9))

# 現在時刻を取得
date = datetime.datetime.now(timezone)


# 出力
print( date )
print( "年: " + str(date.year) )
print( "月: " + str(date.month) )
print( "日: " + str(date.day) )
print( "曜日(日»0, 土»6): " + str(int(date.weekday())) )
print( "時間: " + str(date.hour) )
print( "分: " + str(date.minute) )
print( "秒: " + str(date.second) )
print( "ミリ秒: " + str(date.microsecond) )


# 見やすいように
year = str(date.year) # 年
month = str(date.month) # 月
day = str(date.day) # 日
hour = str(date.hour) # 時
minute = str(date.minute) # 分
second = str(date.second) # 秒
microsecond = str(date.microsecond) # ミリ秒

# 曜日を定義
week = ["日","月","火","水","木","金","土"]
weekday = week[int(date.weekday())]

# 出力
print( year + "年" + month + "月" + day + "日（" + weekday + "）" + hour + "時" + minute + "分" + second + "秒" + microsecond  )


"""
時間の引き算をしよう！
"""

# 2003年8月24日を定義
birthday = datetime.datetime(2003, 8, 24, 0, 0, 0, 0, tzinfo=timezone) # datetime.datetime(年, 月, 日, 時, 分, 秒, ミリ秒, タイムゾーン

# 現在時刻 - 2003年8月24日 (経過時間)
difference = datetime.datetime.fromtimestamp((date.timestamp() - birthday.timestamp()))

# 見やすい形にするために定義
d_year = str(difference.year - 1970) # 年 0が1970年なので1970を引く
d_month = str(difference.month ) # 月
d_day = str(difference.day ) # 日
d_hour = str(difference.hour) #時
d_minute = str(difference.minute) # 分
d_second = str(difference.second) # 秒
d_microsecond = str(difference.microsecond) # ミリ秒

# 出力
print( d_year + "年" + d_month + "ヶ月" + d_day + "日" + d_hour + "時間" + d_minute + "分" + d_second + "秒" + d_microsecond  )
