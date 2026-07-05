---
type: Jurisdiction
title: "San Augustine County, TX"
classification: county
fips: "48405"
state: "TX"
demographics:
  population: 7874
  population_under_18: 1573
  population_18_64: 4190
  population_65_plus: 2111
  median_household_income: 50408
  poverty_rate: 27.14
  homeownership_rate: 75.1
  unemployment_rate: 9.51
  median_home_value: 99900
  gini_index: 0.4742
  vacancy_rate: 38.93
  race_white: 5468
  race_black: 1696
  race_asian: 0
  race_native: 39
  hispanic: 657
  bachelors_plus: 1099
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.9936
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.0057
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/9"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# San Augustine County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7874 |
| Under 18 | 1573 |
| 18–64 | 4190 |
| 65+ | 2111 |
| Median household income | 50408 |
| Poverty rate | 27.14 |
| Homeownership rate | 75.1 |
| Unemployment rate | 9.51 |
| Median home value | 99900 |
| Gini index | 0.4742 |
| Vacancy rate | 38.93 |
| White | 5468 |
| Black | 1696 |
| Asian | 0 |
| Native | 39 |
| Hispanic/Latino | 657 |
| Bachelor's or higher | 1099 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 99% (congressional)
- [TX-17](/us/states/tx/districts/17.md) — 1% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 9](/us/states/tx/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
