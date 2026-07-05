---
type: Jurisdiction
title: "Comal County, TX"
classification: county
fips: "48091"
state: "TX"
demographics:
  population: 183826
  population_under_18: 40643
  population_18_64: 108797
  population_65_plus: 34386
  median_household_income: 101889
  poverty_rate: 6.48
  homeownership_rate: 76.61
  unemployment_rate: 3.94
  median_home_value: 427200
  gini_index: 0.4499
  vacancy_rate: 8.47
  race_white: 130763
  race_black: 4872
  race_asian: 2947
  race_native: 825
  hispanic: 52232
  bachelors_plus: 75605
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.9502
  - to: "us/states/tx/districts/35"
    rel: in-district
    area_weight: 0.0487
  - to: "us/states/tx/districts/senate/25"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/73"
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

# Comal County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 183826 |
| Under 18 | 40643 |
| 18–64 | 108797 |
| 65+ | 34386 |
| Median household income | 101889 |
| Poverty rate | 6.48 |
| Homeownership rate | 76.61 |
| Unemployment rate | 3.94 |
| Median home value | 427200 |
| Gini index | 0.4499 |
| Vacancy rate | 8.47 |
| White | 130763 |
| Black | 4872 |
| Asian | 2947 |
| Native | 825 |
| Hispanic/Latino | 52232 |
| Bachelor's or higher | 75605 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 95% (congressional)
- [TX-35](/us/states/tx/districts/35.md) — 5% (congressional)
- [TX Senate District 25](/us/states/tx/districts/senate/25.md) — 100% (state senate)
- [TX House District 73](/us/states/tx/districts/house/73.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
