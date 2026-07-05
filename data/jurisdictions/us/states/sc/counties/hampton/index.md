---
type: Jurisdiction
title: "Hampton County, SC"
classification: county
fips: "45049"
state: "SC"
demographics:
  population: 18254
  population_under_18: 3911
  population_18_64: 10754
  population_65_plus: 3589
  median_household_income: 44711
  poverty_rate: 20.69
  homeownership_rate: 73.44
  unemployment_rate: 9.49
  median_home_value: 112000
  gini_index: 0.4541
  vacancy_rate: 16.43
  race_white: 7509
  race_black: 9594
  race_asian: 179
  race_native: 38
  hispanic: 757
  bachelors_plus: 2123
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/sc/districts/senate/45"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/sc/districts/house/122"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Hampton County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18254 |
| Under 18 | 3911 |
| 18–64 | 10754 |
| 65+ | 3589 |
| Median household income | 44711 |
| Poverty rate | 20.69 |
| Homeownership rate | 73.44 |
| Unemployment rate | 9.49 |
| Median home value | 112000 |
| Gini index | 0.4541 |
| Vacancy rate | 16.43 |
| White | 7509 |
| Black | 9594 |
| Asian | 179 |
| Native | 38 |
| Hispanic/Latino | 757 |
| Bachelor's or higher | 2123 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 100% (congressional)
- [SC Senate District 45](/us/states/sc/districts/senate/45.md) — 100% (state senate)
- [SC House District 122](/us/states/sc/districts/house/122.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
