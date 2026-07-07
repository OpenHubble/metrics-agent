#!/bin/bash

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (use sudo)"
  exit 1
fi

# Install dependencies
apt update -y
apt install -y python3 python3-venv python3-pip curl tar jq

# Set directories
INSTALL_DIR="/opt/openhubble-agent" # Install directory
CONFIG_DIR="/etc/openhubble-agent" # Config directory
LOG_DIR="/var/log/openhubble-agent" # Log directory

# Get the latest release tag from GitHub
LATEST_VERSION=$(curl -s "https://api.github.com/repos/OpenHubble/agent/releases/latest" | jq -r '.tag_name')

if [ -z "$LATEST_VERSION" ] || [ "$LATEST_VERSION" == "null" ]; then
  echo "Failed to get latest version."
  exit 1
fi

TARBALL_URL="https://api.github.com/repos/OpenHubble/agent/tarball/$LATEST_VERSION"

echo "Installing OpenHubble Agent version $LATEST_VERSION..."

# Create directories if not exist
mkdir -p "$INSTALL_DIR" # Ensure the install directory exists
mkdir -p "$CONFIG_DIR" # Ensure the config directory exists
mkdir -p "$LOG_DIR" # Ensure the logs directory exists

# Download and extract the latest version
curl -L "$TARBALL_URL" -o /tmp/openhubble-agent.tar.gz
tar -xzf /tmp/openhubble-agent.tar.gz --strip-components=1 -C "$INSTALL_DIR"

# Copy the config file to the config directory
echo "Setting up configurations..."
cp "$INSTALL_DIR/.env.example" "$CONFIG_DIR/.env" || {
  echo "Failed to copy configuration file."
  exit 1
}

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv "$INSTALL_DIR/.venv"

# Install Python dependencies
echo "Installing dependencies..."
"$INSTALL_DIR/.venv/bin/python3" -m pip install --no-cache-dir -r "$INSTALL_DIR/requirements.txt"

# Make Agent executable
chmod +x "$INSTALL_DIR/cli/wrapper.sh"

# Create symbolic link
ln -sf "$INSTALL_DIR/cli/wrapper.sh" /usr/local/bin/openhubble-agent

# Copy the service file for systemctl
echo "Setting up service..."
cp "$INSTALL_DIR/openhubble-agent.service" /etc/systemd/system/ || {
  echo "Failed to copy service file."
  exit 1
}

# Reload Daemon
echo "Reloading services..."
systemctl daemon-reload

echo "OpenHubble Agent ($LATEST_VERSION) has been installed successfully."
