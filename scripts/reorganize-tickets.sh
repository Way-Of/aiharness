#!/bin/bash
# Reorganize tickets into category subdirectories
# Usage: ./reorganize-tickets.sh <project-slug>

set -e

PROJECT_SLUG="${1:?Usage: $0 <project-slug>}"
TICKETS_DIR="thoughts/${PROJECT_SLUG}/shared/tickets"

if [ ! -d "$TICKETS_DIR" ]; then
  echo "Error: $TICKETS_DIR does not exist"
  exit 1
fi

echo "Reorganizing tickets in $TICKETS_DIR..."

# Create category directories
mkdir -p "$TICKETS_DIR"/{frontend,backend,infrastructure,devops,security,architecture,docs,testing,ai-tools,done}

# Move tickets based on category in frontmatter
for ticket in "$TICKETS_DIR"/*.md; do
  [ -f "$ticket" ] || continue
  
  filename=$(basename "$ticket")
  
  # Skip if already in a subdirectory
  if [[ "$ticket" == */*/* ]]; then
    continue
  fi
  
  # Extract category from frontmatter
  category=$(grep -m1 "^category:" "$ticket" | sed 's/category: *"*//' | sed 's/"*$//' | xargs)
  
  if [ -z "$category" ]; then
    echo "  Skipping $filename (no category found)"
    continue
  fi
  
  # Map category to directory
  case "$category" in
    feature|bug|improvement) dir="backend" ;;
    infrastructure) dir="infrastructure" ;;
    compliance) dir="security" ;;
    system) dir="infrastructure" ;;
    *) dir="$category" ;;
  esac
  
  # Create directory if needed
  mkdir -p "$TICKETS_DIR/$dir"
  
  # Move the ticket
  if [ -f "$TICKETS_DIR/$dir/$filename" ]; then
    echo "  Skipping $filename (already exists in $dir/)"
  else
    git mv "$ticket" "$TICKETS_DIR/$dir/$filename"
    echo "  Moved $filename -> $dir/"
  fi
done

echo "Done! Check $TICKETS_DIR for reorganized tickets."
