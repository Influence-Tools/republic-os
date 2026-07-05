---
type: Jurisdiction
title: "Pettis County, MO"
classification: county
fips: "29159"
state: "MO"
demographics:
  population: 43397
  population_under_18: 10887
  population_18_64: 24994
  population_65_plus: 7516
  median_household_income: 60430
  poverty_rate: 15.6
  homeownership_rate: 69.14
  unemployment_rate: 3.85
  median_home_value: 166300
  gini_index: 0.4272
  vacancy_rate: 8.98
  race_white: 36541
  race_black: 1073
  race_asian: 299
  race_native: 200
  hispanic: 4299
  bachelors_plus: 7413
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/52"
    rel: in-district
    area_weight: 0.7011
  - to: "us/states/mo/districts/house/57"
    rel: in-district
    area_weight: 0.2989
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Pettis County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43397 |
| Under 18 | 10887 |
| 18–64 | 24994 |
| 65+ | 7516 |
| Median household income | 60430 |
| Poverty rate | 15.6 |
| Homeownership rate | 69.14 |
| Unemployment rate | 3.85 |
| Median home value | 166300 |
| Gini index | 0.4272 |
| Vacancy rate | 8.98 |
| White | 36541 |
| Black | 1073 |
| Asian | 299 |
| Native | 200 |
| Hispanic/Latino | 4299 |
| Bachelor's or higher | 7413 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 52](/us/states/mo/districts/house/52.md) — 70% (state house)
- [MO House District 57](/us/states/mo/districts/house/57.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
