---
type: Jurisdiction
title: "Fisher County, TX"
classification: county
fips: "48151"
state: "TX"
demographics:
  population: 3655
  population_under_18: 829
  population_18_64: 2065
  population_65_plus: 761
  median_household_income: 65533
  poverty_rate: 13.72
  homeownership_rate: 80.43
  unemployment_rate: 4.66
  median_home_value: 78600
  gini_index: 0.3904
  vacancy_rate: 22.42
  race_white: 2762
  race_black: 126
  race_asian: 7
  race_native: 9
  hispanic: 1023
  bachelors_plus: 590
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Fisher County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3655 |
| Under 18 | 829 |
| 18–64 | 2065 |
| 65+ | 761 |
| Median household income | 65533 |
| Poverty rate | 13.72 |
| Homeownership rate | 80.43 |
| Unemployment rate | 4.66 |
| Median home value | 78600 |
| Gini index | 0.3904 |
| Vacancy rate | 22.42 |
| White | 2762 |
| Black | 126 |
| Asian | 7 |
| Native | 9 |
| Hispanic/Latino | 1023 |
| Bachelor's or higher | 590 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
