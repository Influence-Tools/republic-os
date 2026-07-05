---
type: Jurisdiction
title: "Floyd County, TX"
classification: county
fips: "48153"
state: "TX"
demographics:
  population: 5216
  population_under_18: 1326
  population_18_64: 2895
  population_65_plus: 995
  median_household_income: 58462
  poverty_rate: 17.94
  homeownership_rate: 73.26
  unemployment_rate: 6.04
  median_home_value: 89600
  gini_index: 0.5066
  vacancy_rate: 24.69
  race_white: 3260
  race_black: 126
  race_asian: 10
  race_native: 35
  hispanic: 3030
  bachelors_plus: 662
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/83"
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

# Floyd County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5216 |
| Under 18 | 1326 |
| 18–64 | 2895 |
| 65+ | 995 |
| Median household income | 58462 |
| Poverty rate | 17.94 |
| Homeownership rate | 73.26 |
| Unemployment rate | 6.04 |
| Median home value | 89600 |
| Gini index | 0.5066 |
| Vacancy rate | 24.69 |
| White | 3260 |
| Black | 126 |
| Asian | 10 |
| Native | 35 |
| Hispanic/Latino | 3030 |
| Bachelor's or higher | 662 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
