---
type: Jurisdiction
title: "Hamilton County, TX"
classification: county
fips: "48193"
state: "TX"
demographics:
  population: 8406
  population_under_18: 1889
  population_18_64: 4422
  population_65_plus: 2095
  median_household_income: 58219
  poverty_rate: 16.47
  homeownership_rate: 78.69
  unemployment_rate: 5.43
  median_home_value: 147700
  gini_index: 0.4945
  vacancy_rate: 28.64
  race_white: 7082
  race_black: 165
  race_asian: 3
  race_native: 15
  hispanic: 1196
  bachelors_plus: 2055
districts:
  - to: "us/states/tx/districts/31"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/59"
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

# Hamilton County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8406 |
| Under 18 | 1889 |
| 18–64 | 4422 |
| 65+ | 2095 |
| Median household income | 58219 |
| Poverty rate | 16.47 |
| Homeownership rate | 78.69 |
| Unemployment rate | 5.43 |
| Median home value | 147700 |
| Gini index | 0.4945 |
| Vacancy rate | 28.64 |
| White | 7082 |
| Black | 165 |
| Asian | 3 |
| Native | 15 |
| Hispanic/Latino | 1196 |
| Bachelor's or higher | 2055 |

## Districts

- [TX-31](/us/states/tx/districts/31.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 59](/us/states/tx/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
