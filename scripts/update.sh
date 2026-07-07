#!/bin/bash

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root (use sudo)"
  exit 1
fi

set -e

# Set install directory
INSTALL_DIR="/opt/openhubble-agent"

# Get the latest release tag from GitHub
LATEST_VERSION=$(curl -s "https://api.github.com/repos/OpenHubble/agent/releases/latest" | jq -r '.tag_name')

if [ -z "$LATEST_VERSION" ] || [ "$LATEST_VERSION" == "null" ]; then
  echo "Failed to get latest version."
  exit 1
fi

TARBALL_URL="https://api.github.com/repos/OpenHubble/agent/tarball/$LATEST_VERSION"

echo "Updating OpenHubble Agent to version $LATEST_VERSION..."

# Change directory to source directory
cd "$INSTALL_DIR" || {
  echo "Source directory not found."
  exit 1
}

# Backup existing installation (optional, in case you need to roll back)
echo "Backing up current installation..."
tar -czf "/tmp/openhubble-agent-backup-$LATEST_VERSION.tar.gz" "$INSTALL_DIR"

# Remove existing files
echo "Removing old files..."
rm -rf "$INSTALL_DIR"/*

# Download and extract the latest version
curl -L "$TARBALL_URL" -o /tmp/openhubble-agent.tar.gz
tar -xzf /tmp/openhubble-agent.tar.gz --strip-components=1 -C "$INSTALL_DIR"

# Recreate the virtual environment
echo "Recreating virtual environment..."
python3 -m venv "$INSTALL_DIR/.venv"

# Install Python dependencies
echo "Installing Python dependencies..."
"$INSTALL_DIR/.venv/bin/python3" -m pip install --no-cache-dir -r "$INSTALL_DIR/requirements.txt"

# Make the Agent executable
chmod +x "$INSTALL_DIR/cli/wrapper.sh"

# Create symbolic link
ln -sf "$INSTALL_DIR/cli/wrapper.sh" /usr/local/bin/openhubble-agent

# Reload the Daemon
echo "Reloading services..."
systemctl daemon-reload

# Restart the service
echo "Restarting the service..."
systemctl restart openhubble-agent.service || {
  echo "Failed to restart the service."
  exit 1
}

echo "OpenHubble Agent has been updated to version $LATEST_VERSION successfully."
