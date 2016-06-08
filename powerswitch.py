
tell={'router':'on','switch':'on'}


def status(device,set_status):

    if device is None:
        return tell

    if device not in tell:
        return {'error':"device not found"}


    if set_status is None:
        return {device:tell[device]}

    if set_status not in ['on','off']:
        return {'error':"wrong status"}

    tell[device]=set_status

    return {device:set_status}






