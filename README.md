# petcher - Publication fECTHCER #

petcher is a Python-based tool designed to automate the retrieval of publication titles from DBLP.org and checks their availability on arXiv. It also allows users to search for publications with specific keywords within a defined time range, streamlining access to relevant research.

## Features

- Crawl data from DBLP.
- Scrape paper titles, authors, and publication dates.
- Filter results based on specified keywords and search methods.
- Loof for its availability on arXiv
- Save extracted data in a tab-separated values (TSV) format.

## Installation

### Prerequisites

Make sure you have Python 3.12 installed. 

### Required Packages

You can install the required packages using pip. My project uses the versions specified in requirements.txt. To install the requirements, run:
```bash
pip install -r requirements.txt
```
Feel free to adjust further if needed!

## Usage
To use DBLPExplore, run the following command in your terminal:
| Argument | Description | Required/Optional |
|---|---|---|
| -v, --venue | The acronym of the venue you want to explore. | Required |
| -s, --start | The start year for publication (default: 0). | Optional |
| -e, --end | The end year for publication (default: current year). | Optional |
| -m, --method | The search method to use (default: "all"). Options: "all", "any". | Optional |
| -k, --keywords | Keywords to search for publications. Enter multiple keywords separated by spaces. | Optional |
| -o, --output | Destination file path for saving the results (default: data/publications). | Optional |

*Note: The acronyms for these conferences follow the naming conventions used by DBLP, which may not align with standard abbreviations. The code only supports conferences listed in the `components/venue_map` folder. To add a venue that is not listed, include a venue record in any file within the `components/venue_map` directory.*

### Example
Here’s an example command to extract publications from a conference:
```bash
python main.py -v AAAI SIGIR CSUR -s 2015 -e 2020 -m any -k "neural network" -o "data/pub.jsonl"
```

This command will extract data from the AAAI, SIGIR, and CSUR conferences for the years 2015 to 2020, including publications that contain the phrase "neural network" in the title. The results will be saved to data/pub.jsonl.

For better usability, I have included a Bash script to simplify modifying the command for additional parameters and improve reusability. The script is available as `run.sh`.

To execute the script, run:
```
chmod +x run.sh
./run.sh
```

## Acknowledgments

Thanks to the developers of DBLP for providing a comprehensive database of computer science publications and to arXiv for offering a valuable repository of research papers.

