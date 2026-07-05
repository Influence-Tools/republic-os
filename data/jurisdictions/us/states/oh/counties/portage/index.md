---
type: Jurisdiction
title: "Portage County, OH"
classification: county
fips: "39133"
state: "OH"
demographics:
  population: 161956
  population_under_18: 29466
  population_18_64: 102788
  population_65_plus: 29702
  median_household_income: 75766
  poverty_rate: 11.68
  homeownership_rate: 70.14
  unemployment_rate: 5.34
  median_home_value: 227000
  gini_index: 0.4472
  vacancy_rate: 8.52
  race_white: 140144
  race_black: 8127
  race_asian: 3536
  race_native: 174
  hispanic: 3717
  bachelors_plus: 49002
districts:
  - to: "us/states/oh/districts/14"
    rel: in-district
    area_weight: 0.9907
  - to: "us/states/oh/districts/13"
    rel: in-district
    area_weight: 0.0091
  - to: "us/states/oh/districts/senate/27"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/house/72"
    rel: in-district
    area_weight: 0.851
  - to: "us/states/oh/districts/house/35"
    rel: in-district
    area_weight: 0.1488
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Portage County, OH

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 161956 |
| Under 18 | 29466 |
| 18–64 | 102788 |
| 65+ | 29702 |
| Median household income | 75766 |
| Poverty rate | 11.68 |
| Homeownership rate | 70.14 |
| Unemployment rate | 5.34 |
| Median home value | 227000 |
| Gini index | 0.4472 |
| Vacancy rate | 8.52 |
| White | 140144 |
| Black | 8127 |
| Asian | 3536 |
| Native | 174 |
| Hispanic/Latino | 3717 |
| Bachelor's or higher | 49002 |

## Districts

- [OH-14](/us/states/oh/districts/14.md) — 99% (congressional)
- [OH-13](/us/states/oh/districts/13.md) — 1% (congressional)
- [OH Senate District 27](/us/states/oh/districts/senate/27.md) — 100% (state senate)
- [OH House District 72](/us/states/oh/districts/house/72.md) — 85% (state house)
- [OH House District 35](/us/states/oh/districts/house/35.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
