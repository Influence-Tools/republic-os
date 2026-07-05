---
type: Jurisdiction
title: "Clinton County, PA"
classification: county
fips: "42035"
state: "PA"
demographics:
  population: 37798
  population_under_18: 7620
  population_18_64: 22613
  population_65_plus: 7565
  median_household_income: 60816
  poverty_rate: 14.81
  homeownership_rate: 72.3
  unemployment_rate: 5.64
  median_home_value: 175900
  gini_index: 0.4319
  vacancy_rate: 17.15
  race_white: 35538
  race_black: 391
  race_asian: 224
  race_native: 19
  hispanic: 719
  bachelors_plus: 7390
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/76"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Clinton County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37798 |
| Under 18 | 7620 |
| 18–64 | 22613 |
| 65+ | 7565 |
| Median household income | 60816 |
| Poverty rate | 14.81 |
| Homeownership rate | 72.3 |
| Unemployment rate | 5.64 |
| Median home value | 175900 |
| Gini index | 0.4319 |
| Vacancy rate | 17.15 |
| White | 35538 |
| Black | 391 |
| Asian | 224 |
| Native | 19 |
| Hispanic/Latino | 719 |
| Bachelor's or higher | 7390 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 25](/us/states/pa/districts/senate/25.md) — 100% (state senate)
- [PA House District 76](/us/states/pa/districts/house/76.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
