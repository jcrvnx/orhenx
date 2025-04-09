#!/usr/bin/env bash

# === Configuration ===
# Directory where the hackingtool is installed and managed by Git
install_dir="/usr/share/hackingtool"

# === Color Codes ===
RED='\e[1;31m'
GREEN='\e[1;32m'
YELLOW='\e[1;33m'
BLUE='\e[1;34m'
NC='\e[0m' # No Color - Important for resetting

# === Helper Functions ===
# Consistent logging format
log_info() { echo -e "${BLUE}[*]${NC} $1"; }
log_success() { echo -e "${GREEN}[+]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
# Log errors to stderr
log_error() { echo -e "${RED}[-]${NC} $1" >&2; }

# Function to exit the script with an error message
die() {
    log_error "$1"
    exit 1
}

echo -e "${YELLOW}" # Start banner in Yellow
echo "   ____  ____  __  _________   ___  __ "
echo "  / __ \/ __ \/ / / / ____/ | / / |/ / "
echo " / / / / /_/ / /_/ / __/ /  |/ /|   /  "
echo "/ /_/ / _, _/ __  / /___/ /|  //   |   "
echo "\____/_/ |_/_/ /_/_____/_/ |_//_/|_|   "
echo -e "${NC}" # Reset color after banner
                                      


# === Pre-flight Checks ===
log_info "Verifying root privileges..."
if [[ $EUID -ne 0 ]]; then
   die "This script must be executed as root."
fi
log_success "Root check passed."

log_info "Checking internet connectivity..."
# Use curl --head for a lighter check, timeout after 10s, follow redirects (-L), silent (-s)
if ! curl -s --head -m 10 -L https://github.com > /dev/null; then
    die "Internet connection check failed. Cannot reach github.com."
fi
log_success "Internet connection verified."

# === Update Process ===
log_info "Navigating to tool directory: ${install_dir}"
if ! cd "${install_dir}"; then
    die "Failed to change directory to '${install_dir}'. Is the tool installed correctly?"
fi
log_success "Current directory: $(pwd)"

# Mark directory as safe for Git (often needed when root runs git on user-owned repo)
log_info "Ensuring Git trusts this directory..."
# Use --global because root is running it; avoids potential ownership issues.
# Check return code, but maybe just warn instead of dying if this fails.
if ! git config --global --add safe.directory "${install_dir}"; then
    log_warning "Could not mark directory as safe. Git operations *might* fail if ownership is mismatched."
    # Continue, as 'git pull' might still work depending on exact setup.
fi

log_info "Attempting to update the tool via Git..."
# No 'sudo' needed here since we already verified root privileges ($EUID -ne 0)
if ! git pull; then
    die "Git pull failed. Check network, permissions, or resolve merge conflicts manually in '${install_dir}'."
fi
log_success "Repository updated successfully."

# Check if the installation script exists and is executable
install_script="install.sh"
log_info "Looking for installation script: ${install_script}"
if [[ ! -f "${install_script}" ]]; then
    die "Installation script '${install_script}' not found in '${install_dir}'."
fi

# Ensure install.sh is executable (harmless if already set)
chmod +x "${install_script}"

log_info "Executing installation/update script: ${install_script}"
# No 'sudo' needed here either
if ! bash "${install_script}"; then
    die "Execution of '${install_script}' failed. Check output above for details."
fi
log_success "Installation script completed."

echo # Blank line for separation
log_success "Hackingtool update process finished successfully."
echo

exit 0