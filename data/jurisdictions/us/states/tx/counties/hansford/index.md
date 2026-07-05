---
type: Jurisdiction
title: "Hansford County, TX"
classification: county
fips: "48195"
state: "TX"
demographics:
  population: 5119
  population_under_18: 1454
  population_18_64: 2943
  population_65_plus: 722
  median_household_income: 69441
  poverty_rate: 8.58
  homeownership_rate: 81.16
  unemployment_rate: 6.2
  median_home_value: 124800
  gini_index: 0.461
  vacancy_rate: 18.33
  race_white: 3321
  race_black: 7
  race_asian: 15
  race_native: 57
  hispanic: 2572
  bachelors_plus: 1490
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/87"
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

# Hansford County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5119 |
| Under 18 | 1454 |
| 18–64 | 2943 |
| 65+ | 722 |
| Median household income | 69441 |
| Poverty rate | 8.58 |
| Homeownership rate | 81.16 |
| Unemployment rate | 6.2 |
| Median home value | 124800 |
| Gini index | 0.461 |
| Vacancy rate | 18.33 |
| White | 3321 |
| Black | 7 |
| Asian | 15 |
| Native | 57 |
| Hispanic/Latino | 2572 |
| Bachelor's or higher | 1490 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
