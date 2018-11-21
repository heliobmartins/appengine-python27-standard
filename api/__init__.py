"""Main module that starts API server."""
import endpoints

from .api_definition import api_definition
from .referral_api import ReferralApi

API = endpoints.api_server([ReferralApi])
