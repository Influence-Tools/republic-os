---
type: Jurisdiction
title: "Washington County, TX"
classification: county
fips: "48477"
state: "TX"
demographics:
  population: 36647
  population_under_18: 7757
  population_18_64: 20426
  population_65_plus: 8464
  median_household_income: 77825
  poverty_rate: 13.42
  homeownership_rate: 69.79
  unemployment_rate: 2.98
  median_home_value: 288100
  gini_index: 0.4842
  vacancy_rate: 12.25
  race_white: 24488
  race_black: 5218
  race_asian: 529
  race_native: 258
  hispanic: 6772
  bachelors_plus: 10006
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/12"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Washington County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36647 |
| Under 18 | 7757 |
| 18–64 | 20426 |
| 65+ | 8464 |
| Median household income | 77825 |
| Poverty rate | 13.42 |
| Homeownership rate | 69.79 |
| Unemployment rate | 2.98 |
| Median home value | 288100 |
| Gini index | 0.4842 |
| Vacancy rate | 12.25 |
| White | 24488 |
| Black | 5218 |
| Asian | 529 |
| Native | 258 |
| Hispanic/Latino | 6772 |
| Bachelor's or higher | 10006 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 12](/us/states/tx/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
