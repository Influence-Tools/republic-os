---
type: Jurisdiction
title: "Dorchester County, MD"
classification: county
fips: "24019"
state: "MD"
demographics:
  population: 32754
  population_under_18: 6865
  population_18_64: 18351
  population_65_plus: 7538
  median_household_income: 61839
  poverty_rate: 17.14
  homeownership_rate: 65.57
  unemployment_rate: 5.71
  median_home_value: 262400
  gini_index: 0.4697
  vacancy_rate: 17.57
  race_white: 20185
  race_black: 8133
  race_asian: 381
  race_native: 0
  hispanic: 1996
  bachelors_plus: 6269
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.6584
  - to: "us/states/md/districts/senate/37"
    rel: in-district
    area_weight: 0.6093
  - to: "us/states/md/districts/house/37b"
    rel: in-district
    area_weight: 0.5127
  - to: "us/states/md/districts/house/37a"
    rel: in-district
    area_weight: 0.0966
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Dorchester County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32754 |
| Under 18 | 6865 |
| 18–64 | 18351 |
| 65+ | 7538 |
| Median household income | 61839 |
| Poverty rate | 17.14 |
| Homeownership rate | 65.57 |
| Unemployment rate | 5.71 |
| Median home value | 262400 |
| Gini index | 0.4697 |
| Vacancy rate | 17.57 |
| White | 20185 |
| Black | 8133 |
| Asian | 381 |
| Native | 0 |
| Hispanic/Latino | 1996 |
| Bachelor's or higher | 6269 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 66% (congressional)
- [MD Senate District 37](/us/states/md/districts/senate/37.md) — 61% (state senate)
- [MD House District 37B](/us/states/md/districts/house/37b.md) — 51% (state house)
- [MD House District 37A](/us/states/md/districts/house/37a.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
