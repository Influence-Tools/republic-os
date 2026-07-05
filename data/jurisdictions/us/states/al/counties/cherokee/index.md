---
type: Jurisdiction
title: "Cherokee County, AL"
classification: county
fips: "01019"
state: "AL"
demographics:
  population: 25443
  population_under_18: 4726
  population_18_64: 14497
  population_65_plus: 6220
  median_household_income: 53863
  poverty_rate: 14.75
  homeownership_rate: 81.08
  unemployment_rate: 3.88
  median_home_value: 179700
  gini_index: 0.4699
  vacancy_rate: 30.68
  race_white: 23091
  race_black: 970
  race_asian: 60
  race_native: 62
  hispanic: 469
  bachelors_plus: 4525
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/al/districts/senate/10"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/house/39"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Cherokee County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25443 |
| Under 18 | 4726 |
| 18–64 | 14497 |
| 65+ | 6220 |
| Median household income | 53863 |
| Poverty rate | 14.75 |
| Homeownership rate | 81.08 |
| Unemployment rate | 3.88 |
| Median home value | 179700 |
| Gini index | 0.4699 |
| Vacancy rate | 30.68 |
| White | 23091 |
| Black | 970 |
| Asian | 60 |
| Native | 62 |
| Hispanic/Latino | 469 |
| Bachelor's or higher | 4525 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 10](/us/states/al/districts/senate/10.md) — 100% (state senate)
- [AL House District 39](/us/states/al/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
