import interproLinkage as il
import unittest
import os.path

class TestinterproLinkage(unittest.TestCase):
    # Test formats
    def test_jsonld(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.jsonld")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.jsonld")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.jsonld") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.jsonld")

    def test_rdf(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.rdf")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.rdf")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.rdf") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.rdf")

    def test_ttl(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.ttl")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.ttl")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.ttl") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.ttl")
    
    def test_turtle(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle")

    def test_xml(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.xml")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.xml")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.xml") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.xml")

    def test_nt(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt")
    
    def test_n3(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.n3")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.n3")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.n3") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.n3")

    def test_trig(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trig")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trig")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trig") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trig")

    def test_trix(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trix")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trix")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trix") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.trix")

    def test_nquads(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nquads")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nquads")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nquads") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nquads")
    
    def test_turtle2(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle2")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle2")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle2") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.turtle2")

    def test_nt11(self):
        il.main("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.json", "./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt11")
        assert os.path.exists("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt11")
        assert os.path.getsize("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt11") > 1000
        #os.remove("./example/GCA_003004595.1.prodigal-Pfam.interproscan_small.nt11")


if __name__ == '__main__':
    unittest.main()

