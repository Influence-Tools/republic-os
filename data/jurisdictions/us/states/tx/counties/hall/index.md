---
type: Jurisdiction
title: "Hall County, TX"
classification: county
fips: "48191"
state: "TX"
demographics:
  population: 2820
  population_under_18: 599
  population_18_64: 1533
  population_65_plus: 688
  median_household_income: 48459
  poverty_rate: 16.25
  homeownership_rate: 73.57
  unemployment_rate: 9.04
  median_home_value: 86100
  gini_index: 0.4607
  vacancy_rate: 32.78
  race_white: 1698
  race_black: 116
  race_asian: 12
  race_native: 31
  hispanic: 1002
  bachelors_plus: 560
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/88"
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

# Hall County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2820 |
| Under 18 | 599 |
| 18–64 | 1533 |
| 65+ | 688 |
| Median household income | 48459 |
| Poverty rate | 16.25 |
| Homeownership rate | 73.57 |
| Unemployment rate | 9.04 |
| Median home value | 86100 |
| Gini index | 0.4607 |
| Vacancy rate | 32.78 |
| White | 1698 |
| Black | 116 |
| Asian | 12 |
| Native | 31 |
| Hispanic/Latino | 1002 |
| Bachelor's or higher | 560 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
