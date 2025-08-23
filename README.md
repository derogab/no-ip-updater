<h1 align="center">NO-IP Updater</h1>
<h3 align="center">A simple script to auto update current IP address to a No-IP domain</h3>
<p align="center">
    <a href="https://hub.docker.com/r/derogab/no-ip-updater">
        <img src="https://img.shields.io/docker/pulls/derogab/no-ip-updater?label=Downloads&logo=docker" alt="Docker Pulls">
    </a>
    <a href="https://github.com/derogab/no-ip-updater/actions/workflows/docker-publish.yml">
        <img src="https://github.com/derogab/no-ip-updater/actions/workflows/docker-publish.yml/badge.svg" alt="Build & Push Docker Image">
    </a>
</p>

### Configs
Copy `.env.template` to `.env`. Then edit `.env` with own configs.

| Variable           | Description                                                                 | Default |
|--------------------|-----------------------------------------------------------------------------|---------|
| `NOIP_USER`        | Your No-IP account username (required)                                      | -       |
| `NOIP_PASSWORD`    | Your No-IP account password (required)                                      | -       |
| `NOIP_HOSTNAME`    | The hostname (domain) you want to update on No-IP (required)                | -       |
| `FREQUENCY_MINUTES`| How often (in minutes) to check and update the IP address                   | 15      |
| `ENABLE_DEBUG`     | Enable debug logging (`1` or `true` to enable, otherwise disables)          | -       |
| `TZ`               | Time zone for the container (optional, e.g., `UTC`, `Europe/Rome`)          | UTC     |

### Start
```
docker-compose up -d
```

### Credits
[no-ip-updater](https://github.com/derogab/no-ip-updater) is made with ♥  by [derogab](https://github.com/derogab) and it's released under the [MIT license](./LICENSE).

### Contributors

<a href="https://github.com/derogab/no-ip-updater/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=derogab/no-ip-updater" />
</a>

### Tip
If you like this project or directly benefit from it, please consider buying me a coffee:  
🔗 `bc1qd0qatgz8h62uvnr74utwncc6j5ckfz2v2g4lef`  
⚡️ `derogab@sats.mobi`  
💶 [Sponsor on GitHub](https://github.com/sponsors/derogab)

### Stargazers over time
[![Stargazers over time](https://starchart.cc/derogab/no-ip-updater.svg?variant=adaptive)](https://starchart.cc/derogab/no-ip-updater)
