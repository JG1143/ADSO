class Persona:

    def __init__(self, per_id, per_uuid, per_pri_nombre, per_seg_nombre, per_pri_apellido, per_seg_apellido, per_documento):
        self.__per_id           = per_id
        self.__per_uuid         = per_uuid
        self.__per_pri_nombre   = per_pri_nombre
        self.__per_seg_nombre   = per_seg_nombre
        self.__per_pri_apellido = per_pri_apellido
        self.__per_seg_apellido = per_seg_apellido
        self.__per_documento    = per_documento

    def to_dict(self): 
        return {
            "per_id": self.__per_id,
            "per_uuid": self.__per_uuid,
            "per_pri_nombre": self.__per_pri_nombre,
            "per_seg_nombre": self.__per_seg_nombre,
            "per_pri_apellido": self.__per_pri_apellido,
            "per_seg_apellido": self.__per_seg_apellido,
            "per_documento": self.__per_documento
        }