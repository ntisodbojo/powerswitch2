
tell={'infrastructure':0,'router':0,'switch':0}


def status(device,set_status):

    if device is None:
        return tell

    if device not in tell:
        return {'error':"device not found"}


    if set_status is None:
        return {device:tell[device]}

    if set_status not in [1,2]:
        return {'error':"wrong status"}

    tell[device]=set_status

    return {device:set_status}






