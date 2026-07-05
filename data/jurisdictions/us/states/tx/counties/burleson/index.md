---
type: Jurisdiction
title: "Burleson County, TX"
classification: county
fips: "48051"
state: "TX"
demographics:
  population: 18857
  population_under_18: 4138
  population_18_64: 10549
  population_65_plus: 4170
  median_household_income: 70000
  poverty_rate: 12.69
  homeownership_rate: 81.72
  unemployment_rate: 4.96
  median_home_value: 191000
  gini_index: 0.4459
  vacancy_rate: 17.53
  race_white: 13131
  race_black: 2002
  race_asian: 180
  race_native: 128
  hispanic: 4276
  bachelors_plus: 4203
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/17"
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

# Burleson County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18857 |
| Under 18 | 4138 |
| 18–64 | 10549 |
| 65+ | 4170 |
| Median household income | 70000 |
| Poverty rate | 12.69 |
| Homeownership rate | 81.72 |
| Unemployment rate | 4.96 |
| Median home value | 191000 |
| Gini index | 0.4459 |
| Vacancy rate | 17.53 |
| White | 13131 |
| Black | 2002 |
| Asian | 180 |
| Native | 128 |
| Hispanic/Latino | 4276 |
| Bachelor's or higher | 4203 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 17](/us/states/tx/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
