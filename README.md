# Git commit log

```sh
docker build . -t mohammadrony/commit-log
```

Docker application

```sh
docker run --rm --name commit-log mohammadrony/commit-log
```

Custom repository commit

```sh
docker run --rm --name commit-log \
  -e GITHUB_REPOSITORY="dsinnovators/js-essentials" \
  mohammadrony/commit-log
```
