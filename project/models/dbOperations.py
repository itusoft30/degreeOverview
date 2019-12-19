from project import login_manager
from project.models.models import *
from project.config.Database import db

newStudent = RegUser(name="student",surname="itu",email="st@itu.edu.tr",password="gAAAAABd-q3zvxtASOAf20AL0Qz2cKsnPFzH1Ja0MtlFjToU5Dzgv2GuD_j8_hsoPsQv9-y_X-K94OHatvZwUUvrD4bftwxLeQ==",user_type="2")
newInstructer = RegUser(name="inst",surname="itu",email="inst@itu.edu.tr",password="gAAAAABd-q3zV0j-USRHcWhrrJI7l05JaHNif4A2z47OsMGdV-suafTjWiBgT85OxUksqKxzd5Z5WIGhk_aYRUdNdqQAPzizaw==",user_type="1")

#db.session.add(newStudent)
#db.session.add(newInstructer)
#db.session.commit()

print(RegUser.query.all())


