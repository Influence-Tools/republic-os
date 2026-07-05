---
type: Jurisdiction
title: "Wilbarger County, TX"
classification: county
fips: "48487"
state: "TX"
demographics:
  population: 12616
  population_under_18: 2708
  population_18_64: 7409
  population_65_plus: 2499
  median_household_income: 54102
  poverty_rate: 17.46
  homeownership_rate: 67.18
  unemployment_rate: 9.29
  median_home_value: 89400
  gini_index: 0.4155
  vacancy_rate: 18.25
  race_white: 7892
  race_black: 740
  race_asian: 389
  race_native: 31
  hispanic: 3816
  bachelors_plus: 1944
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Wilbarger County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12616 |
| Under 18 | 2708 |
| 18–64 | 7409 |
| 65+ | 2499 |
| Median household income | 54102 |
| Poverty rate | 17.46 |
| Homeownership rate | 67.18 |
| Unemployment rate | 9.29 |
| Median home value | 89400 |
| Gini index | 0.4155 |
| Vacancy rate | 18.25 |
| White | 7892 |
| Black | 740 |
| Asian | 389 |
| Native | 31 |
| Hispanic/Latino | 3816 |
| Bachelor's or higher | 1944 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
