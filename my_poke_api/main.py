import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .settings import ALLOWED_ORIGINS, DOCS_URL, PRODUCTION

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
RESOURCES = BASE_DIR / "my_poke_api" / "resources"

app = FastAPI(docs_url=DOCS_URL)

# CORS
if PRODUCTION:  # pragma: no cover
    origins = ALLOWED_ORIGINS.split(",")
else:
    origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{region}")
async def get_pokemon_region(region: str):
    with open(RESOURCES / "pokemon.json", "r") as f:
        pokemon_data = json.load(f)

    with open(RESOURCES / f"{region.lower()}_idx.txt", "r") as f:
        region_idxs = f.read().split(",")

    pokemon_in_region = []
    for idx in region_idxs:
        pokemon_in_region.append(pokemon_data[idx])

    return pokemon_in_region
