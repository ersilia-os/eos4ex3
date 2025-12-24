# MolE molecular representation through redundancy reduced embeddings

MolE representations (Molecular representation through redundancy reduced Embeddings) are task-independent, learned molecular embeddings generated through a self-supervised deep learning approach. They are designed to encode chemically meaningful information about molecules without needing labeled training data.

This model was incorporated on 2025-06-23.Last packaged on 2025-12-16.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4ex3`
- **Slug:** `mole-representations`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1000`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representation of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_000 | float |  | Dimension 0 of the Molecular representation through redundancy reduced Embeddings |
| dim_001 | float |  | Dimension 1 of the Molecular representation through redundancy reduced Embeddings |
| dim_002 | float |  | Dimension 2 of the Molecular representation through redundancy reduced Embeddings |
| dim_003 | float |  | Dimension 3 of the Molecular representation through redundancy reduced Embeddings |
| dim_004 | float |  | Dimension 4 of the Molecular representation through redundancy reduced Embeddings |
| dim_005 | float |  | Dimension 5 of the Molecular representation through redundancy reduced Embeddings |
| dim_006 | float |  | Dimension 6 of the Molecular representation through redundancy reduced Embeddings |
| dim_007 | float |  | Dimension 7 of the Molecular representation through redundancy reduced Embeddings |
| dim_008 | float |  | Dimension 8 of the Molecular representation through redundancy reduced Embeddings |
| dim_009 | float |  | Dimension 9 of the Molecular representation through redundancy reduced Embeddings |

_10 of 1000 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4ex3](https://hub.docker.com/r/ersiliaos/eos4ex3)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4ex3.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4ex3.zip)

### Resource Consumption
- **Model Size (Mb):** `768`
- **Environment Size (Mb):** `5792`
- **Image Size (Mb):** `8073.69`

**Computational Performance (seconds):**
- 10 inputs: `32.87`
- 100 inputs: `23.18`
- 10000 inputs: `311.9`

### References
- **Source Code**: [https://github.com/rolayoalarcon/MolE/tree/main](https://github.com/rolayoalarcon/MolE/tree/main)
- **Publication**: [https://www.nature.com/articles/s41467-025-58804-4](https://www.nature.com/articles/s41467-025-58804-4)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4ex3
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4ex3
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
