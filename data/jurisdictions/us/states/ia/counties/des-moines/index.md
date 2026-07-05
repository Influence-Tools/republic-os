---
type: Jurisdiction
title: "Des Moines County, IA"
classification: county
fips: "19057"
state: "IA"
demographics:
  population: 38487
  population_under_18: 8560
  population_18_64: 21747
  population_65_plus: 8180
  median_household_income: 62928
  poverty_rate: 12.84
  homeownership_rate: 74.65
  unemployment_rate: 3.11
  median_home_value: 136500
  gini_index: 0.4383
  vacancy_rate: 8.64
  race_white: 32890
  race_black: 1830
  race_asian: 464
  race_native: 126
  hispanic: 1415
  bachelors_plus: 8472
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/48"
    rel: in-district
    area_weight: 0.7334
  - to: "us/states/ia/districts/senate/50"
    rel: in-district
    area_weight: 0.2665
  - to: "us/states/ia/districts/house/95"
    rel: in-district
    area_weight: 0.7334
  - to: "us/states/ia/districts/house/99"
    rel: in-district
    area_weight: 0.2665
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Des Moines County, IA

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38487 |
| Under 18 | 8560 |
| 18–64 | 21747 |
| 65+ | 8180 |
| Median household income | 62928 |
| Poverty rate | 12.84 |
| Homeownership rate | 74.65 |
| Unemployment rate | 3.11 |
| Median home value | 136500 |
| Gini index | 0.4383 |
| Vacancy rate | 8.64 |
| White | 32890 |
| Black | 1830 |
| Asian | 464 |
| Native | 126 |
| Hispanic/Latino | 1415 |
| Bachelor's or higher | 8472 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 48](/us/states/ia/districts/senate/48.md) — 73% (state senate)
- [IA Senate District 50](/us/states/ia/districts/senate/50.md) — 27% (state senate)
- [IA House District 95](/us/states/ia/districts/house/95.md) — 73% (state house)
- [IA House District 99](/us/states/ia/districts/house/99.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
