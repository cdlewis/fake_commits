from RockStar import RockStar
python_code = open( "hello.py" ).read()
rock_it_bro = RockStar(days=300, filename='hello.py', code=python_code)
rock_it_bro.make_me_a_rockstar()
