---
type: Jurisdiction
title: "Edwards County, IL"
classification: county
fips: "17047"
state: "IL"
demographics:
  population: 6075
  population_under_18: 1338
  population_18_64: 3367
  population_65_plus: 1370
  median_household_income: 60519
  poverty_rate: 16.49
  homeownership_rate: 79.33
  unemployment_rate: 5.57
  median_home_value: 100000
  gini_index: 0.4348
  vacancy_rate: 12.45
  race_white: 5787
  race_black: 6
  race_asian: 22
  race_native: 0
  hispanic: 89
  bachelors_plus: 857
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Edwards County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6075 |
| Under 18 | 1338 |
| 18–64 | 3367 |
| 65+ | 1370 |
| Median household income | 60519 |
| Poverty rate | 16.49 |
| Homeownership rate | 79.33 |
| Unemployment rate | 5.57 |
| Median home value | 100000 |
| Gini index | 0.4348 |
| Vacancy rate | 12.45 |
| White | 5787 |
| Black | 6 |
| Asian | 22 |
| Native | 0 |
| Hispanic/Latino | 89 |
| Bachelor's or higher | 857 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 100% (state senate)
- [IL House District 116](/us/states/il/districts/house/116.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
