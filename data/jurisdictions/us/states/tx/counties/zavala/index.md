---
type: Jurisdiction
title: "Zavala County, TX"
classification: county
fips: "48507"
state: "TX"
demographics:
  population: 9412
  population_under_18: 2757
  population_18_64: 5178
  population_65_plus: 1477
  median_household_income: 36749
  poverty_rate: 33.92
  homeownership_rate: 69.03
  unemployment_rate: 3.97
  median_home_value: 98800
  gini_index: 0.4393
  vacancy_rate: 17.11
  race_white: 2079
  race_black: 79
  race_asian: 47
  race_native: 9
  hispanic: 8717
  bachelors_plus: 696
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/80"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Zavala County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9412 |
| Under 18 | 2757 |
| 18–64 | 5178 |
| 65+ | 1477 |
| Median household income | 36749 |
| Poverty rate | 33.92 |
| Homeownership rate | 69.03 |
| Unemployment rate | 3.97 |
| Median home value | 98800 |
| Gini index | 0.4393 |
| Vacancy rate | 17.11 |
| White | 2079 |
| Black | 79 |
| Asian | 47 |
| Native | 9 |
| Hispanic/Latino | 8717 |
| Bachelor's or higher | 696 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 80](/us/states/tx/districts/house/80.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
