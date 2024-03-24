#!/usr/bin/env bash
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

main() {
  $(tmux bind-key -T prefix C-p run -b "/usr/bin/env python3 $CURRENT_DIR/scripts/platform.py || /usr/bin/env python $CURRENT_DIR/scripts/platform.py")
}
main

