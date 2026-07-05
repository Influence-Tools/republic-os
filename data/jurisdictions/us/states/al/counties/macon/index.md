---
type: Jurisdiction
title: "Macon County, AL"
classification: county
fips: "01087"
state: "AL"
demographics:
  population: 18691
  population_under_18: 2887
  population_18_64: 11837
  population_65_plus: 3967
  median_household_income: 43707
  poverty_rate: 24.32
  homeownership_rate: 61.54
  unemployment_rate: 8.29
  median_home_value: 102000
  gini_index: 0.5006
  vacancy_rate: 25.03
  race_white: 3218
  race_black: 14498
  race_asian: 59
  race_native: 6
  hispanic: 408
  bachelors_plus: 3543
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/al/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/house/82"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Macon County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18691 |
| Under 18 | 2887 |
| 18–64 | 11837 |
| 65+ | 3967 |
| Median household income | 43707 |
| Poverty rate | 24.32 |
| Homeownership rate | 61.54 |
| Unemployment rate | 8.29 |
| Median home value | 102000 |
| Gini index | 0.5006 |
| Vacancy rate | 25.03 |
| White | 3218 |
| Black | 14498 |
| Asian | 59 |
| Native | 6 |
| Hispanic/Latino | 408 |
| Bachelor's or higher | 3543 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 28](/us/states/al/districts/senate/28.md) — 100% (state senate)
- [AL House District 82](/us/states/al/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
