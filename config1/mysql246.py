import pymysql
class db246:
    ota = pymysql.connect(
        host='192.168.75.246',
        port=6666,
        user='root',
        passwd='ITRI@mysql-class#production',
        db='itri-ota',
        autocommit=True
    )
    t_server = pymysql.connect(
        host='192.168.75.246',
        port=6666,
        user='root',
        passwd='ITRI@mysql-class#production',
        db='db_headset_platform',
        autocommit=True
    )
    '''
    device = pymysql.connect(
        '192.168.75.245',
        'root',
        'r03test123456',
        'device',
        autocommit=True
    )
    video = pymysql.connect(
        '192.168.75.245',
        'root',
        'r03test123456',
        'video',
        autocommit=True
    )
    '''

    itri_ota_cursor = ota.cursor()
    t_server_cursor = t_server.cursor()

    '''
    device_mycursor = device.cursor()
    video_cursor=video.cursor()
    '''


