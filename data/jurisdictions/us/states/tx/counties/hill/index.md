---
type: Jurisdiction
title: "Hill County, TX"
classification: county
fips: "48217"
state: "TX"
demographics:
  population: 37328
  population_under_18: 8638
  population_18_64: 21070
  population_65_plus: 7620
  median_household_income: 64591
  poverty_rate: 14.68
  homeownership_rate: 78.21
  unemployment_rate: 4.19
  median_home_value: 179200
  gini_index: 0.4428
  vacancy_rate: 16.23
  race_white: 28005
  race_black: 2093
  race_asian: 285
  race_native: 300
  hispanic: 8635
  bachelors_plus: 6188
districts:
  - to: "us/states/tx/districts/06"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/13"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Hill County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37328 |
| Under 18 | 8638 |
| 18–64 | 21070 |
| 65+ | 7620 |
| Median household income | 64591 |
| Poverty rate | 14.68 |
| Homeownership rate | 78.21 |
| Unemployment rate | 4.19 |
| Median home value | 179200 |
| Gini index | 0.4428 |
| Vacancy rate | 16.23 |
| White | 28005 |
| Black | 2093 |
| Asian | 285 |
| Native | 300 |
| Hispanic/Latino | 8635 |
| Bachelor's or higher | 6188 |

## Districts

- [TX-06](/us/states/tx/districts/06.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 13](/us/states/tx/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
