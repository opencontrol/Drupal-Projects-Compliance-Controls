# Drupal Plugins Compliance Controls Documentation Sample

Included is a sample `opencontrol.yaml` file that imports the Drupal Plugins Compliance components and generates compliance documentation for a demonstration ATO.

The steps below can be used to import the OpenControl dependencies and serve a GitBook. Ensure that Compliance-Masonry is installed on your local workstation.

Run the following commands from the root of the `examples/opencontrol/test-system` directory.

1. Remove any existing `exports/` and `opencontrols/` directories in your workspace


rm -rf exports/ opencontrols/
compliance-masonry get
compliance-masonry docs gitbook FedRAMP-low
tree

npm install -g gitbook-cli


```sh
rm -rf exports/ opencontrols/
```

2. Retrieve dependencies

```shell
compliance-masonry get
compliance-masonry docs gitbook FedRAMP-low
```

The `compliance-masonry get` command reads the `opencontrol.yaml` file and retrieves all the dependencies, even from other OpenControl repositories!

The `compliance-masonry docs gitbook FedRAMP-low` command generates a document of the components and standards matching the `FedRAMP-Low` certification that is expressed in the `gitbook` format.

At this point, you have generated content for your `SSP` inside of the `exports` directory that has artfully combined data from the all other OpenControl `YAML` files into a `gitbook`!

3. Publish Gitbook content

Our next step is to publish/deploy our `gitbook` content representing our SSP for shared human access. First, install [GitBook](https://github.com/GitbookIO/gitbook-cli#readme):

```shell
npm install -g gitbook-cli
```

To make a PDF version:

```shell
cd exports && gitbook pdf ./ ./compliance.pdf
# creates the PDF at `exports/compliance.pdf`
```

To make a HTML web site version:

```shell
cd exports && gitbook serve
# visit your HTML SSP at http://localhost:4000
```

The steps above are included in the project's `Makefile` so you can reliably run, say:

```shell
make clean pdf
# or
make clean serve
```
