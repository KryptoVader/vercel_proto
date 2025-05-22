# File: api/marks.py
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

# Student marks data
STUDENT_MARKS = {
    "X7exvlqRk": 0, "mN6JI": 46, "HRF5IzPPXf": 72, "jzwAnR": 56, "L": 14,
    "Ek": 54, "5S6X": 0, "2TX": 25, "yBycJF": 86, "6N1bwt": 72,
    "XmwiU7g": 94, "FFcfxk": 70, "x": 63, "IK": 36, "t4JhSm": 37,
    "ZqmxA3lJ7N": 78, "cq0MRdeCP": 97, "kW": 36, "4Qs": 39, "Ev0rgP": 81,
    "Kx": 61, "CLmpaJZe31": 60, "W": 10, "QMLcI5": 97, "n9iDvZGD": 56,
    "aKsBiLVLit": 79, "2rR1M3bMtp": 68, "zJE0xkF": 86, "oD": 86, "wq3moMNJYo": 83,
    "UCkST": 56, "JjTja5tb": 33, "vDSkhI4VLR": 9, "l4oiy": 7, "hCOO8OnHT": 12,
    "sW1KK": 41, "UYco": 45, "T4SQxktwF": 80, "M": 69, "pLl2z1lD": 98,
    "x31xAb": 77, "OTbUq": 79, "IgkYB": 45, "tTKaXz": 32, "zHjd": 50,
    "aM": 38, "d": 63, "iTRSD85DI": 31, "b": 17, "Ku8i7iQ": 68,
    "k": 12, "RRneXBMBY": 32, "EM": 49, "MqC": 5, "B": 66,
    "FsjgaN4": 72, "fe3GCSI4": 45, "oGg3RDIJFM": 29, "hPpnX4": 0, "rvJiOY5": 89,
    "6KSMLYq9D": 21, "m0Vo": 97, "BiCj2R33w": 31, "KmX": 54, "glm9z": 16,
    "gE1XGqclqb": 1, "Oq": 67, "H4RNXQwg": 35, "CRSfxYLJC": 82, "S6V4S": 73,
    "aFiteMXH": 89, "pFj": 10, "qMhEih": 62, "Rvej": 53, "vSU2q3R": 29,
    "6f22": 78, "GM": 14, "bSKnyYPp": 11, "MU0bmoRr": 97, "gW7hE": 0,
    "ldD": 63, "yWeeKTU5": 68, "XeZKuHfRD": 71, "561": 70, "MzRTVv": 13,
    "Nd8OQEX": 66, "0G": 37, "VVIAyk0lY": 31, "kK3T": 85, "1oxixIARG": 49,
    "spoo3": 12, "OMcL": 15, "40I": 28, "mnXmyOM": 13, "5F": 37,
    "a": 24, "Znp": 67, "FqoQI": 88, "g": 56, "sckaG3": 74
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and query parameters
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        # Set CORS headers
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Get the names from the query parameters
        names = query_params.get('name', [])
        
        # Look up marks for each name, maintaining order
        marks = []
        for name in names:
            mark = STUDENT_MARKS.get(name, None)
            marks.append(mark)
        
        # Create response
        response = {"marks": marks}
        
        # Send JSON response
        self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        # Handle preflight requests for CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

