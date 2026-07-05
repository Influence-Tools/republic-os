---
type: Jurisdiction
title: "Harding County, NM"
classification: county
fips: "35021"
state: "NM"
demographics:
  population: 741
  population_under_18: 188
  population_18_64: 356
  population_65_plus: 197
  median_household_income: 48553
  poverty_rate: 19.43
  homeownership_rate: 76.92
  unemployment_rate: 15.31
  median_home_value: 70000
  gini_index: 0.7267
  vacancy_rate: 42.34
  race_white: 396
  race_black: 13
  race_asian: 0
  race_native: 1
  hispanic: 270
  bachelors_plus: 241
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/8"
    rel: in-district
    area_weight: 0.9596
  - to: "us/states/nm/districts/senate/7"
    rel: in-district
    area_weight: 0.0404
  - to: "us/states/nm/districts/house/67"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Harding County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 741 |
| Under 18 | 188 |
| 18–64 | 356 |
| 65+ | 197 |
| Median household income | 48553 |
| Poverty rate | 19.43 |
| Homeownership rate | 76.92 |
| Unemployment rate | 15.31 |
| Median home value | 70000 |
| Gini index | 0.7267 |
| Vacancy rate | 42.34 |
| White | 396 |
| Black | 13 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 270 |
| Bachelor's or higher | 241 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 8](/us/states/nm/districts/senate/8.md) — 96% (state senate)
- [NM Senate District 7](/us/states/nm/districts/senate/7.md) — 4% (state senate)
- [NM House District 67](/us/states/nm/districts/house/67.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
