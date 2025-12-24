from boxcars_py import parse_replay

def test_parse_replay():
    with open("tests/replays/dec2025.replay", "rb") as f:
        buf = f.read()
    replay = parse_replay(buf)
    assert type(replay) == type({})
