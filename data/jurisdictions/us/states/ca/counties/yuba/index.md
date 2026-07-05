---
type: Jurisdiction
title: "Yuba County, CA"
classification: county
fips: "06115"
state: "CA"
demographics:
  population: 84507
  population_under_18: 22964
  population_18_64: 50483
  population_65_plus: 11060
  median_household_income: 76373
  poverty_rate: 14.18
  homeownership_rate: 63.5
  unemployment_rate: 6.83
  median_home_value: 412300
  gini_index: 0.4454
  vacancy_rate: 6.61
  race_white: 45485
  race_black: 3355
  race_asian: 6730
  race_native: 1509
  hispanic: 26003
  bachelors_plus: 12713
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.6884
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.3116
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/3"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Yuba County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84507 |
| Under 18 | 22964 |
| 18–64 | 50483 |
| 65+ | 11060 |
| Median household income | 76373 |
| Poverty rate | 14.18 |
| Homeownership rate | 63.5 |
| Unemployment rate | 6.83 |
| Median home value | 412300 |
| Gini index | 0.4454 |
| Vacancy rate | 6.61 |
| White | 45485 |
| Black | 3355 |
| Asian | 6730 |
| Native | 1509 |
| Hispanic/Latino | 26003 |
| Bachelor's or higher | 12713 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 69% (congressional)
- [CA-01](/us/states/ca/districts/01.md) — 31% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 3](/us/states/ca/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
