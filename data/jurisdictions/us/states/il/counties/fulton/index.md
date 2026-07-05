---
type: Jurisdiction
title: "Fulton County, IL"
classification: county
fips: "17057"
state: "IL"
demographics:
  population: 33020
  population_under_18: 6451
  population_18_64: 19480
  population_65_plus: 7089
  median_household_income: 60599
  poverty_rate: 13.16
  homeownership_rate: 76.59
  unemployment_rate: 6.69
  median_home_value: 107200
  gini_index: 0.4316
  vacancy_rate: 12.95
  race_white: 30518
  race_black: 966
  race_asian: 100
  race_native: 126
  hispanic: 830
  bachelors_plus: 5910
districts:
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.5727
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.4273
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.9582
  - to: "us/states/il/districts/house/93"
    rel: in-district
    area_weight: 0.0418
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Fulton County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33020 |
| Under 18 | 6451 |
| 18–64 | 19480 |
| 65+ | 7089 |
| Median household income | 60599 |
| Poverty rate | 13.16 |
| Homeownership rate | 76.59 |
| Unemployment rate | 6.69 |
| Median home value | 107200 |
| Gini index | 0.4316 |
| Vacancy rate | 12.95 |
| White | 30518 |
| Black | 966 |
| Asian | 100 |
| Native | 126 |
| Hispanic/Latino | 830 |
| Bachelor's or higher | 5910 |

## Districts

- [IL-17](/us/states/il/districts/17.md) — 57% (congressional)
- [IL-15](/us/states/il/districts/15.md) — 43% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 100% (state senate)
- [IL House District 94](/us/states/il/districts/house/94.md) — 96% (state house)
- [IL House District 93](/us/states/il/districts/house/93.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
