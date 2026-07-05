---
type: Jurisdiction
title: "Arkansas County, AR"
classification: county
fips: "05001"
state: "AR"
demographics:
  population: 16515
  population_under_18: 3826
  population_18_64: 9365
  population_65_plus: 3324
  median_household_income: 53164
  poverty_rate: 19.02
  homeownership_rate: 64.58
  unemployment_rate: 8.14
  median_home_value: 138100
  gini_index: 0.4509
  vacancy_rate: 22.9
  race_white: 11454
  race_black: 4317
  race_asian: 10
  race_native: 82
  hispanic: 682
  bachelors_plus: 2103
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ar/districts/senate/8"
    rel: in-district
    area_weight: 0.584
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.4159
  - to: "us/states/ar/districts/house/61"
    rel: in-district
    area_weight: 0.6122
  - to: "us/states/ar/districts/house/62"
    rel: in-district
    area_weight: 0.3575
  - to: "us/states/ar/districts/house/65"
    rel: in-district
    area_weight: 0.0303
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Arkansas County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16515 |
| Under 18 | 3826 |
| 18–64 | 9365 |
| 65+ | 3324 |
| Median household income | 53164 |
| Poverty rate | 19.02 |
| Homeownership rate | 64.58 |
| Unemployment rate | 8.14 |
| Median home value | 138100 |
| Gini index | 0.4509 |
| Vacancy rate | 22.9 |
| White | 11454 |
| Black | 4317 |
| Asian | 10 |
| Native | 82 |
| Hispanic/Latino | 682 |
| Bachelor's or higher | 2103 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 8](/us/states/ar/districts/senate/8.md) — 58% (state senate)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 42% (state senate)
- [AR House District 61](/us/states/ar/districts/house/61.md) — 61% (state house)
- [AR House District 62](/us/states/ar/districts/house/62.md) — 36% (state house)
- [AR House District 65](/us/states/ar/districts/house/65.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
