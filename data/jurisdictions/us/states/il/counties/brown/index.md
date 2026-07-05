---
type: Jurisdiction
title: "Brown County, IL"
classification: county
fips: "17009"
state: "IL"
demographics:
  population: 6322
  population_under_18: 1062
  population_18_64: 4231
  population_65_plus: 1029
  median_household_income: 67917
  poverty_rate: 9.25
  homeownership_rate: 71.78
  unemployment_rate: 3.06
  median_home_value: 150300
  gini_index: 0.4106
  vacancy_rate: 12.06
  race_white: 4711
  race_black: 1132
  race_asian: 3
  race_native: 11
  hispanic: 424
  bachelors_plus: 738
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/99"
    rel: in-district
    area_weight: 0.6986
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.3014
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Brown County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6322 |
| Under 18 | 1062 |
| 18–64 | 4231 |
| 65+ | 1029 |
| Median household income | 67917 |
| Poverty rate | 9.25 |
| Homeownership rate | 71.78 |
| Unemployment rate | 3.06 |
| Median home value | 150300 |
| Gini index | 0.4106 |
| Vacancy rate | 12.06 |
| White | 4711 |
| Black | 1132 |
| Asian | 3 |
| Native | 11 |
| Hispanic/Latino | 424 |
| Bachelor's or higher | 738 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 100% (state senate)
- [IL House District 99](/us/states/il/districts/house/99.md) — 70% (state house)
- [IL House District 100](/us/states/il/districts/house/100.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
