---
type: Jurisdiction
title: "Washington County, AL"
classification: county
fips: "01129"
state: "AL"
demographics:
  population: 15143
  population_under_18: 3300
  population_18_64: 4318
  population_65_plus: 7525
  median_household_income: 61042
  poverty_rate: 17.11
  homeownership_rate: 85.8
  unemployment_rate: 4.86
  median_home_value: 159700
  gini_index: 0.4791
  vacancy_rate: 23.52
  race_white: 9973
  race_black: 3643
  race_asian: 27
  race_native: 1011
  hispanic: 159
  bachelors_plus: 2662
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/al/districts/senate/22"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/65"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Washington County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15143 |
| Under 18 | 3300 |
| 18–64 | 4318 |
| 65+ | 7525 |
| Median household income | 61042 |
| Poverty rate | 17.11 |
| Homeownership rate | 85.8 |
| Unemployment rate | 4.86 |
| Median home value | 159700 |
| Gini index | 0.4791 |
| Vacancy rate | 23.52 |
| White | 9973 |
| Black | 3643 |
| Asian | 27 |
| Native | 1011 |
| Hispanic/Latino | 159 |
| Bachelor's or higher | 2662 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 22](/us/states/al/districts/senate/22.md) — 100% (state senate)
- [AL House District 65](/us/states/al/districts/house/65.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
