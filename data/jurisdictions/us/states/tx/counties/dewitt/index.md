---
type: Jurisdiction
title: "DeWitt County, TX"
classification: county
fips: "48123"
state: "TX"
demographics:
  population: 20016
  population_under_18: 4471
  population_18_64: 11485
  population_65_plus: 4060
  median_household_income: 63730
  poverty_rate: 17.6
  homeownership_rate: 73.92
  unemployment_rate: 3.72
  median_home_value: 170900
  gini_index: 0.4796
  vacancy_rate: 25.08
  race_white: 11786
  race_black: 1214
  race_asian: 133
  race_native: 163
  hispanic: 7143
  bachelors_plus: 3149
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/30"
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

# DeWitt County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20016 |
| Under 18 | 4471 |
| 18–64 | 11485 |
| 65+ | 4060 |
| Median household income | 63730 |
| Poverty rate | 17.6 |
| Homeownership rate | 73.92 |
| Unemployment rate | 3.72 |
| Median home value | 170900 |
| Gini index | 0.4796 |
| Vacancy rate | 25.08 |
| White | 11786 |
| Black | 1214 |
| Asian | 133 |
| Native | 163 |
| Hispanic/Latino | 7143 |
| Bachelor's or higher | 3149 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 30](/us/states/tx/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
