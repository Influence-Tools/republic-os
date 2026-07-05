---
type: Jurisdiction
title: "Montague County, TX"
classification: county
fips: "48337"
state: "TX"
demographics:
  population: 21046
  population_under_18: 4788
  population_18_64: 11665
  population_65_plus: 4593
  median_household_income: 64545
  poverty_rate: 14.19
  homeownership_rate: 79.88
  unemployment_rate: 7.06
  median_home_value: 206400
  gini_index: 0.444
  vacancy_rate: 17.49
  race_white: 18901
  race_black: 14
  race_asian: 35
  race_native: 105
  hispanic: 2586
  bachelors_plus: 3650
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/68"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Montague County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21046 |
| Under 18 | 4788 |
| 18–64 | 11665 |
| 65+ | 4593 |
| Median household income | 64545 |
| Poverty rate | 14.19 |
| Homeownership rate | 79.88 |
| Unemployment rate | 7.06 |
| Median home value | 206400 |
| Gini index | 0.444 |
| Vacancy rate | 17.49 |
| White | 18901 |
| Black | 14 |
| Asian | 35 |
| Native | 105 |
| Hispanic/Latino | 2586 |
| Bachelor's or higher | 3650 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
