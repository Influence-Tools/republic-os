---
type: Jurisdiction
title: "Pike County, AL"
classification: county
fips: "01109"
state: "AL"
demographics:
  population: 32987
  population_under_18: 8643
  population_18_64: 12491
  population_65_plus: 11853
  median_household_income: 48677
  poverty_rate: 23.31
  homeownership_rate: 61.33
  unemployment_rate: 3.66
  median_home_value: 157600
  gini_index: 0.4938
  vacancy_rate: 23.12
  race_white: 18356
  race_black: 12275
  race_asian: 622
  race_native: 104
  hispanic: 902
  bachelors_plus: 7595
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/31"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/house/89"
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

# Pike County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32987 |
| Under 18 | 8643 |
| 18–64 | 12491 |
| 65+ | 11853 |
| Median household income | 48677 |
| Poverty rate | 23.31 |
| Homeownership rate | 61.33 |
| Unemployment rate | 3.66 |
| Median home value | 157600 |
| Gini index | 0.4938 |
| Vacancy rate | 23.12 |
| White | 18356 |
| Black | 12275 |
| Asian | 622 |
| Native | 104 |
| Hispanic/Latino | 902 |
| Bachelor's or higher | 7595 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 31](/us/states/al/districts/senate/31.md) — 100% (state senate)
- [AL House District 89](/us/states/al/districts/house/89.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
