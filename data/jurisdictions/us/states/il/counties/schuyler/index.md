---
type: Jurisdiction
title: "Schuyler County, IL"
classification: county
fips: "17169"
state: "IL"
demographics:
  population: 6787
  population_under_18: 1153
  population_18_64: 3890
  population_65_plus: 1744
  median_household_income: 65948
  poverty_rate: 20.77
  homeownership_rate: 79.44
  unemployment_rate: 4.95
  median_home_value: 109700
  gini_index: 0.4274
  vacancy_rate: 17.3
  race_white: 6222
  race_black: 254
  race_asian: 44
  race_native: 0
  hispanic: 182
  bachelors_plus: 1362
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.5477
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 0.4523
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.5477
  - to: "us/states/il/districts/house/99"
    rel: in-district
    area_weight: 0.4523
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Schuyler County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6787 |
| Under 18 | 1153 |
| 18–64 | 3890 |
| 65+ | 1744 |
| Median household income | 65948 |
| Poverty rate | 20.77 |
| Homeownership rate | 79.44 |
| Unemployment rate | 4.95 |
| Median home value | 109700 |
| Gini index | 0.4274 |
| Vacancy rate | 17.3 |
| White | 6222 |
| Black | 254 |
| Asian | 44 |
| Native | 0 |
| Hispanic/Latino | 182 |
| Bachelor's or higher | 1362 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 55% (state senate)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 45% (state senate)
- [IL House District 94](/us/states/il/districts/house/94.md) — 55% (state house)
- [IL House District 99](/us/states/il/districts/house/99.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
