---
type: Jurisdiction
title: "Anderson County, TX"
classification: county
fips: "48001"
state: "TX"
demographics:
  population: 58439
  population_under_18: 11195
  population_18_64: 38379
  population_65_plus: 8865
  median_household_income: 62068
  poverty_rate: 17.36
  homeownership_rate: 72.34
  unemployment_rate: 5.95
  median_home_value: 185300
  gini_index: 0.4611
  vacancy_rate: 14.86
  race_white: 34060
  race_black: 10841
  race_asian: 390
  race_native: 854
  hispanic: 11442
  bachelors_plus: 8408
districts:
  - to: "us/states/tx/districts/06"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/8"
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

# Anderson County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58439 |
| Under 18 | 11195 |
| 18–64 | 38379 |
| 65+ | 8865 |
| Median household income | 62068 |
| Poverty rate | 17.36 |
| Homeownership rate | 72.34 |
| Unemployment rate | 5.95 |
| Median home value | 185300 |
| Gini index | 0.4611 |
| Vacancy rate | 14.86 |
| White | 34060 |
| Black | 10841 |
| Asian | 390 |
| Native | 854 |
| Hispanic/Latino | 11442 |
| Bachelor's or higher | 8408 |

## Districts

- [TX-06](/us/states/tx/districts/06.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 8](/us/states/tx/districts/house/8.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
