Pineapple Search

About:

This project was made to address a very simple issue I had. I wanted a stupid simple search engine with user defined results; but non existed as far as I could tell.

Features

    - User defined search index: The user defines all search index results in the results.yaml file.
    - Search suggestions: As the user types, search suggestions will appear.
    - Simplicity: No frills, no automation, just enough search engine for a homelab.

Building:

To build this project, follow these steps,

Clone the repository

    git clone https://github.com/BrookLovesYou/PineappleSearch.git

Navigate to the project directory

    cd PineappleSearch

Build the container

    docker build -t pineapplesearch .

Running:

To run the project locally,

Ensure you've completed the build steps above.

Start the server

    docker run -p 5000:5000 pineapplesearch

Contributing:

Contributions are welcome! Please feel free to submit a Pull Request.

License:

This project is licensed under the Apache License 2.0 - see the LICENSE.md file for details.
