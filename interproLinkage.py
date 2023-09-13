# InterProScan version 5.63-95.0

from json import load, dump, dumps
from pyld import jsonld
from argparse import ArgumentError, RawTextHelpFormatter, ArgumentParser
from genericpath import isfile
from rdflib import Graph

output_format_dict = {
    "ttl": "turtle",
    "json-ld": "jsonld",
    "jsonld": "jsonld",
    "rdf": "pretty-xml",
    "xml": "xml",
    "nt": "nt",
    "n3": "n3",
    "trig": "trig",
    "turtle": "turtle",
}


# Define context for interpro JSON data
json_context = load(open("./jsonld_context.json", "r"))


def main(input_file_path: str, output_file_path: str):
    output_file_extension = output_file_path.split(".")[-1]
    if output_file_extension not in output_format_dict.keys():
        parser.print_help()
        raise ArgumentError(
            outut_arg, args.output + " output file extension not supported."
        )
    output_format = output_format_dict[output_file_extension]

    # Read JSON data
    with open(input_file_path, "r") as input_file:
        json_data = load(input_file)
        # Convert JSON to JSON-LD
        jsonld_data = jsonld.expand(json_data, {"expandContext": json_context})[0]

    if output_format == "jsonld":
        # Save the JSON-LD data
        with open(output_file_path, "w") as output_file:
            dump(jsonld_data, output_file, indent=4)
    else:
        # Convert JSON-LD to other formats
        graph_parser = Graph()
        graph_parser.parse(data=dumps(jsonld_data), format="json-ld")
        with open(output_file_path, "w") as output_file:
            graph_parser.serialize(
                destination=output_file_path, format=output_format, indent=1
            )


if __name__ == "__main__":
    parser = ArgumentParser(
        description="""
                            Format 	 Keyword 	                 Notes 
                            JSON-LD  	 json-ld 	                 JSON Linked Data lightweight Linked Data format 
                            Turtle 	         turtle, ttl or turtle2 	 turtle2 is just turtle with more spacing & linebreaks mnot supported now
                            RDF/XML 	 xml or pretty-xml      	 pretty xml. 
                            Notation-3 	 n3 	                         N3 is a superset of Turtle that also caters for rules and a few other things                   
                            Trig             trig 	                         turtle-like format for RDF triples + context (RDF quads) and thus multiple graphs 
                            """,
        formatter_class=RawTextHelpFormatter,
    )
    input_arg = parser.add_argument(
        "-i",
        "--input",
        help="input file format being json output from interproscan.",
        type=str
    )

    outut_arg = parser.add_argument(
        "-o",
        "--output",
        help="output file with jsonld, ttl, rdf, xml, nt, ntll, n3, trig, trix or nquads file extension.",
        type=str
    )

    args = parser.parse_args()

    if not isfile(args.input):
        raise ArgumentError(input_arg, args.input + " input does not exist.")

    main(args.input, args.output)
