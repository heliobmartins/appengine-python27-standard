"""Main API definition."""
import endpoints

import settings

api_definition = endpoints.api(name='Caas', version='v1',
                               description='CancerAid as a Service API',
                               allowed_client_ids=[settings.ALLOWED_CLIENT_ID,
                                                   endpoints.API_EXPLORER_CLIENT_ID],
                               auth_level=endpoints.AUTH_LEVEL.OPTIONAL)
