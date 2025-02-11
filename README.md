# Git commit log

Run application

```sh
docker run -d --name commit-log \
  mohammadrony/commit-log
```

Run with custom repository

```sh
docker run -d --name commit-log \
  -e GITHUB_REPOSITORY="dsinnovators/js-essentials" \
  mohammadrony/commit-log`
```

Check commit log

```sh
docker logs commit-log
```
