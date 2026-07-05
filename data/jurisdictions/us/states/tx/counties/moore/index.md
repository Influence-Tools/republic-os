---
type: Jurisdiction
title: "Moore County, TX"
classification: county
fips: "48341"
state: "TX"
demographics:
  population: 21373
  population_under_18: 6638
  population_18_64: 12341
  population_65_plus: 2394
  median_household_income: 61762
  poverty_rate: 18.28
  homeownership_rate: 62.46
  unemployment_rate: 3.3
  median_home_value: 152600
  gini_index: 0.434
  vacancy_rate: 13.53
  race_white: 10415
  race_black: 1053
  race_asian: 449
  race_native: 589
  hispanic: 13048
  bachelors_plus: 1915
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/87"
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

# Moore County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21373 |
| Under 18 | 6638 |
| 18–64 | 12341 |
| 65+ | 2394 |
| Median household income | 61762 |
| Poverty rate | 18.28 |
| Homeownership rate | 62.46 |
| Unemployment rate | 3.3 |
| Median home value | 152600 |
| Gini index | 0.434 |
| Vacancy rate | 13.53 |
| White | 10415 |
| Black | 1053 |
| Asian | 449 |
| Native | 589 |
| Hispanic/Latino | 13048 |
| Bachelor's or higher | 1915 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 87](/us/states/tx/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
