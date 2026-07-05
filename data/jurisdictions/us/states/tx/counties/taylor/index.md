---
type: Jurisdiction
title: "Taylor County, TX"
classification: county
fips: "48441"
state: "TX"
demographics:
  population: 145863
  population_under_18: 35666
  population_18_64: 88385
  population_65_plus: 21812
  median_household_income: 67139
  poverty_rate: 14.67
  homeownership_rate: 60.54
  unemployment_rate: 2.59
  median_home_value: 198600
  gini_index: 0.4491
  vacancy_rate: 11.68
  race_white: 98072
  race_black: 11843
  race_asian: 3304
  race_native: 534
  hispanic: 36641
  bachelors_plus: 35760
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/71"
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

# Taylor County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 145863 |
| Under 18 | 35666 |
| 18–64 | 88385 |
| 65+ | 21812 |
| Median household income | 67139 |
| Poverty rate | 14.67 |
| Homeownership rate | 60.54 |
| Unemployment rate | 2.59 |
| Median home value | 198600 |
| Gini index | 0.4491 |
| Vacancy rate | 11.68 |
| White | 98072 |
| Black | 11843 |
| Asian | 3304 |
| Native | 534 |
| Hispanic/Latino | 36641 |
| Bachelor's or higher | 35760 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 71](/us/states/tx/districts/house/71.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
