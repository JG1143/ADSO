class Instructor:

    def __init__(self, ins_id, ins_uuid, ins_especialidad, ins_per_id):
        self.__ins_id           = ins_id
        self.__ins_uuid         = ins_uuid
        self.__ins_especialidad = ins_especialidad
        self.__ins_per_id       = ins_per_id


    def to_dict(self):
        return {
            "ins_id": self.__ins_id,
            "ins_uuid": self.__ins_uuid,
            "ins_especialidad": self.__ins_especialidad,
            "ins_per_id": self.__ins_per_id
        }