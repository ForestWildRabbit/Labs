import yaml
from app.core.main import app  # Make sure this imports your FastAPI app correctly

# Get OpenAPI schema (Swagger format)
openapi_schema = app.openapi()

# Save to swagger.yml
with open("swagger.yml", "w") as f:
    yaml.dump(openapi_schema, f, sort_keys=False)