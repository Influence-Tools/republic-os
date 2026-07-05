---
type: Jurisdiction
title: "Ventura County, CA"
classification: county
fips: "06111"
state: "CA"
demographics:
  population: 837469
  population_under_18: 182707
  population_18_64: 508969
  population_65_plus: 145793
  median_household_income: 109797
  poverty_rate: 9.34
  homeownership_rate: 64.57
  unemployment_rate: 5.73
  median_home_value: 822700
  gini_index: 0.4506
  vacancy_rate: 5.24
  race_white: 435268
  race_black: 15401
  race_asian: 60589
  race_native: 14035
  hispanic: 371359
  bachelors_plus: 290023
districts:
  - to: "us/states/ca/districts/26"
    rel: in-district
    area_weight: 0.7693
  - to: "us/states/ca/districts/24"
    rel: in-district
    area_weight: 0.0729
  - to: "us/states/ca/districts/senate/21"
    rel: in-district
    area_weight: 0.7571
  - to: "us/states/ca/districts/senate/27"
    rel: in-district
    area_weight: 0.0848
  - to: "us/states/ca/districts/house/38"
    rel: in-district
    area_weight: 0.6914
  - to: "us/states/ca/districts/house/42"
    rel: in-district
    area_weight: 0.1489
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Ventura County, CA

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 837469 |
| Under 18 | 182707 |
| 18–64 | 508969 |
| 65+ | 145793 |
| Median household income | 109797 |
| Poverty rate | 9.34 |
| Homeownership rate | 64.57 |
| Unemployment rate | 5.73 |
| Median home value | 822700 |
| Gini index | 0.4506 |
| Vacancy rate | 5.24 |
| White | 435268 |
| Black | 15401 |
| Asian | 60589 |
| Native | 14035 |
| Hispanic/Latino | 371359 |
| Bachelor's or higher | 290023 |

## Districts

- [CA-26](/us/states/ca/districts/26.md) — 77% (congressional)
- [CA-24](/us/states/ca/districts/24.md) — 7% (congressional)
- [CA Senate District 21](/us/states/ca/districts/senate/21.md) — 76% (state senate)
- [CA Senate District 27](/us/states/ca/districts/senate/27.md) — 8% (state senate)
- [CA House District 38](/us/states/ca/districts/house/38.md) — 69% (state house)
- [CA House District 42](/us/states/ca/districts/house/42.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
