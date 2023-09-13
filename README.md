# interproscan-to-linked-data
Convert interproscan json format to linked data format (rdf, turtle, json-ld, n3, xml, nquad, trix, trig)


Run interproscan with the example protein sequence on [interproscan](https://www.ebi.ac.uk/interpro/search/sequence/)

```
>example protein sequence
MITIDGNGAV ASVAFRTSEV IAIYPITPSST MAEQADAWAGN GLKNVWGDTP RVVEMQSEAG
AIATVHGALQ TGALSTSFTS SQGLLLMIPTL YKLAGELTPFV LHVAARTVAT HALSIFGDHS
DVMAVRQTGC AMLCAANVQE AQDFALISQIA TLKSRVPFIHF FDGFRTSHEI NKIVPLADDT
ILDLMPQVEI DAHRARALNP EHPVIRGTSAN PDTYFQSREAT NPWYNAVYDH VEQAMNDFSA
ATGRQYQPFE YYGHPQAERV IILMGSAIGTC EEVVDELLTRG EKVGVLKVRL YRPFSAKHLL
QALPGSVRSV AVLDRTKEPG AQAEPLYLDVM TALAEAFNNGE RETLPRVIGG RYGLSSKEFG
PDCVLAVFAE LNAAKPKARF TVGIYDDVTNL SLPLPENTLPN SAKLEALFYG LGSDGSVSAT
KNNIKIIGNS TPWYAQGYFV YDSKKAGGLTV SHLRVSEQPIR SAYLISQADF VGCHQLQFID
KYQMAERLKP GGIFLLNTPY SADEVWSRLPQ EVQAVLNQKKA RFYVINAAKI ARECGLAARI
NTVMQMAFFH LTQILPGDSA LAELQGAIAKS YSSKGQDLVER NWQALALARE SVEEVPLQPV
NPHSANRPPV VSDAAPDFVK TVTAAMLAGLG DALPVSALPPD GTWPMGTTRW EKRNIAEEIP
IWKEELCTQC NHCVAACPHS AIRAKVVPPEA MENAPASLHSL DVKSRDMRGQ KYVLQVAPED
CTGCNLCVEV CPAKDRQNPE IKAINMMSRLE HVEEEKINYDF FLNLPEIDRS KLERIDIRTS
QLITPLFEYS GACSGCGETP YIKLLTQLYGD RMLIANATGCS SIYGGNLPST PYTTDANGRG
PAWANSLFED NAEFGLGFRL TVDQHRVRVLR LLDQFADKIPA ELLTALKSDA TPEVRREQVA
ALRQQLNDVA EAHELLRDAD ALVEKSIWLIG GDGWAYDIGFG GLDHVLSLTE NVNILVLDTQ
CYSNTGGQAS KATPLGAVTK FGEHGKRKARK DLGVSMMMYGH VYVAQISLGA QLNQTVKAIQ
EAEAYPGPSL IIAYSPCEEH GYDLALSHDQM RQLTATGFWPL YRFDPRRADE GKLPLALDSR
PPSEAPEETL LHEQRFRRLN SQQPEVAEQLW KDAAADLQKRY DFLAQMAGKA EKSNTD
```

Save the results in json format

Running the script
```
python3 interproLinkage.py [-h] [-i INPUT] [-o OUTPUT]
```

For the example file assuming your terminal is active in the git repo. 
```
python3 interproLinkage.py -i example/iprscan5-[JobID].json -o iprscan5-[JobID].ttl
```

Querying the created turtle file using SPARQL in GraphDB,
We want all PFAM annotations that match and match's evalue with description of the domain. 
```
PREFIX ns1: <https://www.ebi.ac.uk/interpro/>
SELECT DISTINCT ?accession ?evalue ?description
WHERE {
  # Define HMM library
  VALUES ?library {"PFAM"}

  # Get evalue creating redundant variable ?k
  ?k ns1:evalue ?evalue .

  # Get the parent location variable. 
  ?location ns1:locations ?k .
 
  # Create a path from the library to the overlapping parent location for linkage. 
  ?lib_parent ns1:library ?library .
  ?entry ns1:accession ?accession ; 
         ns1:signatureLibraryRelease ?lib_parent .
  ?location ns1:signature ?entry .

  # Match the description to the PFAM annotation entry. 
  ?entry ns1:description ?description .  
}
```

example output, the exact output can change as knowledge increases. 
| accession | evalue                | description                                         |
|-----------|-----------------------|-----------------------------------------------------|
| "PF17147" | "9e-16"^^xsd:double   | "Pyruvate:ferredoxin oxidoreductase core domain II" |
| "PF10371" | "2.8e-23"^^xsd:double | "Domain of unknown function"                        |
| "PF01558" | "6.3e-34"^^xsd:double | "Pyruvate ferredoxin/flavodoxin oxidoreductase"     |
| "PF12838" | "1.5e-09"^^xsd:double | "4Fe-4S dicluster domain"                           |
....