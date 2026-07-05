---
type: Jurisdiction
title: "Choctaw County, AL"
classification: county
fips: "01023"
state: "AL"
demographics:
  population: 12380
  population_under_18: 2443
  population_18_64: 6921
  population_65_plus: 3016
  median_household_income: 47813
  poverty_rate: 16.49
  homeownership_rate: 82.38
  unemployment_rate: 5.03
  median_home_value: 123400
  gini_index: 0.4555
  vacancy_rate: 27.01
  race_white: 7025
  race_black: 4649
  race_asian: 3
  race_native: 22
  hispanic: 144
  bachelors_plus: 1900
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/65"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Choctaw County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12380 |
| Under 18 | 2443 |
| 18–64 | 6921 |
| 65+ | 3016 |
| Median household income | 47813 |
| Poverty rate | 16.49 |
| Homeownership rate | 82.38 |
| Unemployment rate | 5.03 |
| Median home value | 123400 |
| Gini index | 0.4555 |
| Vacancy rate | 27.01 |
| White | 7025 |
| Black | 4649 |
| Asian | 3 |
| Native | 22 |
| Hispanic/Latino | 144 |
| Bachelor's or higher | 1900 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 24](/us/states/al/districts/senate/24.md) — 100% (state senate)
- [AL House District 65](/us/states/al/districts/house/65.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
