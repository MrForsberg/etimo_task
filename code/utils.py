import uuid


class Utils(object):

    @staticmethod
    def get_unique_id():
        return uuid.uuid4()

    @staticmethod
    def create_response_message(message, status):
        return {"message": message, "status": str(status)}

    @staticmethod
    def create_response_data(data, status):
        return {"data": data, "status": int(status)}
