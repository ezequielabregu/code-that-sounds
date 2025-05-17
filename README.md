# Creative Coding with Pure Data

This repository contains the source files for the Quarto book "Creative Coding with Pure Data." This book aims to introduce readers to the fundamentals and creative applications of Pure Data for audio synthesis, algorithmic composition, and interactive installations.

## Project Structure

The project is organized as follows:

- **`_quarto.yml`**: The main configuration file for the Quarto book. It defines the book's metadata, chapter order, formatting options, and website settings.
- **`index.qmd`**: The landing page or main introduction of the book.
- **`chapters/`**: This directory contains the individual chapters of the book as Quarto Markdown (`.qmd`) files.

- **`references.bib`**: The bibliography file for managing citations and references used throughout the book.
- **`styles.css`**: Custom CSS file for additional styling beyond the selected Quarto theme.
- **`assets/`**: Directory for storing static assets like images, audio examples, Pure Data patches (`.pd` files), or other supplementary materials.
- **`README.md`**: This file, providing an overview of the project.

## Prerequisites

To build and render this book, you need to have [Quarto CLI](https://quarto.org/docs/get-started/) installed on your system.

## Building the Book

To render the book from the source files, navigate to the project's root directory in your terminal and run:

```bash
quarto render
```

This command will process all the `.qmd` files and generate the book in the output format(s) specified in `_quarto.yml` (typically HTML by default, located in the `_book/` directory).

## Previewing the Book

To preview the book locally with live reloading as you make changes, run:

```bash
quarto preview
```

This will start a local web server, and the book will automatically update in your browser whenever you save changes to the source files.

## Contributing

Contributions to this project are welcome! If you have suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.