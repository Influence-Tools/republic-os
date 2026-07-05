---
type: Jurisdiction
title: "San Patricio County, TX"
classification: county
fips: "48409"
state: "TX"
demographics:
  population: 70181
  population_under_18: 18036
  population_18_64: 41308
  population_65_plus: 10837
  median_household_income: 69704
  poverty_rate: 14.78
  homeownership_rate: 66.87
  unemployment_rate: 4.47
  median_home_value: 192400
  gini_index: 0.4494
  vacancy_rate: 16.76
  race_white: 39142
  race_black: 1050
  race_asian: 754
  race_native: 872
  hispanic: 39623
  bachelors_plus: 10737
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.9909
  - to: "us/states/tx/districts/senate/27"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/tx/districts/house/43"
    rel: in-district
    area_weight: 0.9968
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# San Patricio County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 70181 |
| Under 18 | 18036 |
| 18–64 | 41308 |
| 65+ | 10837 |
| Median household income | 69704 |
| Poverty rate | 14.78 |
| Homeownership rate | 66.87 |
| Unemployment rate | 4.47 |
| Median home value | 192400 |
| Gini index | 0.4494 |
| Vacancy rate | 16.76 |
| White | 39142 |
| Black | 1050 |
| Asian | 754 |
| Native | 872 |
| Hispanic/Latino | 39623 |
| Bachelor's or higher | 10737 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 99% (congressional)
- [TX Senate District 27](/us/states/tx/districts/senate/27.md) — 100% (state senate)
- [TX House District 43](/us/states/tx/districts/house/43.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
