from typing import List, Dict
from resources.aviationweather import get_metar, get_taf, get_stationinfo

def get_wx(station_ids: List)->Dict:
    ids_query_param = ','.join(station_ids)

    all_metar_message: str = get_metar({ 'ids': ids_query_param })
    all_taf_message: str = get_taf({ 'ids': ids_query_param })
    all_stationinfo_message: str = get_stationinfo({ 'ids': ids_query_param })

    # Metar は改行区切りでid毎に出力される
    metar_messages = all_metar_message.split('\n')

    # TAFは'TAF'を区切りにして出力
    taf_messages_temp = all_taf_message.split('TAF ')
    taf_messages = []
    for msg in taf_messages_temp:
        msg = 'TAF ' + msg
        taf_messages.append(msg)

    # stationinfo は'STATION INFO for'を区切り文字にする
    stationinfo_messages = all_stationinfo_message.split('STATION INFO for ')

    wx = {}
    for station_id in station_ids:
        wx[station_id] = {
            'metar': {
                'text': '',
                'html': ''
            },
            'taf': {
                'text': '',
                'html': ''
            },
            'stationinfo': {
                'text': '',
                'html': '',
            }
        }

        # Metar
        metar_messages_filtered = [metar_message for metar_message in metar_messages if str(station_id) in metar_message]

        if (len(metar_messages_filtered) > 0):
            wx[station_id]['metar']['text'] = metar_messages_filtered[0]
            wx[station_id]['metar']['html'] = metar_messages_filtered[0]

        # Taf
        taf_messages_filtered = [taf_message for taf_message in taf_messages if str(station_id) in taf_message]

        if (len(taf_messages_filtered) > 0):
            wx[station_id]['taf']['text'] = taf_messages_filtered[0]
            wx[station_id]['taf']['html'] = taf_messages_filtered[0].replace('\n', '<br>')

        # Station Info
        stationinfo_messages_filtered = [stationinfo_message for stationinfo_message in stationinfo_messages if str(station_id) in stationinfo_message]

        if (len(stationinfo_messages_filtered) > 0):
            wx[station_id]['stationinfo']['text'] = stationinfo_messages_filtered[0]
            wx[station_id]['stationinfo']['html'] = stationinfo_messages_filtered[0].replace('\n', '<br>')

    return wx
