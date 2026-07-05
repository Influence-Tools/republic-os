---
type: Jurisdiction
title: "Colbert County, AL"
classification: county
fips: "01033"
state: "AL"
demographics:
  population: 58022
  population_under_18: 12368
  population_18_64: 33801
  population_65_plus: 11853
  median_household_income: 60628
  poverty_rate: 17.36
  homeownership_rate: 71.29
  unemployment_rate: 3.14
  median_home_value: 171000
  gini_index: 0.4541
  vacancy_rate: 13.33
  race_white: 44866
  race_black: 8991
  race_asian: 280
  race_native: 120
  hispanic: 2049
  bachelors_plus: 12243
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/al/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/18"
    rel: in-district
    area_weight: 0.7019
  - to: "us/states/al/districts/house/7"
    rel: in-district
    area_weight: 0.22
  - to: "us/states/al/districts/house/3"
    rel: in-district
    area_weight: 0.078
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Colbert County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58022 |
| Under 18 | 12368 |
| 18–64 | 33801 |
| 65+ | 11853 |
| Median household income | 60628 |
| Poverty rate | 17.36 |
| Homeownership rate | 71.29 |
| Unemployment rate | 3.14 |
| Median home value | 171000 |
| Gini index | 0.4541 |
| Vacancy rate | 13.33 |
| White | 44866 |
| Black | 8991 |
| Asian | 280 |
| Native | 120 |
| Hispanic/Latino | 2049 |
| Bachelor's or higher | 12243 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 6](/us/states/al/districts/senate/6.md) — 100% (state senate)
- [AL House District 18](/us/states/al/districts/house/18.md) — 70% (state house)
- [AL House District 7](/us/states/al/districts/house/7.md) — 22% (state house)
- [AL House District 3](/us/states/al/districts/house/3.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
