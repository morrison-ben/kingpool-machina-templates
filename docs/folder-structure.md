# Folder Structure Configuration Guide

## Overview
The folder structure in the system is defined through YAML configuration files that specify how documents and content should be organized. This guide explains how to create and customize folder structures for your application.

## Configuration Structure

The folder structure is defined in YAML format with the following main components:

```yaml
workflow:
  name: "populate-folders"
  title: "Setup Folders"
  description: "Setup Folders"
  inputs:
    force-setup: "$.get('force-setup') == 'true'"
  outputs:
    setup-register: "$.get('setup-register')"
    workflow-status: "($.get('setup-register') is True or $.get('force-setup') is True) and 'skipped' or 'executed'"
```

## Folder Definition

The folder structure is defined in the `doc-structure` document. Here's how to define folders:

```json
[
  {
    "title": "Folder Name",
    "isActive": true,
    "icon": "folder",
    "items": [
      {
        "name": "collection-name",
        "title": "Display Title",
        "description": "Description of the collection",
        "category": "Category Name",
        "metadata": {
          "name": ["tag1", "tag2"]
        },
        "sorters": ["_id", -1],
        "view": "list"
      }
    ]
  }
]
```

### Properties Explanation

- **title**: The display name of the folder
- **isActive**: Boolean to control if the folder is active
- **icon**: Icon to display (currently supports "folder")
- **items**: Array of collections within the folder

#### Collection Properties

- **name**: Unique identifier for the collection
- **title**: Display name for the collection
- **description**: Detailed description of the collection's purpose
- **category**: Category grouping for the collection
- **metadata**: 
  - **name**: Array of tags/aliases for the collection
- **sorters**: Array defining sort order [field, direction (-1 for desc, 1 for asc)]
- **view**: Display mode ("list" or "grid")

## Example

Here's a practical example of defining a folder structure:

```yaml
doc-structure: |
  [
    {
      "title": "Catalogue",
      "isActive": true,
      "icon": "folder",
      "items": [
        {
          "name": "schedules",
          "title": "Game Schedule",
          "description": "The schedules synced from the Sportradar API.",
          "category": "Catalogue",
          "metadata": {
            "name": ["nba-game", "nba-games", "schedules", "schedule"]
          },
          "sorters": ["_id", -1],
          "view": "list"
        }
      ]
    }
  ]
```

## Implementation Steps

1. Create or modify a YAML file in your project
2. Define the workflow configuration
3. Specify the folder structure in the `doc-structure` section
4. Each folder can contain multiple items (collections)
5. Deploy the configuration

## Best Practices

1. Use descriptive titles and names
2. Keep metadata tags relevant and specific
3. Choose appropriate view modes based on content type
4. Group related collections under meaningful folder titles
5. Use clear and concise descriptions

## Notes

- The system automatically handles folder creation and updates
- Use `force-setup: true` to override existing configurations
- The setup-register tracks if the folder structure has been initialized 