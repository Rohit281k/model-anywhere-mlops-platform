# lakeFS usage

Use lakeFS for Git-like data lake versioning.

```bash
lakectl repo create lakefs://model-anywhere s3://your-bucket/model-anywhere
lakectl branch create lakefs://model-anywhere/experiment-v1 --source lakefs://model-anywhere/main
lakectl fs upload lakefs://model-anywhere/experiment-v1/raw/dataset.csv -s data/raw/dataset.csv
lakectl commit lakefs://model-anywhere/experiment-v1 -m "add dataset"
lakectl merge lakefs://model-anywhere/experiment-v1 lakefs://model-anywhere/main
```
