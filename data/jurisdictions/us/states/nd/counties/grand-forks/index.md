---
type: Jurisdiction
title: "Grand Forks County, ND"
classification: county
fips: "38035"
state: "ND"
demographics:
  population: 72923
  population_under_18: 15443
  population_18_64: 47089
  population_65_plus: 10391
  median_household_income: 68075
  poverty_rate: 13.2
  homeownership_rate: 51.78
  unemployment_rate: 2.33
  median_home_value: 252700
  gini_index: 0.4597
  vacancy_rate: 7.66
  race_white: 60573
  race_black: 2820
  race_asian: 2020
  race_native: 1347
  hispanic: 3919
  bachelors_plus: 22365
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/nd/districts/senate/20"
    rel: in-district
    area_weight: 0.8243
  - to: "us/states/nd/districts/senate/42"
    rel: in-district
    area_weight: 0.0943
  - to: "us/states/nd/districts/senate/18"
    rel: in-district
    area_weight: 0.0496
  - to: "us/states/nd/districts/senate/17"
    rel: in-district
    area_weight: 0.0289
  - to: "us/states/nd/districts/house/20"
    rel: in-district
    area_weight: 0.8243
  - to: "us/states/nd/districts/house/42"
    rel: in-district
    area_weight: 0.0943
  - to: "us/states/nd/districts/house/18"
    rel: in-district
    area_weight: 0.0496
  - to: "us/states/nd/districts/house/17"
    rel: in-district
    area_weight: 0.0289
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Grand Forks County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 72923 |
| Under 18 | 15443 |
| 18–64 | 47089 |
| 65+ | 10391 |
| Median household income | 68075 |
| Poverty rate | 13.2 |
| Homeownership rate | 51.78 |
| Unemployment rate | 2.33 |
| Median home value | 252700 |
| Gini index | 0.4597 |
| Vacancy rate | 7.66 |
| White | 60573 |
| Black | 2820 |
| Asian | 2020 |
| Native | 1347 |
| Hispanic/Latino | 3919 |
| Bachelor's or higher | 22365 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 20](/us/states/nd/districts/senate/20.md) — 82% (state senate)
- [ND Senate District 42](/us/states/nd/districts/senate/42.md) — 9% (state senate)
- [ND Senate District 18](/us/states/nd/districts/senate/18.md) — 5% (state senate)
- [ND Senate District 17](/us/states/nd/districts/senate/17.md) — 3% (state senate)
- [ND House District 20](/us/states/nd/districts/house/20.md) — 82% (state house)
- [ND House District 42](/us/states/nd/districts/house/42.md) — 9% (state house)
- [ND House District 18](/us/states/nd/districts/house/18.md) — 5% (state house)
- [ND House District 17](/us/states/nd/districts/house/17.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
