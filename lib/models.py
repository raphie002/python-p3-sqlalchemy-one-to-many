# lib/models.py
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData # type: ignore
from sqlalchemy.orm import relationship, backref # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# Define the Game model
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    platform = Column(String)
    genre = Column(String)
    price = Column(Integer)

    # Define the one-to-many relationship with Review
    # 'reviews' will be an attribute on Game instances to access related Review objects
    # backref='game' creates a 'game' attribute on Review objects to access the parent Game
    reviews = relationship('Review', backref='game')

    def __repr__(self):
        return f"Game(id={self.id}, " \
               f"title='{self.title}', " \
               f"platform='{self.platform}', " \
               f"genre='{self.genre}', " \
               f"price={self.price})"

# Define the Review model
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    
    # Define the foreign key relationship to the games table
    game_id = Column(Integer, ForeignKey('games.id'))

    def __repr__(self):
        return f"Review(id={self.id}, " \
               f"score={self.score}, " \
               f"comment='{self.comment}', " \
               f"game_id={self.game_id})"