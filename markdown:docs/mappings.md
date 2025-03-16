# Mappings in Workflow System

## Overview

Mappings are a crucial component of the workflow system that transform data from one format to another. They act as translators between different data structures, making it easier to work with data from various sources.

## Mapping Structure

A mapping consists of:
- **type**: Always "mapping"
- **title**: A human-readable title for the mapping
- **name**: A unique identifier used to reference the mapping
- **description**: A brief explanation of what the mapping does
- **outputs**: Key-value pairs defining how data should be transformed

## Centralized Mappings

Mappings are centrally defined in the `_mappings.yml` file, which allows them to be reused across different workflows. This approach promotes consistency and reduces duplication.

## Using Mappings in Workflows

To use a mapping in a workflow:

1. Add a task of type "mapping"
2. Set the name to match the mapping defined in `_mappings.yml`
3. Provide the required inputs as specified in the mapping definition
4. The outputs will be automatically generated based on the mapping definition

Example:
```yaml
- type: "mapping"
  name: "sportradar-nba-team-mapping"
  description: "Transform the SportRadar NBA team data"
  condition: "$.get('team-profile') is not None"
  inputs:
    team_profile: "$.get('team-profile')"
```

## NBA Team Mapping

The `sportradar-nba-team-mapping` is designed to transform NBA team data from the SportRadar API. It extracts various team details including:

- Basic identifiers (id, sr_id, reference)
- Team name information (name, alias, market, full_name)
- Organizational structure (conference, division, league)
- Venue information
- Historical data (founded, championships, titles, playoff appearances)
- Management information (owner, GM, president)
- Team personnel (coaches, players)
- Other team details (G-League affiliate, retired numbers, sponsor, team colors)

### Input Structure

The mapping expects a `team_profile` input with the following structure:
```json
{
  "alias": "LAL",
  "championship_seasons": "1949, 1950, 1952, 1953, 1954, 1972, 1980, 1982, 1985, 1987, 1988, 2000, 2001, 2002, 2009, 2010, 2020",
  "championships_won": 17,
  "coaches": [...],
  "conference": {...},
  "conference_titles": 19,
  "division": {...},
  "division_titles": 33,
  "founded": 1947,
  "general_manager": "Rob Pelinka",
  "gleague_affiliate": "South Bay Lakers",
  "id": "583ecae2-fb46-11e1-82cb-f4ce4684ea4c",
  "league": {...},
  "market": "Los Angeles",
  "name": "Lakers",
  "owner": "Buss Family Trusts",
  "players": [...],
  "playoff_appearances": 64,
  "president": "Jeanie Buss",
  "reference": "1610612747",
  "retired_numbers": "8, 13, 16, 21, 22, 24, 25, 32, 33, 34, 42, 44, 52, 99",
  "sponsor": "Bibigo",
  "sr_id": "sr:team:3427",
  "team_colors": [...],
  "venue": {...}
}
```

### Key Differences Between Mappings

It's important to note the differences between the various SportRadar mappings:

1. **sportradar-nba-mapping**: Used for NBA game events
2. **sportradar-soccer-mapping**: Used for soccer game events
3. **sportradar-nba-team-mapping**: Used specifically for NBA team data

Each mapping expects different input structures and produces different outputs based on the specific data format provided by the SportRadar API for that sport and entity type.

## Best Practices

1. Always use the correct mapping name that matches the data structure you're working with
2. Ensure the input parameter name matches what the mapping expects
3. Reference mappings from the central `_mappings.yml` file rather than defining them inline
4. Check the mapping definition to understand what outputs will be available after the mapping is applied 