from .aprendiz_bp import apr_bp
from .curso_bp import cur_bp
from .evaluacion_bp import eva_bp
from .imparte_bp import imp_bp
from .instructor_bp import inst_bp
from .matricula_bp import mat_bp
from .mat_eva_bp import mat_eva_bp
from .persona_bp import per_bp


def loadRouters(app):
    app.register_blueprint(apr_bp, url_prefix='/aprendiz')
    app.register_blueprint(cur_bp, url_prefix='/curso')
    app.register_blueprint(eva_bp, url_prefix='/evaluacion')
    app.register_blueprint(imp_bp, url_prefix='/imparte')
    app.register_blueprint(inst_bp, url_prefix='/instructor')
    app.register_blueprint(mat_bp, url_prefix='/matricula')
    app.register_blueprint(mat_eva_bp, url_prefix='/mat_eva')
    app.register_blueprint(per_bp, url_prefix='/persona')