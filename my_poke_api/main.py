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

POKEMON_DATA = {}
POKEMON_BY_REGION = {}
REGIONS = [
    "kanto",
    "johto",
    "hoenn",
    "sinnoh",
    "unova",
    "kalos",
    "alola",
    "galar",
    "paldea",
]


@app.on_event("startup")
async def startup_event():
    with open(RESOURCES / "pokemon.json", "r") as f:
        POKEMON_DATA.update(json.load(f))

    for region in REGIONS:
        with open(RESOURCES / f"{region}_idx.txt", "r") as f:
            region_idxs = f.read().split(",")

        pokemon_in_region = []
        for idx in region_idxs:
            pokemon_in_region.append(POKEMON_DATA[idx])

        POKEMON_BY_REGION[region] = pokemon_in_region


@app.get("/{region}")
async def get_pokemon_region(region: str):
    return POKEMON_BY_REGION[region.lower()]
