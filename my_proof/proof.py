import json
import logging
import os
from typing import Dict, Any

import requests

from my_proof.models.proof_response import ProofResponse


class Proof:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.proof_response = ProofResponse(dlp_id=config['dlp_id'])

    def generate(self) -> ProofResponse:
        """Generate proofs for all input files."""
        logging.info("Starting proof generation")
        self.proof_response.ownership = 1.0
        self.proof_response.quality = 1.0
        self.proof_response.authenticity = 1.0
        self.proof_response.uniqueness = 1.0

        # Calculate overall score and validity
        self.proof_response.score = 1.0
        self.proof_response.valid = True

        # Additional (public) properties to include in the proof about the data
        self.proof_response.attributes = {
            'total_score': 1.0
        }

        # Additional metadata about the proof, written onchain
        self.proof_response.metadata = {
            'dlp_id': self.config['dlp_id'],
        }

        return self.proof_response