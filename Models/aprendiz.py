class Aprendiz:

    def __init__(self, apr_id, apr_uuid, apr_fecha_nac, apr_per_id):
        self.__apr_id        = apr_id
        self.__apr_uuid      = apr_uuid
        self.__apr_fecha_nac = apr_fecha_nac
        self.__apr_per_id    = apr_per_id

    # la tupla se convierte en un obj y ese obj en dic
    def to_dict(self):
        return {
            "apr_id": self.__apr_id,
            "apr_uuid": self.__apr_uuid,
            "apr_fecha_nac": self.__apr_fecha_nac,
            "apr_per_id": self.__apr_per_id
        }
