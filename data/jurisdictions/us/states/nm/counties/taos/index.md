---
type: Jurisdiction
title: "Taos County, NM"
classification: county
fips: "35055"
state: "NM"
demographics:
  population: 34543
  population_under_18: 5400
  population_18_64: 18604
  population_65_plus: 10539
  median_household_income: 58950
  poverty_rate: 15.46
  homeownership_rate: 77.61
  unemployment_rate: 7.61
  median_home_value: 382800
  gini_index: 0.512
  vacancy_rate: 26.83
  race_white: 19242
  race_black: 122
  race_asian: 259
  race_native: 2410
  hispanic: 17478
  bachelors_plus: 14901
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/6"
    rel: in-district
    area_weight: 0.8054
  - to: "us/states/nm/districts/senate/8"
    rel: in-district
    area_weight: 0.1946
  - to: "us/states/nm/districts/house/42"
    rel: in-district
    area_weight: 0.6684
  - to: "us/states/nm/districts/house/41"
    rel: in-district
    area_weight: 0.3267
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Taos County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34543 |
| Under 18 | 5400 |
| 18–64 | 18604 |
| 65+ | 10539 |
| Median household income | 58950 |
| Poverty rate | 15.46 |
| Homeownership rate | 77.61 |
| Unemployment rate | 7.61 |
| Median home value | 382800 |
| Gini index | 0.512 |
| Vacancy rate | 26.83 |
| White | 19242 |
| Black | 122 |
| Asian | 259 |
| Native | 2410 |
| Hispanic/Latino | 17478 |
| Bachelor's or higher | 14901 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 6](/us/states/nm/districts/senate/6.md) — 81% (state senate)
- [NM Senate District 8](/us/states/nm/districts/senate/8.md) — 19% (state senate)
- [NM House District 42](/us/states/nm/districts/house/42.md) — 67% (state house)
- [NM House District 41](/us/states/nm/districts/house/41.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
