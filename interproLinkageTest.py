import interproLinkage as il
import unittest
import os.path
from os.path import exists, getsize

class TestinterproLinkage(unittest.TestCase):
    # Test formats
    def test_jsonld(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.jsonld")
        assert exists("./example/iprscan5-JobID.jsonld")
        assert getsize("./example/iprscan5-JobID.jsonld") > 1000
        os.remove("./example/iprscan5-JobID.jsonld")

    def test_rdf(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.rdf")
        assert exists("./example/iprscan5-JobID.rdf")
        assert getsize("./example/iprscan5-JobID.rdf") > 1000
        os.remove("./example/iprscan5-JobID.rdf")

    def test_ttl(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.ttl")
        assert exists("./example/iprscan5-JobID.ttl")
        assert getsize("./example/iprscan5-JobID.ttl") > 1000
        os.remove("./example/iprscan5-JobID.ttl")
    
    def test_turtle(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.turtle")
        assert exists("./example/iprscan5-JobID.turtle")
        assert getsize("./example/iprscan5-JobID.turtle") > 1000
        os.remove("./example/iprscan5-JobID.turtle")

    def test_xml(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.xml")
        assert exists("./example/iprscan5-JobID.xml")
        assert getsize("./example/iprscan5-JobID.xml") > 1000
        os.remove("./example/iprscan5-JobID.xml")

    def test_nt(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.nt")
        assert exists("./example/iprscan5-JobID.nt")
        assert getsize("./example/iprscan5-JobID.nt") > 1000
        os.remove("./example/iprscan5-JobID.nt")
    
    def test_n3(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.n3")
        assert exists("./example/iprscan5-JobID.n3")
        assert getsize("./example/iprscan5-JobID.n3") > 1000
        os.remove("./example/iprscan5-JobID.n3")

    def test_trig(self):
        il.main("./example/iprscan5-JobID.json", "./example/iprscan5-JobID.trig")
        assert exists("./example/iprscan5-JobID.trig")
        assert getsize("./example/iprscan5-JobID.trig") > 1000
        os.remove("./example/iprscan5-JobID.trig")

if __name__ == '__main__':
    unittest.main()

