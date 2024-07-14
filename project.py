from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))

    chapters = relationship('Chapter', backref='project')

    def __repr__(self):
        return f'<Project id={self.id} name="{self.name}">
        
