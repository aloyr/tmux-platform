# Platform.sh project list for tmux

[![GitHub](https://img.shields.io/github/license/aloyr/tmux-platform)](https://opensource.org/licenses/MIT)

Show a menu with platform.sh's projects list, and copies the platform.sh project ID to the pasteboard.

This is just a first draft and assumes the user is already authenticated via the CLI.

## Installation
### Requirements
* macOS
* tmux >= 3.0
* python >= 3.0

### With Tmux Plugin Manager
Add the plugin in `.tmux.conf`:
```
set -g @plugin 'aloyr/tmux-platform'
```
Press `prefix + I` to fetch the plugin and source it. Done.

### Manual
Clone the repo somewhere. Add `run-shell` in the end of `.tmux.conf`:

```
run-shell PATH_TO_REPO/tmux-platform.tmux
```
NOTE: this line should be placed after `set-option -g status-right ...`.

Press `prefix + :` and type `source-file ~/.tmux.conf`. Done.

## Usage
Press tmux `prefix + C-p` (for example, `C-b C-p`) and you will see a list of platform.sh projects.

