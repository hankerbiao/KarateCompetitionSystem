from sqlmodel import Field, SQLModel, create_engine, Session, select, Relationship
from typing import List, Optional


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    heroes: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")


sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    team_justice_league = Team(name="Justice League")
    team_avengers = Team(name="Avengers")

    session.add(team_justice_league)
    session.add(team_avengers)
    session.commit()

    hero_superman = Hero(name="Superman", secret_name="Clark Kent", age=30, team_id=team_justice_league.id)
    hero_batman = Hero(name="Batman", secret_name="Bruce Wayne", age=35, team_id=team_justice_league.id)
    hero_spiderman = Hero(name="Spider-Man", secret_name="Peter Parker", age=18, team_id=team_avengers.id)

    session.add(hero_superman)
    session.add(hero_batman)
    session.add(hero_spiderman)
    session.commit()

# with Session(engine) as session:
    statement = select(Hero).where(Hero.team_id == team_justice_league.id)
    results = session.exec(statement)
    for hero in results:
        print(f"Hero: {hero.name}, Team: {hero.team.name}")
