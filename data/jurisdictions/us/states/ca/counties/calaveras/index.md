---
type: Jurisdiction
title: "Calaveras County, CA"
classification: county
fips: "06009"
state: "CA"
demographics:
  population: 46248
  population_under_18: 7833
  population_18_64: 24898
  population_65_plus: 13517
  median_household_income: 78647
  poverty_rate: 13.0
  homeownership_rate: 83.96
  unemployment_rate: 4.52
  median_home_value: 457200
  gini_index: 0.4577
  vacancy_rate: 33.4
  race_white: 36396
  race_black: 457
  race_asian: 1031
  race_native: 776
  hispanic: 6702
  bachelors_plus: 11344
districts:
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/8"
    rel: in-district
    area_weight: 0.8126
  - to: "us/states/ca/districts/house/9"
    rel: in-district
    area_weight: 0.1872
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Calaveras County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46248 |
| Under 18 | 7833 |
| 18–64 | 24898 |
| 65+ | 13517 |
| Median household income | 78647 |
| Poverty rate | 13.0 |
| Homeownership rate | 83.96 |
| Unemployment rate | 4.52 |
| Median home value | 457200 |
| Gini index | 0.4577 |
| Vacancy rate | 33.4 |
| White | 36396 |
| Black | 457 |
| Asian | 1031 |
| Native | 776 |
| Hispanic/Latino | 6702 |
| Bachelor's or higher | 11344 |

## Districts

- [CA-05](/us/states/ca/districts/05.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 8](/us/states/ca/districts/house/8.md) — 81% (state house)
- [CA House District 9](/us/states/ca/districts/house/9.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
