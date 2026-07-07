# OpenHubble Agent

Lightweight **monitoring agent** written in **Python** with **FastAPI**, designed to collect system metrics and expose an API for data retrieval and visualization. Includes installation, configuration, update, and uninstallation guides.

Got it! Here's a revised version of the paragraph that starts with "Before everything" and includes the installation context:

## Built-in Command-Line Tool

Before everything else, you should know that this agent includes a built-in command-line tool, `openhubble-agent`, which allows you to manage the agent and interact with its services directly from the terminal. This tool enables you to start, stop, restart, and check the status of the agent, view logs, and perform other management tasks.

For detailed instructions on how to install and use the command-line tool, please refer to the [CLI documentation](https://github.com/OpenHubble/agent/blob/main/docs/cli.md).

## Installing the Agent

To install the **OpenHubble Agent**, follow these steps:

### 1. Download and Run the Installation Script

Use `curl` to fetch the installation script and run it with **root** privileges:

```bash
curl -s https://get.openhubble.com/agent | sudo bash
```

This script will:

- Update your system's packages.
- Install required dependencies (`git`, `python3`, `python3-venv`, and `python3-pip`).
- Clone the **OpenHubble agent** repository.
- Set up the required directories and configurations.
- Create a Python virtual environment and install the necessary Python modules.
- Set up a systemd service for the **OpenHubble agent**.

### 2. Configure the Agent

After the installation, you need to configure the **agent**. Edit the configuration file located at:

```bash
sudo nano /etc/openhubble-agent/.env
```

Update the configuration values according to your system and monitoring requirements. Save and close the file when done.

### 3. Enable the Service

To ensure the **agent** starts automatically after a reboot, enable the service:

```bash
sudo systemctl enable openhubble-agent.service
```

### 4. Restart the Service

After editing the configuration file, restart the service to apply the changes:

```bash
sudo systemctl restart openhubble-agent.service
```

> Also you can restart service using **built-in command-line tool**!
> ```bash
> openhubble-agent restart
> ```

### 5. Verify Installation

To confirm the agent is running, use:

```bash
sudo systemctl status openhubble-agent.service
```

The service status should indicate it is `active (running)`.

---

## Configuring the Firewall (UFW)

After installing the OpenHubble Agent, ensure that your firewall allows incoming traffic on the port the agent is listening to (default is `9703`). If you have changed the port in the configuration file, substitute `9703` with the new port number.

To allow the default port (`9703`), run the following command:

```bash
sudo ufw allow 9703/tcp
```

If you have configured the agent to use a different port (e.g., `12345`), run the following command instead:

```bash
sudo ufw allow 12345/tcp
```

This will allow access to the agent's API. After running the appropriate command, you can check the status of your firewall with:

```bash
sudo ufw status
```

Make sure the port you specified is listed as allowed.

---

## Updating the Agent

The OpenHubble Agent can be updated using the built-in CLI tool. Run the following command with **root** privileges:

```bash
sudo openhubble-agent update
```

This will:

- Pull the latest updates from the repository.
- Update Python dependencies.
- Restart the service.

---

## Uninstalling the Agent

To uninstall the OpenHubble Agent, use the built-in CLI tool:

```bash
sudo openhubble-agent uninstall
```

This will:

- Stop and disable the service.
- Remove the service file, directories, and configuration files.

---

## Attribution

If you modify or redistribute the **OpenHubble Agent**, you must include a reference to **"OpenHubble"** as the original creator of the project. This ensures that our startup is credited for the work and contributions made to the software.

Example attribution:

```bash
This software was modified from the original **OpenHubble Agent** (https://github.com/OpenHubble/agent).
```

---

[OpenHubble](https://openhubble.com) by [Amirhossein Mohammadi](https://amirhossein.info) - 2025