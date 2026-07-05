---
type: Jurisdiction
title: "Sullivan County, NH"
classification: county
fips: "33019"
state: "NH"
demographics:
  population: 43715
  population_under_18: 7757
  population_18_64: 25670
  population_65_plus: 10288
  median_household_income: 80858
  poverty_rate: 10.12
  homeownership_rate: 75.41
  unemployment_rate: 3.08
  median_home_value: 268700
  gini_index: 0.4608
  vacancy_rate: 24.32
  race_white: 40275
  race_black: 339
  race_asian: 125
  race_native: 21
  hispanic: 911
  bachelors_plus: 13834
districts:
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nh/districts/senate/8"
    rel: in-district
    area_weight: 0.6537
  - to: "us/states/nh/districts/senate/5"
    rel: in-district
    area_weight: 0.3051
  - to: "us/states/nh/districts/senate/7"
    rel: in-district
    area_weight: 0.0408
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Sullivan County, NH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43715 |
| Under 18 | 7757 |
| 18–64 | 25670 |
| 65+ | 10288 |
| Median household income | 80858 |
| Poverty rate | 10.12 |
| Homeownership rate | 75.41 |
| Unemployment rate | 3.08 |
| Median home value | 268700 |
| Gini index | 0.4608 |
| Vacancy rate | 24.32 |
| White | 40275 |
| Black | 339 |
| Asian | 125 |
| Native | 21 |
| Hispanic/Latino | 911 |
| Bachelor's or higher | 13834 |

## Districts

- [NH-02](/us/states/nh/districts/02.md) — 100% (congressional)
- [NH Senate District 8](/us/states/nh/districts/senate/8.md) — 65% (state senate)
- [NH Senate District 5](/us/states/nh/districts/senate/5.md) — 31% (state senate)
- [NH Senate District 7](/us/states/nh/districts/senate/7.md) — 4% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
