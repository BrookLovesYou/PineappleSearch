# Pineapple Search

## About:

This project was created to address the need for a straightforward, customizable search engine. Frustrated by existing solutions that were either too complex or lacking true customization, I set out to build something simple yet functional. The result is PineappleSearch, designed to allow users to define their own search index and experience fast, efficient searches within their own environment.

## Features

- **User-defined search index**: All search index results are defined by the user in the results.yaml file.
- **Search suggestions**: Suggestions appear as the user types.
- **Simplicity**: No frills, no automation, just enough search engine for a homelab.

## Building:

To build this project, follow these steps,

Clone the repository

    git clone https://github.com/BrookLovesYou/PineappleSearch.git

Navigate to the project directory

    cd PineappleSearch

Build the container

    docker build -t pineapplesearch .

## Running:

To run the project locally using docker run, ensure you've completed the build steps first, then run:

    docker run -p 5000:5000 --name pineapplesearch -v ./data:/app/data pineapplesearch


To run PineappleSearch locally using docker compose, ensure you've completed the build steps and are in the cloned PineappleSearch repo, then run:

    docker compose up -d

## Modifying the search index:

To modify the search index, edit the results.yaml file in the data/ directory. Follow the format of the example entries. Be sure to restart the container after making any changes.

    docker restart pineapplesearch

## Contributing:

Contributions are welcome! Please feel free to submit a Pull Request. This is a hobby project I intend to give some love over the weekends; I may not be very attentive Monday - Friday.

## License:

This project is licensed under the Apache License 2.0 - see the LICENSE.md file for details.
