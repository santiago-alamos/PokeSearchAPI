# PokéSearchAPI

PokéSearchAPI is the API of [PokéSearch](http://pokesearch.help/), a web application that allows users to search and filter through a collection of Pokémon by characteristics, traits, types, etc.

## Contributing
We welcome contributions from anyone who wants to help improve the project. One way to contribute is by adding tags to the Pokémon in the [pokemon.json](https://github.com/jalvaradosegura/PokeSearchAPI/blob/main/my_poke_api/resources/pokemon.json) file. These tags can then be used by PokéSearch to filter the Pokémon by characteristics or traits.

To contribute, please follow these steps:

1. Fork the repository to your own account
2. Create a new branch from the main branch for your changes
3. Make your changes and commit them to your branch
4. Create a pull request to merge your changes into the main branch
5. Wait for your pull request to be reviewed and approved by a project maintainer

### Adding tags
To add tags to a Pokémon, simply add them into the `tags` field of the Pokémon inside the `pokemon.json` file. The tags field should be an array of strings that describe the Pokémon's characteristics or traits.

For example, here is an entry for Pikachu with tags:

```json
"25": {
        "id": "25",
        "name": "pikachu",
        "types": ["electric"],
        "super_weak_to": [],
        "weak_to": ["ground"],
        "damaged_normally_by": ["fighting", "grass", "poison", "normal", "rock", "ghost", "dragon", "fairy", "psychic", "dark", "bug", "water", "fire", "ice"],
        "resists": ["flying", "steel", "electric"],
        "super_resists": [],
        "immune_to": [],
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "tags": ["yellow", "rat", "ash"]
    },
```

You can add as many tags as you like to each Pokémon. Please only add tags that are relevant and descriptive of the Pokémon.
