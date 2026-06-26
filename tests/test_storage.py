from shelf.models import Note 
from shelf import storage

def test_path(tmp_path):

    path = tmp_path / "test.json"
    note = Note(title='test', body='hello', tags=['test_file']) # inside of the Note dataclass, id & created_at will be generated on their own.
    storage.save([note], path)
    loaded = storage.load(path)

    assert loaded[0].title == note.title
    assert loaded[0].tags == note.tags

def test_missing_file(tmp_path):

    path = tmp_path / "../noteven/a/real/path"

    loaded = storage.load(path)

    assert loaded == []
