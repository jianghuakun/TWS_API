import pymysql
class db127:
    itri_ota = pymysql.connect(
        host='192.168.75.245',
        port=6666,
        user='test@people',
        passwd='test@people-mysql@@',
        db='itri-ota',
        autocommit=True
    )
    itri_t_server = pymysql.connect(
        host='192.168.75.245',
        port=6666,
        user='test@people',
        passwd='test@people-mysql@@',
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

    itri_ota_cursor = itri_ota.cursor()
    itri_t_server_cursor = itri_t_server.cursor()
    '''
    device_mycursor = device.cursor()
    video_cursor=video.cursor()
    '''


