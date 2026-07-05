---
type: Jurisdiction
title: "Barbour County, AL"
classification: county
fips: "01005"
state: "AL"
demographics:
  population: 24643
  population_under_18: 5112
  population_18_64: 14576
  population_65_plus: 4955
  median_household_income: 46042
  poverty_rate: 21.38
  homeownership_rate: 68.24
  unemployment_rate: 7.79
  median_home_value: 112900
  gini_index: 0.4957
  vacancy_rate: 22.39
  race_white: 10852
  race_black: 11423
  race_asian: 145
  race_native: 39
  hispanic: 1534
  bachelors_plus: 2605
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/al/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/house/84"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Barbour County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24643 |
| Under 18 | 5112 |
| 18–64 | 14576 |
| 65+ | 4955 |
| Median household income | 46042 |
| Poverty rate | 21.38 |
| Homeownership rate | 68.24 |
| Unemployment rate | 7.79 |
| Median home value | 112900 |
| Gini index | 0.4957 |
| Vacancy rate | 22.39 |
| White | 10852 |
| Black | 11423 |
| Asian | 145 |
| Native | 39 |
| Hispanic/Latino | 1534 |
| Bachelor's or higher | 2605 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 28](/us/states/al/districts/senate/28.md) — 100% (state senate)
- [AL House District 84](/us/states/al/districts/house/84.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
