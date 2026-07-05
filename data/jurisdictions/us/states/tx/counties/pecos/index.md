---
type: Jurisdiction
title: "Pecos County, TX"
classification: county
fips: "48371"
state: "TX"
demographics:
  population: 14896
  population_under_18: 3565
  population_18_64: 9288
  population_65_plus: 2043
  median_household_income: 72750
  poverty_rate: 21.57
  homeownership_rate: 71.95
  unemployment_rate: 2.55
  median_home_value: 165700
  gini_index: 0.4872
  vacancy_rate: 11.18
  race_white: 7482
  race_black: 678
  race_asian: 386
  race_native: 63
  hispanic: 10627
  bachelors_plus: 2061
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/53"
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

# Pecos County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14896 |
| Under 18 | 3565 |
| 18–64 | 9288 |
| 65+ | 2043 |
| Median household income | 72750 |
| Poverty rate | 21.57 |
| Homeownership rate | 71.95 |
| Unemployment rate | 2.55 |
| Median home value | 165700 |
| Gini index | 0.4872 |
| Vacancy rate | 11.18 |
| White | 7482 |
| Black | 678 |
| Asian | 386 |
| Native | 63 |
| Hispanic/Latino | 10627 |
| Bachelor's or higher | 2061 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 29](/us/states/tx/districts/senate/29.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
