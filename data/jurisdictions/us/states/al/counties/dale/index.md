---
type: Jurisdiction
title: "Dale County, AL"
classification: county
fips: "01045"
state: "AL"
demographics:
  population: 49599
  population_under_18: 11571
  population_18_64: 29059
  population_65_plus: 8969
  median_household_income: 54963
  poverty_rate: 18.72
  homeownership_rate: 61.89
  unemployment_rate: 6.6
  median_home_value: 143500
  gini_index: 0.4728
  vacancy_rate: 14.11
  race_white: 33551
  race_black: 10103
  race_asian: 611
  race_native: 247
  hispanic: 3533
  bachelors_plus: 9161
districts:
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/senate/31"
    rel: in-district
    area_weight: 0.5888
  - to: "us/states/al/districts/senate/29"
    rel: in-district
    area_weight: 0.4109
  - to: "us/states/al/districts/house/93"
    rel: in-district
    area_weight: 0.5949
  - to: "us/states/al/districts/house/89"
    rel: in-district
    area_weight: 0.4044
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Dale County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49599 |
| Under 18 | 11571 |
| 18–64 | 29059 |
| 65+ | 8969 |
| Median household income | 54963 |
| Poverty rate | 18.72 |
| Homeownership rate | 61.89 |
| Unemployment rate | 6.6 |
| Median home value | 143500 |
| Gini index | 0.4728 |
| Vacancy rate | 14.11 |
| White | 33551 |
| Black | 10103 |
| Asian | 611 |
| Native | 247 |
| Hispanic/Latino | 3533 |
| Bachelor's or higher | 9161 |

## Districts

- [AL-01](/us/states/al/districts/01.md) — 100% (congressional)
- [AL Senate District 31](/us/states/al/districts/senate/31.md) — 59% (state senate)
- [AL Senate District 29](/us/states/al/districts/senate/29.md) — 41% (state senate)
- [AL House District 93](/us/states/al/districts/house/93.md) — 59% (state house)
- [AL House District 89](/us/states/al/districts/house/89.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
