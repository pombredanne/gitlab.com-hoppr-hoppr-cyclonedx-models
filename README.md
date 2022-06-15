# hoppr-cyclonedx-models

## Purpose
This script serves to pull current and past versions from the [CycloneDX SBOM Standard](https://github.com/CycloneDX) that operates under the SBOM guidelines.  It then utilizes a [datamodel code generator](https://github.com/CycloneDX) that creates pydantic models from the file received. This encourages efficient adherence to the standards set forth by SBOM adoption.

## Usage 
### Install `datamodel-code-generator`:
-----------------------------------------
`pip install datamodel-code-generator`

For further reference see the [documentation](https://koxudaxi.github.io/datamodel-code-generator/).

### Create your model:
-----------------------------------------
`./model-gen.sh x.y` 

Where x and y refer to the applicable major and minor revisons respectively.

* Example Usage: `./model-gen.sh 1.4`

To see an all current releases visit [CycloneDX Specification Releases](https://github.com/CycloneDX/specification/releases)