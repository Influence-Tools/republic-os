---
type: Jurisdiction
title: "Steuben County, IN"
classification: county
fips: "18151"
state: "IN"
demographics:
  population: 34726
  population_under_18: 6830
  population_18_64: 20303
  population_65_plus: 7593
  median_household_income: 74911
  poverty_rate: 9.34
  homeownership_rate: 79.47
  unemployment_rate: 7.24
  median_home_value: 216200
  gini_index: 0.4453
  vacancy_rate: 26.71
  race_white: 32205
  race_black: 230
  race_asian: 250
  race_native: 11
  hispanic: 1547
  bachelors_plus: 8384
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/51"
    rel: in-district
    area_weight: 0.6682
  - to: "us/states/in/districts/house/52"
    rel: in-district
    area_weight: 0.3315
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Steuben County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34726 |
| Under 18 | 6830 |
| 18–64 | 20303 |
| 65+ | 7593 |
| Median household income | 74911 |
| Poverty rate | 9.34 |
| Homeownership rate | 79.47 |
| Unemployment rate | 7.24 |
| Median home value | 216200 |
| Gini index | 0.4453 |
| Vacancy rate | 26.71 |
| White | 32205 |
| Black | 230 |
| Asian | 250 |
| Native | 11 |
| Hispanic/Latino | 1547 |
| Bachelor's or higher | 8384 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 13](/us/states/in/districts/senate/13.md) — 100% (state senate)
- [IN House District 51](/us/states/in/districts/house/51.md) — 67% (state house)
- [IN House District 52](/us/states/in/districts/house/52.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
