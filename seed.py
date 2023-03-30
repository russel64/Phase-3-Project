from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pokemon, Stat, Move, User

engine = create_engine('sqlite:///pokemon.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

session.query(Pokemon).delete()
session.query(Move).delete()
session.query(Stat).delete()
session.query(User).delete()

p1 = Pokemon(name='Bulbasaur', type='Grass')
p1.moves = [Move(name='Vine Whip'), Move(name='Razor Leaf'), Move(name='Tackle'), Move(name='Leech Seed')]
p1.stats = [Stat(name='ATTACK', value=2), Stat(name='DEFENSE', value=4)]

p2= Pokemon(name='Squirtle', type='Water')
p2.moves = [Move(name='Bubblebeam'), Move(name='Tackle'), Move(name='Headbutt'), Move(name='Surf')]
p2.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p3 = Pokemon(name='Charmander', type='Fire')
p3.moves = [Move(name='Ember'), Move(name='Scratch'), Move(name='Tackle'), Move(name='Fire Punch')]
p3.stats = [Stat(name='ATTACK', value=4), Stat(name='DEFENSE', value=2)]

# p4 = Pokemon(name='Pikachu', type='Electric')
# p4.moves = [Move(name='Thunderbolt'), Move(name='Quick Attack'), Move(name='Iron Tail'), Move(name='Volt Tackle')]
# p4.stats = [Stat(name='ATTACK', value=4), Stat(name='DEFENSE', value=4)]

p5 = Pokemon(name='Chikorita', type='Grass')
p5.moves = [Move(name='Vine Whip'), Move(name='Tackle'), Move(name='Grass Knot'), Move(name='Energy Ball')]
p5.stats = [Stat(name='ATTACK', value=2), Stat(name='DEFENSE', value=4)]

p6 = Pokemon(name='Totodile', type='Water')
p6.moves = [Move(name='Scratch'), Move(name='Water Gun'), Move(name='Aqua Jet'), Move(name='Crunch')]
p6.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p7 = Pokemon(name='Cyndaquil', type='Fire')
p7.moves = [Move(name='Ember'), Move(name='Tackle'), Move(name='Flamethrower'), Move(name='Flame Charge')]
p7.stats = [Stat(name='ATTACK', value=5), Stat(name='DEFENSE', value=1)]

p8 = Pokemon(name='Treecko', type='Grass')
p8.moves = [Move(name='Pound'), Move(name='Bullet Seed'), Move(name='Aerial Ace'), Move(name='Grass Knot')]
p8.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p9 = Pokemon(name='Torchic', type='Fire')
p9.moves = [Move(name='Ember'), Move(name='Scratch'), Move(name='Flame Charge'), Move(name='Flamethrower')]
p9.stats = [Stat(name='ATTACK', value=4), Stat(name='DEFENSE', value=2)]

p10 = Pokemon(name='Mudkip', type='Water')
p10.moves = [Move(name='Tackle'), Move(name='Water Gun'), Move(name='Sludge'), Move(name='Dig')]
p10.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p11 = Pokemon(name='Turtwig', type='Grass')
p11.moves = [Move(name='Razor Leaf'), Move(name='Tackle'), Move(name='Seed Bomb'), Move(name='Body Slam')]
p11.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p12 = Pokemon(name='Piplup', type='Water')
p12.moves = [Move(name='Pound'), Move(name='Bubble'), Move(name='Drill Peck'), Move(name='Icy Wind')]
p12.stats = [Stat(name='ATTACK', value=2), Stat(name='DEFENSE', value=4)]

p13 = Pokemon(name='Chimchar', type='Fire')
p13.moves = [Move(name='Ember'), Move(name='Scratch'), Move(name='Flame Wheel'), Move(name='Flame Charge')]
p13.stats = [Stat(name='ATTACK', value=5), Stat(name='DEFENSE', value=1)]

p14 = Pokemon(name='Snivy', type='Grass')
p14.moves = [Move(name='Vine Whip'), Move(name='Tackle'), Move(name='Wrap'), Move(name='Seed Bomb')]
p14.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p15 = Pokemon(name='Oshawott', type='Water')
p15.moves = [Move(name='Tackle'), Move(name='Water Gun'), Move(name='Night Slash'), Move(name='Aqua Tail')]
p15.stats = [Stat(name='ATTACK', value=2), Stat(name='DEFENSE', value=4)]

p16 = Pokemon(name='Tepig', type='Fire')
p16.moves = [Move(name='Ember'), Move(name='Tackle'), Move(name='Flamethrower'), Move(name='Body Slam')]
p16.stats = [Stat(name='ATTACK', value=4), Stat(name='DEFENSE', value=2)]

p17 = Pokemon(name='Chespin', type='Grass')
p17.moves = [Move(name='Vine Whip'), Move(name='Take Down'), Move(name='Seed Bomb'), Move(name='Gyro Ball')]
p17.stats = [Stat(name='ATTACK', value=2), Stat(name='DEFENSE', value=4)]

p18 = Pokemon(name='Froakie', type='Water')
p18.moves = [Move(name='Pound'), Move(name='Bubble'), Move(name='Water Pulse'), Move(name='Surf')]
p18.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p19 = Pokemon(name='Fennekin', type='Fire')
p19.moves = [Move(name='Ember'), Move(name='Scratch'), Move(name='Flamethrower'), Move(name='Flame Charge')]
p19.stats = [Stat(name='ATTACK', value=4), Stat(name='DEFENSE', value=2)]

p20 = Pokemon(name='Rowlet', type='Grass')
p20.moves = [Move(name='Razor Leaf'), Move(name='Tackle'), Move(name='Seed Bomb'), Move(name='Energy Ball')]
p20.stats = [Stat(name='ATTACK', value=1), Stat(name='DEFENSE', value=5)]

p21 = Pokemon(name='Popplio', type='Water')
p21.moves = [Move(name='Pound'), Move(name='Water Gun'), Move(name='Aqua Jet'), Move(name='Water Pulse')]
p21.stats = [Stat(name='ATTACK', value=3), Stat(name='DEFENSE', value=3)]

p22 = Pokemon(name='Litten', type='Fire')
p22.moves = [Move(name='Ember'), Move(name='Scratch'), Move(name='Flamethrower'), Move(name='Flame Charge')]
p22.stats = [Stat(name='ATTACK', value=4), Stat(name='DEFENSE', value=2)]



u1 = User("1234")
u2 = User("5678")


session.add_all([u1, u2])
session.add_all([p1,p2,p3,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22])
session.commit()
