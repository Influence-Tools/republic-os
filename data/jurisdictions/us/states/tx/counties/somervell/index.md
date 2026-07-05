---
type: Jurisdiction
title: "Somervell County, TX"
classification: county
fips: "48425"
state: "TX"
demographics:
  population: 9691
  population_under_18: 2082
  population_18_64: 5663
  population_65_plus: 1946
  median_household_income: 79825
  poverty_rate: 7.51
  homeownership_rate: 80.04
  unemployment_rate: 3.17
  median_home_value: 289500
  gini_index: 0.4042
  vacancy_rate: 7.57
  race_white: 8066
  race_black: 126
  race_asian: 0
  race_native: 41
  hispanic: 1759
  bachelors_plus: 2484
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/58"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Somervell County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9691 |
| Under 18 | 2082 |
| 18–64 | 5663 |
| 65+ | 1946 |
| Median household income | 79825 |
| Poverty rate | 7.51 |
| Homeownership rate | 80.04 |
| Unemployment rate | 3.17 |
| Median home value | 289500 |
| Gini index | 0.4042 |
| Vacancy rate | 7.57 |
| White | 8066 |
| Black | 126 |
| Asian | 0 |
| Native | 41 |
| Hispanic/Latino | 1759 |
| Bachelor's or higher | 2484 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 58](/us/states/tx/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
